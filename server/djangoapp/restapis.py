"""HTTP client of the cloud functions that hold the dealership data."""
import json
import os

import requests
from requests.auth import HTTPBasicAuth

from .models import CarDealer, DealerReview

# Base URLs of the cloud functions that expose the dealerships, the reviews,
# the car makes and the sentiment analysis. They can be overridden with
# environment variables so that the very same code runs against the IBM Cloud
# Functions and against the local (offline) function server.
DEALERS_URL = os.environ.get(
    "DEALERS_URL", "http://localhost:3000/dealerships/get")
REVIEWS_URL = os.environ.get(
    "REVIEWS_URL", "http://localhost:5000/api/get_reviews")
POST_REVIEW_URL = os.environ.get(
    "POST_REVIEW_URL", "http://localhost:5000/api/post_review")
CARMAKES_URL = os.environ.get(
    "CARMAKES_URL", "http://localhost:3000/carmakes/get")
SENTIMENT_URL = os.environ.get(
    "SENTIMENT_URL", "http://localhost:5000/api/analyze")

# Credentials of the Watson Natural Language Understanding service that is
# used for the sentiment analysis of a review. When the service is not
# reachable the local sentiment analyser is used instead.
NLU_CREDENTIALS = {
    "apikey": os.environ.get("NLU_API_KEY", ""),
    "url": os.environ.get(
        "NLU_URL",
        "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com"
        "/instances/00000000-0000-0000-0000-000000000000"),
}


# Create a `get_request` to make HTTP GET requests
def get_request(url, **kwargs):
    """Perform an HTTP GET request and return the decoded JSON body."""
    print(f"GET from {url} ")
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                params=kwargs, timeout=30)
    except requests.exceptions.RequestException:
        print("Network exception occurred")
        return None
    print(f"With status {response.status_code} ")
    if response.status_code != 200:
        print(f"Unexpected response body: {response.text}")
        return None
    try:
        return json.loads(response.text)
    except ValueError:
        print("Unable to decode the JSON response")
        return None


# Create a `post_request` to make HTTP POST requests
def post_request(url, json_payload, **kwargs):
    """Perform an HTTP POST request and return the response object."""
    print(f"POST to {url}")
    try:
        response = requests.post(url, params=kwargs, json=json_payload, timeout=30)
    except requests.exceptions.RequestException:
        print("An error occurred while making POST request. ")
        return None
    print(f"With status {response.status_code}")
    return response


# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealers_from_cf(url, **kwargs):
    """Get every dealership from the cloud function and parse them."""
    results = []
    json_result = get_request(url, **kwargs)
    if json_result:
        print(f"JSON RESULT: {len(json_result)} dealership document(s) retrieved")
        for dealer_doc in json_result:
            dealer_obj = CarDealer(
                id=dealer_doc["id"], city=dealer_doc["city"],
                state=dealer_doc["state"], st=dealer_doc["st"],
                address=dealer_doc["address"], zip=dealer_doc["zip"],
                lat=dealer_doc["lat"], long=dealer_doc["long"],
                short_name=dealer_doc["short_name"],
                full_name=dealer_doc["full_name"])
            results.append(dealer_obj)
    return results


# Create a get_dealer_by_id_from_cf method to get a single dealer
def get_dealer_by_id_from_cf(url, dealer_id):
    """Get one dealership from the cloud function, selected by its id."""
    results = [{}]
    url_with_id = f"{url}?id={dealer_id}"
    json_result = get_request(url_with_id)
    if not json_result:
        return results
    for dealer_doc in json_result:
        dealer_obj = CarDealer(
            id=dealer_doc["id"], city=dealer_doc["city"],
            state=dealer_doc["state"], st=dealer_doc["st"],
            address=dealer_doc["address"], zip=dealer_doc["zip"],
            lat=dealer_doc["lat"], long=dealer_doc["long"],
            short_name=dealer_doc["short_name"],
            full_name=dealer_doc["full_name"])
        results.append(dealer_obj)
    return results


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id
def get_dealer_reviews_from_cf(url, **kwargs):
    """Get every review of a dealership and analyse its sentiment."""
    results = []
    json_result = get_request(url, **kwargs)
    if json_result:
        for single_review in json_result:
            dealer_review = DealerReview(
                id=single_review["id"],
                name=single_review["name"],
                dealership=single_review["dealership"],
                review=single_review["review"],
                purchase=single_review.get("purchase"),
                purchase_date=single_review.get("purchase_date"),
                car_make=single_review.get("car_make"),
                car_model=single_review.get("car_model"),
                car_year=single_review.get("car_year"),
                sentiment="",
            )
            dealer_review.sentiment = analyze_review_sentiments(dealer_review.review)
            results.append(dealer_review)
            print("DEALER REVIEW:", dealer_review)
    return results


# Create a get_car_makes_from_cf method to get all the car makes and models
def get_car_makes_from_cf(url, **kwargs):
    """Get every car make together with its car models."""
    return get_request(url, **kwargs) or []


# Create an `analyze_review_sentiments` method to analyse the sentiment of a
# review text with the Watson Natural Language Understanding service.
def analyze_review_sentiments(dealerreview):
    """Return the sentiment label (positive / neutral / negative) of a text."""
    body = {"text": dealerreview, "features": {"sentiment": {"document": True}}}
    if NLU_CREDENTIALS["apikey"]:
        try:
            response = requests.post(
                NLU_CREDENTIALS["url"] + "/v1/analyze?version=2019-07-12",
                headers={"Content-Type": "application/json"},
                json=body,
                auth=HTTPBasicAuth("apikey", NLU_CREDENTIALS["apikey"]),
                timeout=15,
            )
            if response.status_code == 200:
                return response.json()["sentiment"]["document"]["label"]
        except requests.exceptions.RequestException:
            print("The Watson NLU service is not reachable, using the local analyser")
    else:
        print("No Watson NLU credentials, using the local sentiment analyser")

    # The NLU service is not available: use the local sentiment analyser that
    # is exposed by the sentiment cloud function.
    json_result = get_request(SENTIMENT_URL, text=dealerreview)
    if json_result:
        return json_result.get("sentiment", "neutral")
    return "neutral"
