from src.generation.response_builder import ResponseBuilder
from src.schemas import CriticAssessment, KnowledgeAnalysis, VisualAnalysis


def test_response_builder_labels_the_evidence():
    state = {
        "visual_output": VisualAnalysis(
            palette=["#1f3a5f"],
            color_confidence=0.8,
            image_quality=1.0,
            needs_caption=False,
        ),
        "knowledge_output": KnowledgeAnalysis(
            base_color="blue",
            matches=["white", "grey"],
            style="Blue works well with neutral colours.",
            used_rules=True,
            retrieval_confidence=1.0,
            evidence="Bundled fashion_rules.json",
        ),
        "critic_output": CriticAssessment(1.0, 1.0, False, "Enough evidence."),
    }

    response = ResponseBuilder().build(state)

    assert "Blue" in response
    assert "Evidence: Bundled fashion_rules.json." in response
