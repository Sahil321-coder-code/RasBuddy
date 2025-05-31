import time
import queue
import json
import threading
import requests
import sounddevice as sd
import pyttsx3
from vosk import Model, KaldiRecognizer
import argostranslate.package
import argostranslate.translate
from PIL import Image, ImageDraw
import Adafruit_SSD1306
import os
import pygame
import random

# OLED setup
RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

WIDTH = 128
HEIGHT = 64
image = Image.new('1', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# Initialize pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Vosk model path
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"
model = Model(VOSK_MODEL_PATH)
rec = KaldiRecognizer(model, 16000)

# Queue
q = queue.Queue()

# Argos Translate
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = to_lang = None
for lang in installed_languages:
    if lang.code == 'hi': from_lang = lang
    if lang.code == 'en': to_lang = lang
translation = from_lang.get_translation(to_lang) if from_lang and to_lang else None

# Weather for Nashik
LAT, LON = 20.0110, 73.7903

# Music setup
MUSIC_FOLDER = "/home/pi/music"
pygame.mixer.init()

# Jokes and facts
jokes = [
    "Why did the computer show up at work late? It had a hard drive!",
    "Why don't robots get scared? Because they have nerves of steel!"
]

facts = [
    "Honey never spoils. Archaeologists found edible honey in ancient Egyptian tombs.",
    "Octopuses have three hearts and blue blood."
]

# Functions
def speak(text):
    engine.say(text)
    engine.runAndWait()

def draw_eyes(blink=False):
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)
    if blink:
        draw.line((30, 30, 50, 30), fill=1, width=3)
        draw.line((78, 30, 98, 30), fill=1, width=3)
    else:
        draw.ellipse((25, 20, 55, 50), outline=1, fill=1)
        draw.ellipse((75, 20, 105, 50), outline=1, fill=1)
        draw.ellipse((35, 30, 45, 40), outline=0, fill=0)
        draw.ellipse((85, 30, 95, 40), outline=0, fill=0)
    disp.image(image)
    disp.display()

def show_text(text):
    draw.rectangle((0, 54, WIDTH, HEIGHT), outline=0, fill=0)
    draw.text((0, 54), text[:20], fill=1)
    disp.image(image)
    disp.display()

def get_weather():
    try:
        r = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true", timeout=5)
        data = r.json()['current_weather']
        return data['weathercode'], data['temperature']
    except:
        return None, None

def weather_to_emoji(code):
    return {
        0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️", 45: "🌫️", 48: "🌫️",
        51: "🌦️", 53: "🌧️", 55: "🌧️", 61: "🌧️", 63: "🌧️",
        65: "🌧️", 71: "❄️", 73: "❄️", 75: "❄️", 80: "🌧️",
        81: "🌧️", 82: "🌧️", 95: "⛈️", 96: "⛈️", 99: "⛈️"
    }.get(code, "")

def audio_callback(indata, frames, time_, status):
    if status: print(status)
    q.put(bytes(indata))

def play_music():
    try:
        song = os.path.join(MUSIC_FOLDER, "song1.mp3")
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        speak("Playing song one")
        while pygame.mixer.music.get_busy(): time.sleep(1)
    except Exception as e:
        speak("Error playing music")

# Main command processor
def process_command(command):
    command = command.lower()
    print("Command:", command)

    if command in ["hello", "hey"]:
        speak("Hello there!")
        show_text("Hello")
    elif "how are you" in command:
        speak("I am good, thank you!")
        show_text("I'm good")
    elif "translate" in command and translation:
        phrase = command.replace("translate", "").strip()
        translated = translation.translate(phrase)
        speak(translated)
        show_text(translated)
    elif "weather" in command:
        code, temp = get_weather()
        if code is not None:
            emoji = weather_to_emoji(code)
            speak(f"Current temp is {temp} Celsius")
            show_text(f"{temp}C {emoji}")
        else:
            speak("Can't get weather")
    elif "play music" in command:
        play_music()
    elif "time" in command:
        now = time.strftime("%H:%M")
        speak(f"The time is {now}")
        show_text(now)
    elif "joke" in command:
        joke = random.choice(jokes)
        speak(joke)
        show_text("Joke loaded")
    elif "fun fact" in command:
        fact = random.choice(facts)
        speak(fact)
        show_text("Fun fact ready")
    else:
        speak("I didn't understand that.")

# Wake word logic
def main():
    buffer = ""
    last_time = time.time()

    speak("Hey! I'm your assistant.")
    draw_eyes()

    stream = sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=audio_callback)
    stream.start()

    wake = False

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            text = res.get("text", "")
            if text:
                print("Heard:", text)
                if not wake:
                    if "hey assistant" in text:
                        wake = True
                        speak("Yes?")
                        buffer = ""
                        last_time = time.time()
                else:
                    buffer += " " + text
                    last_time = time.time()
        else:
            partial = json.loads(rec.PartialResult()).get("partial", "")

        if wake and buffer and (time.time() - last_time > 3):
            process_command(buffer.strip())
            wake = False
            buffer = ""

        draw_eyes((int(time.time()) % 4) < 2)

if __name__ == "__main__":
    main()
