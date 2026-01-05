from .text_utils import split_sentences
from .image_generator import create_image
from .audio_generator import generate_voice
from .video_generator import build_video
from .config import *

def run_pipeline(text: str):
    
    sentences = split_sentences(text)
    
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    timeline = []
 

    for i, sentence in enumerate(sentences, start=1):
        audio_file = AUDIO_DIR / f"sentence_{i:02}.wav"
        image_file = IMAGES_DIR / f"sentence_{i:02}.png"

        generate_voice(sentence, audio_file)
        create_image(sentence, image_file)

        timeline.append((image_file, audio_file))

    build_video(timeline)