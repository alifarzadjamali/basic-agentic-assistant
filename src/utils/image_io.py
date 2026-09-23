from PIL import Image


def load_image(path: str) -> Image.Image:
    """Load an image into a detached RGB Pillow image."""
    with Image.open(path) as image:
        return image.convert("RGB").copy()
