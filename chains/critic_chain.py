from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from model.llm import get_model

def get_critic_chain():
    #critic chain
    critic_prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are an expert research critic and quality evaluator. Your role is to critically analyze research reports for accuracy, completeness, clarity, and adherence to specifications. Provide constructive, specific feedback that helps improve the quality of research outputs.'),
    ('human', """Critically evaluate the following research report against these criteria:

    **CRITERIA FOR EVALUATION:**

    **1. ACCURACY & FACTUAL CORRECTNESS** (Weight: 30%)
    - Verify all claims are supported by the research data
    - Check for factual errors or misinterpretations
    - Ensure data is presented correctly

    **2. STRUCTURE & ORGANIZATION** (Weight: 25%)
    - Verify strict adherence to the required structure:
    - Introduction (15-20 words)
    - Key Findings (25-30 words) 
    - Analysis & Solutions (40-45 words)
    - Conclusion (10-15 words)
    - Total word count must be exactly 100 words

    **3. CLARITY & PRECISION** (Weight: 20%)
    - Assess language clarity and professionalism
    - Check for vague or ambiguous statements
    - Ensure technical accuracy in terminology

    **4. COMPLETENESS** (Weight: 15%)
    - Verify all required sections are present
    - Check that all constraints are met
    - Ensure the report addresses the topic thoroughly

    **5. ACTIONABILITY** (Weight: 10%)
    - Evaluate if solutions provided are practical
    - Check if insights lead to meaningful conclusions

    **EVALUATION FORMAT:**
    1. Overall Score: /100
    2. Strengths (2-3 points)
    3. Weaknesses (2-3 points with specific examples)
    4. Specific Recommendations for improvement
    5. Final verdict: ACCEPT / REJECT with reason

    **Report to Evaluate:**
    {report}

    Provide honest, constructive criticism focused on improvement rather than just criticism.""")
    ])

    return critic_prompt | get_model() | StrOutputParser()