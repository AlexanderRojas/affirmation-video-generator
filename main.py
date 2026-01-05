from src.pipeline import run_pipeline
from src.config import INPUT_DIR

if __name__ == "__main__":
    text = (INPUT_DIR / "affirmation.txt").read_text(encoding="utf-8")
    run_pipeline(text)