from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Travel-related keywords
travel_keywords = [
    "travel", "trip", "tour", "package",
    "flight", "hotel", "visa", "booking",
    "destination", "price", "cost"
]

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"].lower()

    # Reject irrelevant questions
    if not any(word in user_msg for word in travel_keywords):
        return jsonify({
            "reply": "I can only assist with travel-related questions."
        })

    if "goa" in user_msg:
        return jsonify({
            "reply": "Goa tour packages start from ₹12,999."
        })

    if "flight" in user_msg:
        return jsonify({
            "reply": "We provide affordable flight booking services."
        })

    if "hotel" in user_msg:
        return jsonify({
            "reply": "We can book 3-star to 5-star hotels for you."
        })

    if "visa" in user_msg:
        return jsonify({
            "reply": "Visa assistance is available for selected countries."
        })

    return jsonify({
        "reply": "Please ask about tours, flights, hotels, or visas."
    })

if __name__ == "__main__":
    app.run(debug=True)
