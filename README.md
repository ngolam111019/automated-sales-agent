# Automated Sales Agent (AI-Powered E-Commerce Pipeline)

**Automated Sales Agent** is an end-to-end Python pipeline designed to autonomously scrape competitor product data, extract structured information using Large Language Models (LLMs), store it in a relational database, and automatically generate high-converting, SEO-optimized comparison PR articles.

## 🚀 Features

*   **Intelligent Web Crawling (Phase 1):** Uses `Crawl4AI` and Playwright headless browsers to bypass basic anti-bot protections, render JavaScript, and extract clean, LLM-friendly Markdown from complex e-commerce DOMs.
*   **Structured Data Extraction (Phase 2):** Integrates **Google Gemini 2.5 Flash** API with **Pydantic** schemas (`Structured Outputs`) to precisely parse raw Markdown into deterministic JSON formats (Product Name, Prices, Specifications, Features).
*   **Relational Database (Phase 3):** Employs **PostgreSQL** (containerized via Docker) and **SQLAlchemy ORM** to store and relate product data, specs, and features robustly.
*   **AI Content Generation (Phase 3):** A Prompt-Chaining engine that feeds on database records to automatically write objective, persuasive, and SEO-friendly comparison articles.
*   **Automated Orchestration (Phase 4):** A central orchestrator using the `schedule` library to run the entire pipeline (Crawling -> Extraction -> Storage -> Generation) completely hands-free on a defined chronogram.

## 🛠️ Tech Stack

*   **Language:** Python 3.11+
*   **Web Scraper:** Crawl4AI, Playwright
*   **AI / LLM:** Google Gemini API (`gemini-2.5-flash`), `google-genai` SDK
*   **Database & ORM:** PostgreSQL (Docker), SQLAlchemy, psycopg2
*   **Data Validation:** Pydantic
*   **Automation:** schedule

## 🏗️ Architecture

```text
[Target URL] 
   │
   ▼ (Playwright / Crawl4AI)
[Raw Markdown] 
   │
   ▼ (Gemini API + Pydantic Schema)
[Structured JSON Data] 
   │
   ▼ (SQLAlchemy ORM)
[PostgreSQL Database] 
   │
   ▼ (Comparison Engine)
[Gemini AI Content Generator] 
   │
   ▼
[SEO-Optimized PR Markdown Report]
```

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/automated-sales-agent.git
   cd automated-sales-agent
   ```

2. **Set up the virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   crawl4ai-setup # Install Playwright browsers
   ```

3. **Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   DATABASE_URL=postgresql://sales_agent:secretpassword@localhost:15432/sales_agent_db
   ```

4. **Start PostgreSQL Database:**
   ```bash
   docker-compose up -d
   ```

## 🏃‍♂️ Usage

Run the main orchestrator to execute the pipeline:
```bash
export PYTHONPATH=.
python main.py
```
*The script will immediately run a test loop and then enter background scheduling mode (e.g., executing at 08:00 AM daily).*

Generated PR articles will be saved in the `reports/` directory.

## 👤 Author
**[Your Name/Your Portfolio Link]**  
*Role: Technical Lead / AI & Data Pipeline Engineer*
