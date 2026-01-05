from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips
)

from .config import VIDEO_DIR, VIDEO_FPS


def build_video(timeline):
    """
    Build final video from (image, audio) timeline.
    """
      
    clips = []

    for image_path, audio_path in timeline:
        audio = AudioFileClip(str(audio_path))

        clip = (
            ImageClip(str(image_path))
            .with_duration(audio.duration)
            .with_audio(audio)
        )

        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose")

    output_file = VIDEO_DIR / "affirmation_video.mp4"

    final_video.write_videofile(
        str(output_file),
        fps=VIDEO_FPS,
        codec="libx264",
        audio_codec="aac"
    )
