def explain_clause(clause_text, risk_level, reason):
    return f"""
### 🤖 Clause Explanation (Demo Mode)

**What this clause means:**  
This clause defines obligations or liabilities that may apply to one or more parties in the agreement.

**Why this is risky:**  
This clause is classified as **{risk_level} risk** because **{reason.lower()}**.  
Such wording may expose a small business to obligations that are difficult to limit or control.

**Suggested balanced alternative:**  
Consider:
- Adding clear caps on liability  
- Making obligations mutual instead of one-sided  
- Narrowing the scope of indemnification or penalties  

⚠️ *This explanation is generated in demo mode for hackathon purposes and does not constitute legal advice.*
"""
