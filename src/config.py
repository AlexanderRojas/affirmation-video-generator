# src/config.py

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

IMAGES_DIR = OUTPUT_DIR / "images"
AUDIO_DIR = OUTPUT_DIR / "audio"
VIDEO_DIR = OUTPUT_DIR / "video"

FONT_PATH = BASE_DIR / "fonts" / "DejaVuSans-Bold.ttf"

# Voice settings
VOICE_RATE = 160   # slow, calm, affirmations
VOICE_VOLUME = 1.0  # 0.0 – 1.0

# Video
VIDEO_FPS = 24
FADE_DURATION = 0.5

VOICE_LANGUAGE = "es"
