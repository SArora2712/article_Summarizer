def classify_sentence(sentence):
    s = sentence.lower()

    if any(w in s for w in ["advantage", "benefit", "improve"]):
        return "Pros"
    if any(w in s for w in ["risk", "challenge", "issue"]):
        return "Cons"
    if any(w in s for w in ["future", "will", "expected"]):
        return "Future"
    return "Key Points"
