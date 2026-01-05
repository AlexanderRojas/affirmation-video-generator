from pathlib import Path
import pyttsx3
from pydub import AudioSegment

from .config import VOICE_RATE, VOICE_VOLUME


def generate_voice(sentence: str, output_file: Path):
    """
    Generate a spoken audio file from text (voice only, no alpha waves).
    """

    engine = pyttsx3.init()

 # Select Spanish voice
    for voice in engine.getProperty("voices"):
        if "Spanish" in voice.name or "Sabina" in voice.name:
            engine.setProperty("voice", voice.id)
            break



    # Apply voice configuration
    engine.setProperty("rate", VOICE_RATE)
    engine.setProperty("volume", VOICE_VOLUME)

    engine.save_to_file(sentence, str(output_file))
    engine.runAndWait()

    # Post-process audio
    voice_audio = AudioSegment.from_wav(output_file).normalize()

    # Export final audio
    voice_audio.export(output_file, format="wav")
