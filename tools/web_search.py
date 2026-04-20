from langchain.tools import tool
from tavily import TavilyClient

from core.config import settings
tavily = TavilyClient(api_key=settings.TAVILY_API_KEY)

@tool
def web_search(query: str)-> str:
    """Searach the web for recent and reliable information on a topic. returns titles, URLs and snippts"""
    res = tavily.search(query=query, max_results=5)

    results = res.get("results", [])

    if not results:
        return f"Not found"
    
    news_list = []
    
    for r in results:
        title = r.get("title", "no title")
        url = r.get("url","")
        snippt = r.get("content","")

        news_list.append(
            f"- {title}\n {url}\n {snippt[:100]}...."
        )
    
    return "\n------------\n".join(news_list)


    
