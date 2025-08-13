from langgraph.graph import StateGraph, START, END
from states.graph_state import GraphState
from states.state_getter import state_getter
from agents.planner_agent import PlannerAgent
from tools.serper import get_serper_response

builder = StateGraph(GraphState)

builder.add_node(
    "planner",
    lambda state: PlannerAgent(state).invoke(
        user_question=state["user_question"],
        get_feedback=lambda: state_getter(state, "reviewer_latest")
    )
)

builder.add_node(
    "serper_tool",
    lambda state: get_serper_response(
        state=state,
        get_planner_response=lambda: state_getter(state, "planner_latest")
    )
)

builder.add_edge(START, "planner")
builder.add_edge("planner", "serper_tool")
builder.add_edge("serper_tool", END)

graph = builder.compile()

print(graph.invoke({"user_question": "What is the capital of France?"}))