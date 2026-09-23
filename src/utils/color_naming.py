"""Map a measured RGB value to one of the colours supported by local rules."""

from math import dist

REFERENCE_COLOURS = {
    "black": (20, 20, 20),
    "white": (245, 245, 245),
    "blue": (45, 91, 155),
    "brown": (120, 75, 45),
    "beige": (215, 195, 155),
    "grey": (128, 128, 128),
    "green": (70, 125, 80),
    "red": (170, 55, 50),
}


def simple_color_name(hex_color: str) -> str:
    """Choose the nearest named reference using Euclidean RGB distance."""
    value = hex_color.removeprefix("#")
    if len(value) != 6:
        raise ValueError(f"Expected a six-digit hexadecimal colour, got {hex_color!r}")

    try:
        rgb = tuple(int(value[index : index + 2], 16) for index in range(0, 6, 2))
    except ValueError as error:
        raise ValueError(f"Invalid hexadecimal colour: {hex_color!r}") from error

    return min(REFERENCE_COLOURS, key=lambda name: dist(rgb, REFERENCE_COLOURS[name]))
