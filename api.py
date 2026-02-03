from flask import Flask, request, jsonify
from contract_check import analyze_contract
import os

app = Flask(__name__)

@app.route("/analyze-contract", methods=["POST"])
def analyze():
    data = request.json
    contract_text = data.get("text")

    if not contract_text:
        return jsonify({"error": "No contract text"}), 400

    result = analyze_contract(contract_text)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

