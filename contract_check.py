def looks_like_contract(text):
    keywords = [
        "agreement",
        "party",
        "parties",
        "shall",
        "hereby",
        "term",
        "termination",
        "liability",
        "governing law"
    ]

    text_lower = text.lower()
    score = sum(1 for k in keywords if k in text_lower)

    return score >= 3
