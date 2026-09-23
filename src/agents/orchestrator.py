"""The LangChain-wired workflow for the teaching example.

LangChain's Runnable interface composes the steps and gives learners a familiar
extension point. The routing policy remains ordinary Python on purpose: every
decision is easy to inspect, test, and replace.
"""

from typing import Any

from langchain_core.runnables import RunnableLambda

from src.agents.critic_agent import CriticAgent
from src.agents.knowledge_agent import KnowledgeAgent
from src.agents.visual_agent import VisualAgent
from src.config import DEFAULT_MAX_REVISIONS
from src.schemas import CriticAssessment, KnowledgeAnalysis, VisualAnalysis

WorkflowState = dict[str, Any]


class Orchestrator:
    """Run visual analysis, local retrieval, and a transparent critic loop."""

    def __init__(self, max_revisions: int = DEFAULT_MAX_REVISIONS):
        self.visual_agent = VisualAgent()
        self.knowledge_agent = KnowledgeAgent()
        self.critic_agent = CriticAgent()
        self.max_revisions = max_revisions
        self.pipeline = (
            RunnableLambda(self._run_visual)
            | RunnableLambda(self._run_knowledge)
            | RunnableLambda(self._run_critic)
        )

    def run(
        self,
        image: Any,
        user_text: str | None = None,
        *,
        image_path: str | None = None,
    ) -> WorkflowState:
        """Execute the initial chain and, if needed, one evidence-seeking retry."""
        state: WorkflowState = {
            "image": image,
            "image_path": image_path,
            "user_text": user_text,
            "revision_count": 0,
            "trace": [],
        }
        state = self.pipeline.invoke(state)

        while self._needs_revision(state):
            state["revision_count"] += 1
            state["knowledge_output"] = self.knowledge_agent.analyze(
                state["visual_output"], user_text, force_rules=True
            )
            state["trace"].append(
                "Revision: critic requested evidence, so the knowledge agent "
                "retrieved rules."
            )
            state["critic_output"] = self.critic_agent.evaluate(
                state["knowledge_output"], user_text
            )
            state["trace"].append("Critic agent: re-evaluated the revised evidence.")

        return state

    def _needs_revision(self, state: WorkflowState) -> bool:
        critic: CriticAssessment = state["critic_output"]
        return critic.needs_revision and state["revision_count"] < self.max_revisions

    def _run_visual(self, state: WorkflowState) -> WorkflowState:
        visual: VisualAnalysis = self.visual_agent.analyze(
            state["image"], image_path=state["image_path"]
        )
        state["visual_output"] = visual
        state["trace"].append(
            f"Visual agent: found {len(visual.palette)} palette colours; "
            f"captioning needed={visual.needs_caption}."
        )
        return state

    def _run_knowledge(self, state: WorkflowState) -> WorkflowState:
        knowledge: KnowledgeAnalysis = self.knowledge_agent.analyze(
            state["visual_output"], state["user_text"]
        )
        state["knowledge_output"] = knowledge
        state["trace"].append(
            f"Knowledge agent: used_rules={knowledge.used_rules}; "
            f"evidence={knowledge.evidence}."
        )
        return state

    def _run_critic(self, state: WorkflowState) -> WorkflowState:
        critic: CriticAssessment = self.critic_agent.evaluate(
            state["knowledge_output"], state["user_text"]
        )
        state["critic_output"] = critic
        state["trace"].append(
            f"Critic agent: needs_revision={critic.needs_revision}; {critic.feedback}"
        )
        return state
