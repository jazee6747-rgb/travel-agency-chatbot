from flask import Flask, request, jsonify
from flask_cors import CORS # Added for connectivity
import os

app = Flask(__name__)
CORS(app) # This allows your React frontend to talk to this backend

# The theme-specific keywords for your travel agency
travel_keywords = ["goa", "flight", "hotel", "visa", "tour", "travel", "trip", "booking"]

@app.route("/chat", methods=["POST"])
def chat():
    # Get the message from the React frontend
    data = request.json
    if not data or "message" not in data:
        return jsonify({"reply": "Invalid request"}), 400
        
    user_msg = data["message"].lower()

    # 1. Reject irrelevant questions (Assignment Requirement)
    if not any(word in user_msg for word in travel_keywords):
        return jsonify({
            "reply": "I can only assist with travel-related questions like tours, flights, or visas."
        })

    # 2. Specific Logic for Travel Theme
    if "goa" in user_msg:
        return jsonify({"reply": "Goa tour packages start from ₹12,999."})
        
    if "flight" in user_msg:
        return jsonify({"reply": "We provide affordable flight booking services."})
        
    if "hotel" in user_msg:
        return jsonify({"reply": "We can book 3-star to 5-star hotels for you."})
        
    if "visa" in user_msg:
        return jsonify({"reply": "Visa assistance is available for selected countries."})

    # Default response if it is travel-related but not a specific keyword
    return jsonify({
        "reply": "Please ask specifically about tours, flights, hotels, or visas."
    })

if __name__ == "__main__":
    # Required for deployment on platforms like Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
