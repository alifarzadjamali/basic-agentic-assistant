from src.knowledge.rule_loader import load_rules
from src.knowledge.rule_matcher import find_best_match


def test_rule_matching_returns_the_named_rule():
    result = find_best_match(["beige"], load_rules())

    assert "blue" in result["matches"]
    assert result["base_color"] == "beige"
