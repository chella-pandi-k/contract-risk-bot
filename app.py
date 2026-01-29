import streamlit as st
import pdfplumber
from docx import Document
from clause_splitter import split_clauses
from risk_engine import assess_risk
from llm_helper import explain_clause
from contract_check import looks_like_contract
st.info("🔧 Demo Mode: AI explanations are simulated to demonstrate system behavior without external APIs.")
st.set_page_config(page_title="Contract Risk Bot")
st.title("📄 Contract Analysis & Risk Assessment Bot")
st.write("Upload a contract (PDF, DOCX, or TXT) to extract text.")
uploaded_file = st.file_uploader(
    "Upload contract file",
    type=["pdf", "docx", "txt"]
)
def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        return text

    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    return ""

if uploaded_file:
    text = extract_text(uploaded_file)

    if not looks_like_contract(text):
        st.error("⚠️ This document does not appear to be a legal contract.")
        st.stop()

    clauses = split_clauses(text)

    st.subheader("📑 Extracted Clauses")
    st.write(f"Total clauses found: {len(clauses)}")
    for clause in clauses:
        risk_info = assess_risk(clause["text"])

        risk_color = {
            "High": "🔴",
            "Medium": "🟠",
            "Low": "🟢"
        }

        with st.expander(f'{risk_color[risk_info["risk"]]} {clause["clause_id"]} — Risk: {risk_info["risk"]}'):
            st.write("**Reason:**", risk_info["reason"])
            st.write(clause["text"])

            if risk_info["risk"] in ["High", "Medium"]:
                if st.button(f"Explain Risk for {clause['clause_id']}"):
                    explanation = explain_clause(
                        clause["text"],
                        risk_info["risk"],
                        risk_info["reason"]
                    )
                    st.markdown(explanation)



