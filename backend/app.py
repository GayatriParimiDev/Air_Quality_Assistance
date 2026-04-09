# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import handle_message
from database import find_best_city, get_city_aqi, top_n_polluted

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "AQI Chatbot API running"})

@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.json or {}
    message = payload.get("message", "")
    reply = handle_message(message)
    return jsonify({"reply": reply})

@app.route("/api/city", methods=["GET"])
def city_lookup():
    name = request.args.get("name", "")
    if not name:
        return jsonify({"error": "Provide ?name=<city>"}), 400
    best, score = find_best_city(name)
    if not best:
        return jsonify({"error": f"No match for {name}"}), 404
    data = get_city_aqi(best)
    return jsonify({"matched_name": best, "score": score, "data": data})

@app.route("/api/top", methods=["GET"])
def top():
    n = int(request.args.get("n", 10))
    return jsonify(top_n_polluted(n))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
