import re

def split_clauses(text):
    clauses = []

    # Split by numbered clauses like "1.", "1.1", "(a)"
    pattern = r'\n(?=\d+\.|\(\w\))'
    raw_clauses = re.split(pattern, text)

    for idx, clause in enumerate(raw_clauses):
        cleaned = clause.strip()
        legal_verbs = ["shall", "may", "must", "agree", "terminate", "indemnify"]

        if len(cleaned) < 50 or not any(v in cleaned.lower() for v in legal_verbs):
            continue


        clauses.append({
            "clause_id": f"C{idx+1}",
            "text": cleaned
        })

    return clauses
