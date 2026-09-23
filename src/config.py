"""Project-wide paths and stable defaults."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DEFAULT_RULES_PATH = DATA_DIR / "fashion_rules.json"
DEFAULT_IMAGE_PATH = DATA_DIR / "sample_images" / "test.jpg"
DEFAULT_REQUEST = "I want a smart casual outfit."
DEFAULT_MAX_REVISIONS = 1
