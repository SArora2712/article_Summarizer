def audience_weight(sentence, audience):
    sentence = sentence.lower()

    if audience == "Student":
        keywords = ["define", "introduction", "basic", "concept"]
    elif audience == "Professional":
        keywords = ["impact", "industry", "business", "market"]
    elif audience == "Developer":
        keywords = ["algorithm", "model", "system", "data"]
    else:
        keywords = []

    return 0.05 * sum(word in sentence for word in keywords)
