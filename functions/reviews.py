"""Cloud function that manages the dealership reviews.

The function exposes three endpoints:

    GET  /api/get_reviews?id=<dealer_id>  -> the reviews of one dealership
    POST /api/post_review                 -> stores a new review
    GET  /api/analyze?text=<review text>  -> the sentiment of a review text
"""
import os
import re

import requests
from flask import Flask, jsonify, request
from requests.auth import HTTPBasicAuth

import localstore

app = Flask(__name__)

REVIEWS_DB = "reviews"
REVIEWS_FILE = "reviews.json"
REVIEWS_COLLECTION = "reviews"


@app.route("/api/get_reviews", methods=["GET"])
def get_reviews():
    """Return every review of the dealership passed in the `id` query string."""
    dealer_id = request.args.get("id")
    if dealer_id is None:
        return jsonify({"error": "Dealer id is required"}), 400
    try:
        dealer_id = int(dealer_id)
    except (TypeError, ValueError):
        return jsonify({"error": "Dealer id has to be an integer"}), 400

    documents = localstore.get_documents(REVIEWS_DB, REVIEWS_FILE)
    reviews = [doc for doc in documents if int(doc.get("dealership", -1)) == dealer_id]
    return jsonify(reviews)


@app.route("/api/post_review", methods=["POST"])
def post_review():
    """Store a new review of a dealership."""
    payload = request.get_json(silent=True) or {}
    review = payload.get("review")
    if not review:
        return jsonify({"error": "No review was sent"}), 400

    required = ("id", "name", "dealership", "review", "purchase",
                "purchase_date", "car_make", "car_model", "car_year")
    for field in required:
        if field not in review:
            return jsonify({"error": f"The field '{field}' is required"}), 400

    localstore.add_document(REVIEWS_DB, REVIEWS_FILE, REVIEWS_COLLECTION, review)
    return jsonify({"message": "Review posted successfully"}), 201


@app.route("/api/analyze", methods=["GET", "POST"])
def analyze():
    """Return the sentiment label of the review text that is sent in."""
    text = request.args.get("text")
    if text is None and request.is_json:
        text = (request.get_json() or {}).get("text")
    if not text:
        return jsonify({"error": "No text was sent"}), 400
    return jsonify({"text": text, "sentiment": analyze_sentiment(text)})


POSITIVE_WORDS = {
    "fantastic", "great", "excellent", "amazing", "awesome", "perfect",
    "wonderful", "superb", "outstanding", "brilliant", "good", "love",
    "friendly", "helpful", "professional", "smooth", "recommend",
}
NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "horrible", "poor", "worst", "rude",
    "disappointing", "slow", "dirty", "broken", "never", "unfriendly",
}


def analyze_sentiment(text):
    """Return the sentiment of a review text.

    The Watson Natural Language Understanding service is used when its
    credentials are available.  Otherwise the review text is analysed with a
    local lexicon of positive and negative words.
    """
    nlu_url = os.environ.get("NLU_URL", "")
    nlu_key = os.environ.get("NLU_API_KEY", "")
    if nlu_url and nlu_key:
        try:
            response = requests.post(
                nlu_url + "/v1/analyze?version=2019-07-12",
                headers={"Content-Type": "application/json"},
                json={"text": text, "features": {"sentiment": {"document": True}}},
                auth=HTTPBasicAuth("apikey", nlu_key),
                timeout=10,
            )
            if response.status_code == 200:
                return response.json()["sentiment"]["document"]["label"]
        except Exception:  # pylint: disable=broad-except
            print("The Watson NLU service is not reachable, using the local analyser")

    words = set(re.findall(r"[a-z']+", text.lower()))
    score = len(words & POSITIVE_WORDS) - len(words & NEGATIVE_WORDS)
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    return "neutral"


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT, debug=False)
