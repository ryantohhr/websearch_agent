from graph import build_graph

graph = build_graph()

while True:

    user_question = input("Question: ")

    if (user_question.lower() == "quit"):
        break

    graph.invoke({"user_question": user_question}, {"recursion_limit": 10})
