# vosk_model.py
from vosk import Model

MODEL_PATH = "model/vosk-model-en-us-0.22"

print("🔄 Loading Vosk model... (Only once)")
model = Model(MODEL_PATH)
print("✅ Vosk model loaded successfully.")
