from src.agents.critic_agent import CriticAgent
from src.schemas import KnowledgeAnalysis


def test_critic_requests_revision_for_an_ungrounded_fallback():
    knowledge = KnowledgeAnalysis(
        base_color="blue",
        matches=["white", "black"],
        style="Fallback advice.",
        used_rules=False,
        retrieval_confidence=0.4,
        evidence="No rule retrieval",
    )

    result = CriticAgent().evaluate(knowledge)

    assert result.needs_revision is True
    assert "Retrieve" in result.feedback
