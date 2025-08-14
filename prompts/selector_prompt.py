selector_prompt_template = """
You are tasked with narrowing down the number of sites returned by the web search tool for scraping.

These are the sites returned by the web search tool:

{serp}

You should look through the titles and snippets of each of the sites and select those most relevant to the user's question. Follow any instructions given specifically to you by the planner.

If you receive feedback, you should adjust your selection accordingly. Also consider your previous selections.
Feedback: {feedback}
Previous selections: {prev_selections}

The current date and time is: {date}

You should respond with a list of objects in the following format:

    "title": "Title of the site selected for scraping."
    "links": "Link to the site selected for scraping."
    "snippet": "Snippet of the content from the site selected for scraping."

"""