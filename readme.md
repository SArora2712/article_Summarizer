# Context-Aware Article Summariser

An NLP web application that generates audience-adaptive summaries from any document. Built with TextRank + TF-IDF cosine similarity and deployed as a live Streamlit app.


---

## What it does

Most summarisers give you one generic output. This one asks who's reading it. You pick an audience profile and the summary adjusts — the same article reads differently for a software engineer, a business executive, a student, or a general audience.

Under the hood it uses TextRank (graph-based sentence ranking) combined with TF-IDF cosine similarity to score sentences by relevance. No LLM API calls, no cost, runs entirely locally.

---

## Features

- **4 audience profiles** — Technical · General · Executive · Student
- **Multi-format input** — Upload TXT, PDF, or DOCX files
- **WordCloud visualisation** — Visual keyword map of the summarised content
- **One-click PDF export** — Download the summary as a formatted PDF
- **Fully deployed** — Live on Streamlit Cloud, no setup needed to try it

---

## Tech stack

| Component | Technology |
|-----------|------------|
| NLP core | TextRank · TF-IDF · NLTK |
| Similarity | Cosine similarity (NumPy) |
| Web app | Streamlit |
| File handling | PyPDF2 · python-docx |
| Visualisation | WordCloud · Matplotlib |
| Export | FPDF |

---

## Run it locally

```bash
git clone https://github.com/SArora2712/article_Summarizer.git
cd article_Summarizer
pip install -r requirements.txt
streamlit run app.py
```

---

## How it works

1. Text is extracted from the uploaded file
2. Sentences are tokenised and cleaned
3. TF-IDF vectors are computed for each sentence
4. Cosine similarity matrix is built across all sentence pairs
5. TextRank scores each sentence based on its connections (like PageRank for text)
6. Top-N sentences are selected based on the chosen audience profile's compression ratio
7. Output is rendered in the app with optional WordCloud and PDF export

---

## Project context

Built as part of my NLP work alongside my internship at Infosys Springboard. The audience-adaptive logic came from a real observation — the same document needs to be read very differently depending on who's reading it, and most summarisers ignore that completely.

---

*Python · NLP · Streamlit · Deployed*
