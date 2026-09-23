from src.agents.knowledge_agent import KnowledgeAgent
from src.schemas import VisualAnalysis


def test_knowledge_agent_retrieves_a_local_rule_for_a_complex_request():
    visual = VisualAnalysis(
        palette=["#1f3a5f"],
        color_confidence=0.8,
        image_quality=1.0,
        needs_caption=False,
    )

    result = KnowledgeAgent().analyze(visual, "I need a smart casual work outfit")

    assert result.used_rules is True
    assert result.matches
    assert result.evidence == "Bundled fashion_rules.json"
