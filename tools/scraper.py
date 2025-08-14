import requests
from bs4 import BeautifulSoup
from states.graph_state import GraphState

def get_scraper_response(state: GraphState, get_selector_response):
    selector_response = get_selector_response()

    results = []

    for response in selector_response["selected_items"]:
        
        res = requests.get(response["link"])
        soup = BeautifulSoup(res.text, "html.parser") 
        text = " ".join(soup.stripped_strings)

        new_result = {
             "title": response["title"],
             "link": response["link"],
             "text": text[:5000]
        }

        results.append(new_result)

    if "scraper_response" not in state:
            state["scraper_response"] = [results]
    else:
        state["scraper_response"].append(results)

    return state