# AI-Powered Code Reviewer

A local AI code review tool that analyzes code for bugs, warnings, improvements, best practices, and time/space complexity — runs entirely offline using a local LLM via Ollama. No API keys. No cost. No data sent to the cloud.

---

## Features

- Detects bugs, logic errors, and broken functionality
- Highlights risky patterns and edge cases
- Suggests refactors and optimizations
- Evaluates adherence to language-specific best practices
- Analyzes time and space complexity (Big-O)
- Supports Python, JavaScript, Java, C, C++, TypeScript, Go, Rust, SQL
- Fully offline — powered by CodeLlama running locally via Ollama

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript (Vanilla) |
| Backend | Python, Flask |
| AI Model | CodeLlama via Ollama |

---

## Project Structure

```
ai-code-reviewer/
├── app.py                 # Flask server — routes and entry point
├── review.py              # LLM logic — prompt engineering + Ollama call
├── templates/
│   └── index.html         # Frontend UI
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Ollama installed and running — https://ollama.com/download

### Installation

```bash
# 1. Pull the CodeLlama model (one-time, ~3.8 GB)
ollama pull codellama

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Start the app
python app.py
```

Open `http://localhost:5000` in your browser.

---

## How It Works

1. User pastes code and selects the language in the browser
2. Frontend sends a `POST /api/review` request to Flask
3. Flask calls `review.py`, which builds a structured prompt and queries CodeLlama via Ollama
4. The model returns a structured review under fixed headings
5. Frontend parses and renders the output with highlighted section titles

---

## Review Output Sections

| Section | Description |
|---|---|
| BUGS | Actual bugs, logic errors, broken functionality |
| WARNINGS | Edge cases, risky patterns, potential failures |
| IMPROVEMENTS | Refactor suggestions and optimizations |
| BEST PRACTICES | Language conventions, naming, code style |
| TIME COMPLEXITY | Big-O worst-case analysis with explanation |
| SPACE COMPLEXITY | Auxiliary space usage with explanation |
| SUMMARY | 2-3 sentence overall code quality assessment |

---

## System Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| RAM | 8 GB | 16 GB |
| Storage | 4 GB free | 8 GB free |
| OS | Windows 10/11 64-bit | Windows 11 / Linux |
| Python | 3.10+ | 3.11+ |

> If your machine has less than 8 GB RAM, run `ollama pull codellama:7b` instead.

---

## Author

**Mehul**
B.Tech CSE (AI & ML) — University of Engineering & Management, New Town, Kolkata
[GitHub](https://github.com/) • [LinkedIn](https://linkedin.com/)
