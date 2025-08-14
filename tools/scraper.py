import requests
from bs4 import BeautifulSoup
from states.graph_state import GraphState

def get_scraper_response(state: GraphState, get_selector_response):
    selector_response = get_selector_response()

    results = []

    for response in selector_response:
        res = requests.get(response.link)
        soup = BeautifulSoup(res.text, "html.parser")
        text = " ".join(soup.stripped_strings())
        results.append(text)

    if "scraper_response" not in state:
            state["scraper_response"] = [results]
    else:
        state["scraper_response"].append(results)

    return state