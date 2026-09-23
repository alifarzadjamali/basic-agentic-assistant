from src.utils.color_analysis import extract_dominant_colors, get_palette_hex
from src.utils.image_io import load_image


def test_color_extraction_returns_a_three_colour_hex_palette():
    image = load_image("data/sample_images/test.jpg")

    palette = get_palette_hex(extract_dominant_colors(image, k=3))

    assert len(palette) == 3
    assert all(colour.startswith("#") and len(colour) == 7 for colour in palette)
