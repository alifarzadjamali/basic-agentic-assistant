"""Turn the workflow state into a concise, evidence-labelled answer."""

from src.agents.orchestrator import WorkflowState
from src.schemas import CriticAssessment, KnowledgeAnalysis, VisualAnalysis


class ResponseBuilder:
    def build(self, state: WorkflowState) -> str:
        visual: VisualAnalysis = state["visual_output"]
        knowledge: KnowledgeAnalysis = state["knowledge_output"]
        critic: CriticAssessment = state["critic_output"]

        lines = [
            f"Detected main colour: {knowledge.base_color.title()}.",
            f"Palette measured from the image: {', '.join(visual.palette)}.",
            f"Suggested pairings: {', '.join(knowledge.matches)}.",
            f"Style note: {knowledge.style}",
            f"Evidence: {knowledge.evidence}.",
            (
                "Critic check: "
                f"grounding={critic.grounding_score:.2f}, "
                f"completeness={critic.completeness_score:.2f}."
            ),
        ]
        if visual.caption:
            lines.append(f"Optional image caption: {visual.caption}")
        return "\n".join(lines)
