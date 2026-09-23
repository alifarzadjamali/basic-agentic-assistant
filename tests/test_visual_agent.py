from src.agents.visual_agent import VisualAgent
from src.utils.image_io import load_image


def test_visual_agent_returns_a_typed_analysis_without_loading_captioning():
    image = load_image("data/sample_images/test.jpg")

    result = VisualAgent().analyze(image)

    assert result.palette
    assert result.needs_caption is False
    assert result.caption is None
