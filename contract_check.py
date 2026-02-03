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

def analyze_contract(contract_text):
    """
    Entry point for API usage
    """
    # 👇 move or call your existing logic here
    # Example (adjust to your code):

    from clause_splitter import split_clauses
    from risk_engine import assess_risk

    clauses = split_clauses(contract_text)
    risks = assess_risk(clauses)

    return {
        "clauses": clauses,
        "risks": risks
    }
