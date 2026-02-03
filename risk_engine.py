def assess_risk(clause_text):

    # ✅ SAFETY FIX (THIS IS THE KEY LINE)
    if isinstance(clause_text, list):
        clause_text = " ".join(clause_text)

    text = clause_text.lower()

    rules = [
        ("terminate at any time", "High", "Unilateral termination without protection"),
        ("indemnify", "High", "Unlimited indemnity obligation"),
        ("hold harmless", "High", "Broad indemnity wording"),
        ("exclusive jurisdiction", "Medium", "Restrictive jurisdiction clause"),
        ("auto-renew", "Medium", "Automatic renewal without exit option"),
        ("non-compete", "High", "Restrictive non-compete obligation"),
        ("penalty", "Medium", "Penalty clause may be unfavorable"),
    ]

    for keyword, risk, reason in rules:
        if keyword in text:
            return {
                "risk": risk,
                "reason": reason
            }

    return {
        "risk": "Low",
        "reason": "No major risk indicators found"
    }
