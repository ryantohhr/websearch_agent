from typing import TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from agents.base_agent import BaseAgent
from prompts.reporter_prompt import reporter_prompt_template
from utils.date import get_date

class ReporterAgent(BaseAgent):
    def invoke(self, user_question, prompt=reporter_prompt_template, get_feedback=None, get_context=None, get_prev_reports=None):
        reviewer_response = get_feedback()
        feedback = reviewer_response.content["feedback"] if reviewer_response else ""

        reporter_prompt = prompt.format(
            context=get_context(),
            date=get_date(),
            feedback=feedback,
            prev_reports=get_prev_reports()
        )

        messages = [
            SystemMessage(content=reporter_prompt),
            HumanMessage(content=user_question)
        ]

        llm = self.get_llm()
        llm_with_structured_output = llm.with_structured_output(ReporterOutput)
        response = llm_with_structured_output.invoke(messages)

        self.update_state("reporter_response", response)

        return self.state

class ReporterOutput(TypedDict):
    report: str