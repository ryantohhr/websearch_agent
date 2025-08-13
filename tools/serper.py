from langchain_community.utilities import GoogleSerperAPIWrapper
from states.graph_state import GraphState

search = GoogleSerperAPIWrapper()

def format_results(results):
    formatted_results = []
    for result in results:
        title = result.get("title", "No title")
        link = result.get("link", "No link")
        snippet = result.get("snippet", "No snippet")
        formatted_results.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n---")
    
    return "\n".join(formatted_results)

def get_serper_response(state: GraphState, get_planner_response):
    planner_response = get_planner_response()
    query = planner_response["search_query"]

    results = search.results(query)
    formatted_results = format_results(results["organic"])

    state["serper_response"] = [formatted_results]
    
    return state