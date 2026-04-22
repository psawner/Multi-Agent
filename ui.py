import streamlit as st
from pipeline.pipeline import run_research_pipeline

st.set_page_config(page_title="Multi-Agent Research System", layout="wide")

st.title("🔍 Multi-Agent Research Assistant")

# Input
topic = st.text_input("Enter a research topic:")

if st.button("Run Research"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Running multi-agent pipeline..."):
            result = run_research_pipeline(topic)

        st.success("Research completed!")

        # Layout in columns
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Search Results")
            st.write(result["search"])

            st.subheader("📄 Scraped Content")
            st.write(result["read"])

        with col2:
            st.subheader("📝 Final Report")
            st.write(result["report"])

            st.subheader("🧠 Critic Feedback")
            st.write(result["feedback"])