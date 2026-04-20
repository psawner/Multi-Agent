from langchain.tools import tool
import requests

from bs4 import BeautifulSoup
from core.config import settings

@tool
def scrape_url(url:str)->str:
    """Scrape and return clean text content from a given URL for deeper reading"""

    try:
        res = requests.get(url, timeout=settings.REQUEST_TIMEOUT, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        for i in soup(["script", "style", "nav", "footer"]):
            i.decompose()

        return soup.get_text(separator=" ", strip=True)[:300]
    
    except Exception as e:
        return f"couldn't scrape url: {str(e)}"