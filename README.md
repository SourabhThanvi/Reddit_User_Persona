# Reddit User Persona Generator

Automatically generates a detailed evidence-based persona for any Reddit user by analyzing their posts and comments via LLM-powered synthesis. Output is a clean, structured, plain-text persona file—ready for research, product design, or analysis.

---

## Features

- **Reddit Data Scraping**: Collects both posts and comments from any public Reddit profile.
- **Persona Synthesis with LLM**: Uses cutting-edge Large Language Models (via Gemini/OpenAI) to distill key interests, personality traits, behavioral patterns, expertise, and communication style.
- **Cited Evidence**: Each trait or insight is supported by direct quotes or references from the user’s Reddit activity.
- **Human-Readable Output**: Exports a Markdown-free `.txt` persona file.
- **API & Frontend**:
  - FastAPI-based backend for automated persona generation.
  - Streamlit frontend for easy user interaction.

---

## Quickstart

### 1. Clone the Repository

git clone <your_repo_url>
cd <your_repo_directory>

### 2. Create a Virtual Environment

#### a) Using `uv` (**Preferred**)
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt

**recommend [uv](https://github.com/astral-sh/uv) for fast, reproducible environments.**

#### b) Using `conda`
conda create -n reddit_persona python=3.10
conda activate reddit_persona
pip install -r requirements.txt

---

### 3. Configure Reddit and LLM API Keys

Create a `.env` file in the project root:
REDDIT_ID=your_reddit_app_id
REDDIT_SECRET=your_reddit_app_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
GEMINI_API_KEY=your_gemini_api_key

- Your Reddit app **must** be “script” type.
- Gemini API key is required for LLM-based persona generation.

---

### 4. Running the Application

#### A. API Backend (FastAPI)
uvicorn main:app --reload

- Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

#### B. Streamlit Frontend
streamlit run app.py

- Visit [http://localhost:8501](http://localhost:8501) for the web interface.

---

### 5. How to Use

1. **Input**: Enter a Reddit profile URL (`https://www.reddit.com/user/username`).
2. **Processing**: The system scrapes the user's comments and posts, analyzes them with LLM, and generates a detailed persona with evidence.
3. **Output**: Download the persona as a plain `.txt` file via the UI, or retrieve via the API.

---

## Project Structure

``` 
Reddit_User_Persona
├── llm/
│ ├── llm_invoke.py # LLM invocation and persona synthesis
│ ├── persona_file_creation.py # Markdown removal, file output
├── prompts/
│ ├── comment_prompt.py
│ ├── post_prompt.py
│ ├── persona_prompt.py
│ ├── system_prompt.py
├── reddit_scraper/
│ ├── scrape_comments.py
│ ├── scrape_posts.py
├── main.py # FastAPI backend
├── app.py # Streamlit web UI
├── requirements.txt
└── .env # (user secrets, not checked in)
```

## Tech Stack

- Python 3.10+
- **PRAW** (Reddit scraping)
- **FastAPI** (backend API)
- **Streamlit** (frontend)
- **Gemini/OpenAI** LLMs
- `strip-markdown` (for removing markdown in output)

---

## Example Output

Plain-text persona files can be downloaded via the app or API for any Reddit user, formatted for clarity and direct use.

---

## License

MIT — see `LICENSE`.

---

## Contributing

Open to issues and pull requests — for major changes, please open an issue first.
