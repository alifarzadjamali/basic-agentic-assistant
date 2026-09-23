import json
from pathlib import Path

from src.config import DEFAULT_RULES_PATH


def load_rules(path: Path | str = DEFAULT_RULES_PATH) -> dict[str, dict[str, object]]:
    """Load the bundled, local rule set.

    This is retrieval from project data, not a live external source.
    """
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)
