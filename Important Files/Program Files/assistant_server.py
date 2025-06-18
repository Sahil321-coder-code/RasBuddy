import sounddevice as sd
import queue
import json
import pyttsx3
from vosk import Model, KaldiRecognizer
import requests
import wikipedia
import serial

q = queue.Queue()
model = Model("vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)
engine = pyttsx3.init()

try:
    esp = serial.Serial('COM3', 115200)
except:
    esp = None

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()
    if esp:
        esp.write((text + "\n").encode())

def translate_hi_en(text):
    try:
        res = requests.post("http://localhost:5000/translate", json={
            "q": text,
            "source": "hi",
            "target": "en",
            "format": "text"
        })
        return res.json()['translatedText']
    except:
        return "Translation failed."

def handle_query(text):
    text = text.lower()
    if "how are you" in text:
        return "I am doing great! Thanks for asking."
    elif "joke" in text:
        return "Why did the computer go to the doctor? Because it had a virus!"
    elif "fact" in text:
        return "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3000 years old!"
    elif "what is" in text:
        try:
            query = text.replace("what is", "").strip()
            return wikipedia.summary(query, sentences=2)
        except:
            return "Sorry, I couldn't find info on that."
    else:
        return "I am still learning to answer that."

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def main():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print("You said:", text)
                    response = handle_query(text)
                    speak(response)

if __name__ == "__main__":
    main()
