import re

def sentence_length(sentence):
    return len(sentence.split())

def technical_density(sentence):
    tech_words = [
        "algorithm", "model", "framework", "neural",
        "learning", "data", "analysis", "system",
        "architecture", "automation", "bias"
    ]
    words = sentence.lower().split()
    return sum(1 for w in words if w in tech_words) / max(len(words), 1)

def is_definition(sentence):
    return any(k in sentence.lower() for k in [" is ", " means ", " refers to ", " allows "])

# ---------------- STUDENT ----------------
def student_filter(ranked, top_n):
    selected = [s for s, _ in ranked if sentence_length(s) <= 20 and is_definition(s)]
    return (selected + [s for s, _ in ranked])[:top_n]

# ---------------- PROFESSIONAL ----------------
def professional_filter(ranked, top_n):
    selected = [s for s, _ in ranked if 15 <= sentence_length(s) <= 30]
    return (selected + [s for s, _ in ranked])[:top_n]

# ---------------- RESEARCHER ----------------
def researcher_filter(ranked, top_n):
    selected = [s for s, _ in ranked if technical_density(s) > 0.18]
    return (selected + [s for s, _ in ranked])[:top_n]

# ---------------- GENERAL (FIXED) ----------------
def general_filter(ranked, top_n):
    selected = [
        s for s, _ in ranked
        if 12 <= sentence_length(s) <= 25
    ]
    return (selected + [s for s, _ in ranked])[:top_n]

# ---------------- DISPATCH ----------------
def get_audience_summary(ranked, audience, top_n):
    audience = audience.lower()

    if audience == "student":
        return student_filter(ranked, top_n)
    elif audience == "professional":
        return professional_filter(ranked, top_n)
    elif audience == "researcher":
        return researcher_filter(ranked, top_n)
    elif audience == "general":
        return general_filter(ranked, top_n)
    else:
        raise ValueError("Invalid audience")
