from typing import TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from utils.date import get_date
from agents.base_agent import BaseAgent
from prompts.planner_prompt import planner_prompt_template

class PlannerAgent(BaseAgent):
    def invoke(self, user_question, prompt=planner_prompt_template, get_feedback=None):
        reviewer_response = get_feedback()
        feedback = reviewer_response.content["feedback"] if reviewer_response else ""

        planner_prompt = prompt.format(feedback=feedback, date=get_date())

        messages = [
            SystemMessage(content=planner_prompt),
            HumanMessage(content=user_question)
        ]

        llm = self.get_llm()
        llm_with_structured_output = llm.with_structured_output(PlannerOutput)
        response = llm_with_structured_output.invoke(messages)

        self.update_state("planner_response", response)

        return self.state
    
class PlannerOutput(TypedDict):
    search_query: str
    overall_strategy: str
    additional_information: str