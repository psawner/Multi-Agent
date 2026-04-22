from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from model.llm import get_model

#writer chain
def get_writer_chain():
    writer_prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are an expert research writer specializing in technical and business analysis. Write clear, structured, and insightful reports that are concise yet comprehensive. Always follow the specified structure and word limits exactly.'),
        ('human', """Write a detailed research report on the topic below following this exact structure:

        **I. INTRODUCTION** (15-20 words)
        - Brief overview of the topic and its significance

        **II. KEY FINDINGS** (25-30 words)
        - List 3-4 main discoveries or insights from the research

        **III. ANALYSIS & SOLUTIONS** (40-45 words)
        - Explain WHY these findings matter and HOW they impact the subject
        - Provide actionable solutions or recommendations

        **IV. CONCLUSION** (10-15 words)
        - Summarize the key takeaway or next step

        **Topic**: {topic}
        **Research Data**: {research}

        **Constraints**: 
        - Total word count: Exactly 100 words
        - Must follow the structure above exactly
        - Use professional, analytical language
        - Avoid fluff or filler content

        Ensure every section contributes meaningfully to the overall analysis.""")
    ])

    return writer_prompt | get_model() | StrOutputParser()