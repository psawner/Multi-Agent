from langchain.agents import create_agent
from tools.scrape import scrape_url
from model.llm import get_model

def build_reader_agent():
    return create_agent(
        model=get_model(),
        tools=[scrape_url]
    )