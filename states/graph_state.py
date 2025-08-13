import operator
from typing import List, TypedDict, Annotated

class GraphState(TypedDict):
    user_question: str
    planner_response: Annotated[List, operator.add]
    selector_response: Annotated[List, operator.add]
    reporter_response: Annotated[List, operator.add]
    reviewer_response: Annotated[List, operator.add]
    router_response: Annotated[List, operator.add]
    serper_response: Annotated[List, operator.add]
    scraper_response: Annotated[List, operator.add]
    final_answer: Annotated[List, operator.add]