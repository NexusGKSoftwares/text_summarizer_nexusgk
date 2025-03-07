from flask import Flask, request, jsonify
from main.summarizer import extractive_summary, abstractive_summary

app = Flask(__name__)

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")
    method = data.get("method", "abstractive")  # Default to abstractive

    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = (
        abstractive_summary(text) if method == "abstractive"
        else extractive_summary(text)
    )
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
