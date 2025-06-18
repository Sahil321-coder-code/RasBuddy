from flask import Flask, request, jsonify
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import argostranslate.package
import argostranslate.translate
import queue
import json

app = Flask(__name__)

# Load Vosk model
model = Model("vosk-model")
rec = KaldiRecognizer(model, 16000)

# Install Argos model if not already
argostranslate.package.install_from_path("translate-models/hi_en.argosmodel")

langs = argostranslate.translate.get_installed_languages()
from_lang = next(filter(lambda x: x.code == "hi", langs), None)
to_lang = next(filter(lambda x: x.code == "en", langs), None)
translation = from_lang.get_translation(to_lang)

q = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status: print(status)
    q.put(bytes(indata))

@app.route('/translate', methods=['POST'])
def translate_audio():
    audio_data = request.data
    q.put(audio_data)

    if rec.AcceptWaveform(audio_data):
        result = json.loads(rec.Result())
        text = result.get("text", "")
        if text:
            translated = translation.translate(text)
            return jsonify({"translated": translated})
    return jsonify({"translated": "Couldn't understand audio."})

if __name__ == '__main__':
    print("Starting assistant server...")
    app.run(host='0.0.0.0', port=5000)
