import sounddevice as sd
import queue
import json
import pyttsx3
import random
import requests
from vosk import Model, KaldiRecognizer

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load Vosk English model
model = Model("vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)

# Translation function (Hindi → English)
def translate(text):
    try:
        response = requests.post(
            "http://localhost:5000/translate",
            headers={"Content-Type": "application/json"},
            json={
                "q": text,
                "source": "hi",
                "target": "en",
                "format": "text"
            }
        )
        return response.json()["translatedText"]
    except Exception as e:
        print("Translation error:", e)
        return text

# Text-to-speech
def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

# Voice input queue
q = queue.Queue()
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# Jokes, facts, responses
jokes = [
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "How do you organize a space party? You planet!",
    "Why was the math book sad? It had too many problems.",
    "I told my computer I needed a break, and it said no problem—it would go to sleep.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

facts = [
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries aren't.",
    "A bolt of lightning is five times hotter than the sun.",
    "Honey never spoils.",
    "Sharks are older than trees."
]

responses = {
    "how are you": "I'm doing great, thank you!",
    "hello": "Hello there!",
    "what is your name": "I'm your voice assistant.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!"
}

# Run the voice assistant
print("Listening... Speak in English or Hindi.")

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "").strip()
            if not text:
                continue

            print("Recognized:", text)

            # Detect Hindi (very simple check)
            if any('\u0900' <= c <= '\u097F' for c in text):
                print("Detected Hindi, translating...")
                text = translate(text)
                print("Translated to English:", text)

            response = None
            for key in responses:
                if key in text.lower():
                    response = responses[key]
                    break

            if not response:
                if "joke" in text.lower():
                    response = random.choice(jokes)
                elif "fact" in text.lower():
                    response = random.choice(facts)
                else:
                    response = "You said: " + text

            speak(response)
