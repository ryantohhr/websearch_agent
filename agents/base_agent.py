from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

class BaseAgent:
    def __init__(self, state):
        self.state = state

    def get_llm(self):
        llm = ChatAnthropic(
            model="claude-3-haiku-20240307"
        )

        return llm
    
    def update_state(self, key, value):
        self.state[key] = value