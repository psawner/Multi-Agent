from langchain.agents import create_agent
from tools.web_search import web_search
from model.llm import get_model

def build_search_agent():
    return create_agent(
        model=get_model(),
        tools=[web_search]
    )