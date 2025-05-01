from dotenv import load_dotenv
load_dotenv()

from elevenlabs.client import ElevenLabs
from elevenlabs import play, VoiceSettings
import os
import uuid
from datetime import datetime

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

def speak(text: str):
    try:
        audio_stream = client.generate(
            text=text,
            voice="21m00Tcm4TlvDq8ikWAM", #Voice ID
            model="eleven_multilingual_v2",
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.5
            )
        )
        audio = b"".join(audio_stream)

        # Unique filename for saving
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_id = uuid.uuid4().hex[:6]
        filename = f"assets/voice_samples/output_{timestamp}_{file_id}.wav"

        os.makedirs("assets/voice_samples", exist_ok=True)
        with open(filename, "wb") as f:
            f.write(audio)

        play(audio)

    except Exception as e:
        print(f"⚠️ Audio playback failed. Error: {e}")
        print("🗨️ Fallback text response:\n", text)