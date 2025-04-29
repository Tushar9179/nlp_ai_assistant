import queue
import sounddevice as sd
import json
from vosk import KaldiRecognizer

from vosk_model import model
from predict import predict_intent
from speech_output import speak

recognizer = KaldiRecognizer(model, 16000)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print("Stream status:", status)
    q.put(bytes(indata))

def listen_for_command():
    print("🎤 Say something...")

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if text:
                    print("✅ You said:", text)
                    return text

# if __name__ == "__main__":
#     while True:
#         user_input = listen_for_command()
#         response = predict_intent(user_input)
#         print("🤖 Bot:", response)
#         speak(response)
