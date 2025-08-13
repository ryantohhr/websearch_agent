from langgraph.graph import StateGraph, START, END
from states.graph_state import GraphState
from states.state_getter import state_getter
from agents.planner_agent import PlannerAgent

builder = StateGraph(GraphState)

builder.add_node(
    "planner",
    lambda state: PlannerAgent(state).invoke(
        user_question=state["user_question"],
        feedback=lambda: state_getter(state, "reviewer_response")
        ))

builder.add_edge(START, "planner")
builder.add_edge("planner", END)

graph = builder.compile()

print(graph.invoke({"user_question": "What is the capital of France?"}))