import vosk
import sounddevice as sd
import queue
import json
import pyttsx3
import serial
import requests
import random

# Initialize
q = queue.Queue()
model = vosk.Model("vosk-model-small-en-us-0.15")
samplerate = 16000
ser = serial.Serial('COM3', 115200)  # Change COM port accordingly
engine = pyttsx3.init()

# Fun facts & jokes
facts = [
    "The sun is 93 million miles away.",
    "Octopuses have three hearts.",
    "Honey never spoils.",
    "Bananas are berries.",
    "Your brain uses 20 percent of your body's energy."
]

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer get cold? Because it forgot to close windows.",
    "What did the zero say to the eight? Nice belt!",
    "Why can't you trust stairs? They're always up to something.",
    "What’s orange and sounds like a parrot? A carrot."
]

# Listen callback
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def translate_hi_to_en(text):
    try:
        r = requests.post("http://localhost:5000/translate", json={
            "q": text,
            "source": "hi",
            "target": "en",
            "format": "text"
        })
        return r.json()["translatedText"]
    except Exception as e:
        print("Translation failed:", e)
        return text

# Main loop
def main():
    print("Listening...")
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if not text:
                    continue
                print("You said:", text)

                # If text is Hindi, translate
                if any('\u0900' <= char <= '\u097F' for char in text):
                    text = translate_hi_to_en(text)
                    print("Translated to:", text)

                # Respond to commands
                if "how are you" in text:
                    speak("I'm doing great, thank you!")
                    ser.write(b"happy\n")

                elif "tell me a joke" in text:
                    joke = random.choice(jokes)
                    speak(joke)
                    ser.write(b"joke\n")

                elif "tell me a fact" in text:
                    fact = random.choice(facts)
                    speak(fact)
                    ser.write(b"fact\n")

                elif "hello" in text or "hi" in text:
                    speak("Hello there! I'm your assistant.")
                    ser.write(b"hello\n")

                elif "bye" in text:
                    speak("Goodbye!")
                    break

                else:
                    speak("I heard you say: " + text)
                    ser.write((text + '\n').encode())

if __name__ == "__main__":
    main()
