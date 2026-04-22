from agents.search_agent import build_search_agent
from agents.reader_agent import build_reader_agent
from chains.writer_chain import get_writer_chain
from chains.critic_chain import get_critic_chain

search_agent = build_search_agent()
reader_agent = build_reader_agent()
writer_chain = get_writer_chain()
critic_chain = get_critic_chain()

def run_research_pipeline(topic: str) -> dict:
    state = {}

    # 1. SEARCH
    search_res = search_agent.invoke({
        "messages": [("user", f"Find recent and reliable info about: {topic}")]
    })

    state["search"] = search_res["messages"][-1].content


    # 2. READ (SCRAPE BEST URL)
    reader_res = reader_agent.invoke({
        "messages": [("user",
            f"From these results, pick best URL and extract detailed content:\n\n{state['search'][:500]}"
        )]
    })

    state["read"] = reader_res["messages"][-1].content


    # 3. WRITE REPORT
    combined_research = f"""
    SEARCH RESULTS:
    {state['search']}

    SCRAPED CONTENT:
    {state['read']}
    """

    report = writer_chain.invoke({
        "topic": topic,
        "research": combined_research
    })

    state["report"] = report


    # 4. CRITIC
    feedback = critic_chain.invoke({
        "report": report
    })

    state["feedback"] = feedback


    return state