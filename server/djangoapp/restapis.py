"""REST helpers used by the Django application.

The Django layer is a thin proxy in front of two backend services:

* the dealership database service  (``backend_url``)      - port 3030
* the sentiment analyzer service  (``sentiment_analyzer_url``) - port 5050

Both URLs can be overridden with environment variables, see ``.env``.
"""
import os

import requests

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url', default="http://localhost:5050/")

# The legacy cloud function endpoints are still supported so that the
# application keeps working when the services are started from the
# ``functions`` folder instead of ``server/database``.
dealers_url = os.getenv(
    'DEALERS_URL', default=backend_url + "/fetchDealers")
reviews_url = os.getenv(
    'REVIEWS_URL', default=backend_url + "/fetchReviews/dealer/")
post_review_url = os.getenv(
    'POST_REVIEW_URL', default=backend_url + "/insert_review")
carmakes_url = os.getenv(
    'CARMAKES_URL', default=backend_url + "/fetchDealers")


def get_request(endpoint, **kwargs):
    """Perform a GET request against the backend service."""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"

    request_url = backend_url + endpoint
    if params:
        request_url = request_url + "?" + params

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url, timeout=30)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None


def post_request(url, json_payload, **kwargs):
    """Perform a POST request carrying a JSON payload."""
    print(f"POST to {url}")
    try:
        response = requests.post(url, json=json_payload, timeout=30)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """Ask the sentiment analyzer service to score a piece of text."""
    request_url = sentiment_analyzer_url + "analyze/" + str(text)
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url, timeout=30)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    """Store a new review in the dealership database service."""
    request_url = backend_url + "/insert_review"
    print(f"POST to {request_url}")
    try:
        response = requests.post(request_url, json=data_dict, timeout=30)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None


def get_dealers_from_cf(url, **kwargs):
    """Return the list of dealers as plain dictionaries."""
    dealers = get_request(url) if url.startswith('/') else _get(url)
    if dealers is None:
        return []
    return dealers


def get_dealer_by_id_from_cf(url, dealer_id):
    """Return the dealer with the given id as a plain dictionary."""
    dealers = _get(f"{url}?id={dealer_id}")
    if not dealers:
        return {}
    return dealers[0]


def get_dealer_reviews_from_cf(url, **kwargs):
    """Return the reviews of a dealer, enriched with their sentiment."""
    reviews = _get(url)
    if not reviews:
        return []
    for review in reviews:
        review['sentiment'] = analyze_review_sentiments(
            review.get('review', '')).get('sentiment', 'neutral')
    return reviews


def get_car_makes_from_cf(url, **kwargs):
    """Return every car make together with its models."""
    return _get(url)


def _get(url):
    """GET an absolute url and return the decoded JSON body."""
    print(f"GET from {url}")
    try:
        response = requests.get(url, timeout=30)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None
