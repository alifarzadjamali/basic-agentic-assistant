import numpy as np
from sklearn.cluster import KMeans


def extract_dominant_colors(image, k: int = 3) -> list[np.ndarray]:
    """Return up to ``k`` RGB colours, ordered by how common they are.

    K-means can return its cluster centres in arbitrary order. Ordering by pixel
    count makes the first colour a stable, explainable input to the next agent.
    """
    if k < 1:
        raise ValueError("k must be at least 1")

    resized = image.convert("RGB").resize((150, 150))
    pixels = np.array(resized).reshape(-1, 3)
    cluster_count = min(k, len(pixels))

    kmeans = KMeans(n_clusters=cluster_count, n_init=10, random_state=42)
    kmeans.fit(pixels)

    counts = np.bincount(kmeans.labels_, minlength=cluster_count)
    order = np.argsort(-counts, kind="stable")
    return [kmeans.cluster_centers_[index].astype(int) for index in order]


def rgb_to_hex(color: np.ndarray) -> str:
    red, green, blue = color
    return f"#{red:02x}{green:02x}{blue:02x}"


def get_palette_hex(colors: list[np.ndarray]) -> list[str]:
    return [rgb_to_hex(c) for c in colors]
