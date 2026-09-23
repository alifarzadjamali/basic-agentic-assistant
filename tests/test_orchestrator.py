from src.agents.orchestrator import Orchestrator
from src.utils.image_io import load_image


def test_orchestrator_runs_the_langchain_pipeline():
    image = load_image("data/sample_images/test.jpg")

    result = Orchestrator().run(image, "I want a smart casual outfit")

    assert result["visual_output"].palette
    assert result["knowledge_output"].used_rules is True
    assert result["critic_output"].needs_revision is False
    assert len(result["trace"]) == 3


def test_orchestrator_retries_with_rules_when_the_first_route_is_a_fallback():
    image = load_image("data/sample_images/test.jpg")

    result = Orchestrator().run(image, "Help")

    assert result["revision_count"] == 1
    assert result["knowledge_output"].used_rules is True
    assert "Revision:" in result["trace"][3]
