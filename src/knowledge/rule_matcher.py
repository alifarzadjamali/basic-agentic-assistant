def find_best_match(
    detected_colors: list[str], rules: dict[str, dict[str, object]]
) -> dict[str, object]:
    """Retrieve the rule associated with the most prominent named colour."""
    base_color = detected_colors[0].lower()

    if base_color in rules:
        return {
            "base_color": base_color,
            "matches": rules[base_color]["matches"],
            "style": rules[base_color]["style"]
        }

    return {
        "base_color": base_color,
        "matches": [],
        "style": "No matching rule was found in the bundled rule set.",
    }
