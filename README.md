# Multi-Agent Research Assistant

A production ready **Multi-Agent AI system** that automates research using web search, content scraping, structured report generation, and critique — all orchestrated through a modular pipeline.

---

## Features

* 🔎 **Search Agent** – Fetches recent and reliable information from the web
* 📄 **Reader Agent** – Extracts and cleans content from selected URLs
* 📝 **Writer Chain** – Generates structured research reports (exact 100 words)
* 🧠 **Critic Chain** – Evaluates report quality with detailed feedback
* 🔗 **Pipeline Orchestration** – End-to-end automated workflow
* 🎨 **Streamlit UI** – Interactive frontend for users
* 🧩 **Modular Architecture** – Clean separation of agents, tools, chains, and config

---

## Project Structure

```
Multi-Agent/
│
├── agents/            # Agent definitions (search, reader)
├── chains/            # Writer & critic chains
├── core/              # Config & settings management
├── model/             # LLM initialization
├── pipeline/          # Main pipeline logic
├── tools/             # External tools (search, scraper)
│
├── app.py             # CLI entry point
├── ui.py              # Streamlit UI
├── requirements.txt
├── .env
└── README.md
```

---

## Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/psawner/Multi-Agent
cd Multi-Agent
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
MODEL_NAME=openai/gpt-oss-120b
```

---

## ▶️ Running the Project

### 🔹 Option 1: Streamlit UI (Recommended)

```
streamlit run ui.py
```

👉 Open in browser: http://localhost:8501

---

### 🔹 Option 2: CLI Mode

```
python app.py
```

---

## Pipeline Flow

```
User Input
   ↓
Search Agent (Web Search)
   ↓
Reader Agent (Scrape Content)
   ↓
Writer Chain (Generate Report)
   ↓
Critic Chain (Evaluate Report)
   ↓
Final Output
```

---

## 🧠 Tech Stack

* **LLM**: Groq (via LangChain)
* **Framework**: LangChain (Agents & Chains)
* **Search API**: Tavily
* **Web Scraping**: BeautifulSoup
* **Frontend**: Streamlit
* **Language**: Python

---

## Example Output

### Research Report

* Structured into Introduction, Findings, Analysis, and Conclusion
* Exactly 100 words (strict constraint handling)

### Critic Feedback

* Score out of 100
* Strengths & weaknesses
* Actionable recommendations

---

## Key Learnings

* Designing multi-agent systems
* Tool integration with LLMs
* Pipeline orchestration
* Modular & scalable architecture
* Separating config, logic, and execution layers

---

## Future Improvements

* Add retry logic & state management (LangGraph)
* Streaming responses for real-time output
* Deploy using AWS
* Export reports as PDF
* Add more specialized agents (planner, verifier)

---

## Environment & Security

* API keys are managed via `.env` file
* Centralized configuration using a config module
* Production-ready approach (can integrate with AWS Secrets Manager / Docker env variables)

---

## License

This project is for educational and learning purposes.

---

## Acknowledgement

This project demonstrates a real-world **multi-agent AI architecture**, combining reasoning, tool usage, and evaluation in a structured pipeline.
