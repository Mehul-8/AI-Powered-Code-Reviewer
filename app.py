from flask import Flask, render_template, request, jsonify
from review import review_code

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/review", methods=["POST"])
def api_review():
    data = request.get_json()
    code = data.get("code", "").strip()
    language = data.get("language", "python")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        result = review_code(code, language)
        return jsonify({"review": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)