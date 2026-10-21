"""Django views for the Best Cars Dealership capstone application.

The application exposes two flavours of endpoint:

* the HTML pages of the Django template application (home page, dealer
  details, review form, about and contact pages), and
* a JSON API that the React front end and the cURL based review exercises
  use.  The JSON API mirrors the endpoints of the backend services
  (``/fetchDealers``, ``/fetchDealer/<id>``, ``/fetchReviews/dealer/<id>``)
  and of the user management endpoints (``/login``, ``/logout``,
  ``/register``).
"""
import json
import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, CarModel
from .populate import initiate
from .restapis import (analyze_review_sentiments, get_request, post_review)

logger = logging.getLogger(__name__)


def _wants_json(request):
    """Return True when the caller expects a JSON answer.

    A browser navigating to the application sends ``Accept: text/html`` and
    therefore gets the HTML pages.  Every other client (curl, the React
    front end, the automated review exercises) receives JSON.
    """
    accept = request.headers.get('Accept', '')
    if 'application/json' in accept:
        return True
    if request.content_type == 'application/json':
        return True
    if 'text/html' in accept:
        return False
    return True


def _json_body(request):
    """Return the decoded JSON body of a request."""
    if not request.body:
        return {}
    try:
        return json.loads(request.body)
    except (ValueError, TypeError):
        return {}


# Create an `about` view to render a static about page
def about(request):
    """Render the static 'About Us' page."""
    context = {}
    return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    """Render the static 'Contact Us' page."""
    context = {}
    return render(request, 'djangoapp/contact.html', context)


# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_request(request):
    """Log a user in.

    The JSON flavour of the endpoint accepts ``{"userName": ...,
    "password": ...}`` and answers with the name of the authenticated user,
    the HTML flavour is used by the login form of the navigation bar.
    """
    context = {}
    if _wants_json(request):
        data = _json_body(request)
        username = data.get('userName', '')
        password = data.get('password', '')
        user = authenticate(request, username=username, password=password)
        res_data = {"userName": username}
        if user is not None:
            login(request, user)
            res_data = {
                "userName": username,
                "status": "Authenticated",
                "firstname": user.first_name,
                "lastname": user.last_name,
            }
        return JsonResponse(res_data)

    if request.method == "POST":
        username = request.POST['username']
        psw = request.POST['psw']
        user = authenticate(request, username=username, password=psw)
        if user is not None:
            login(request, user)
            return redirect("djangoapp:index")
        print(f"Failed login for user {username}")
        messages.error(request, "Invalid username or password.")
        return redirect("djangoapp:index")
    return render(request, 'djangoapp/registration.html', context)


# The name used by the course material for the login view
login_user = login_request


# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_request(request):
    """Log the current user out and return to the home page."""
    print(f"Log out the user `{request.user.username}`")
    logout(request)
    if _wants_json(request):
        return JsonResponse({"userName": ""})
    messages.success(request, "You have been logged out successfully.")
    return redirect("djangoapp:index")


# Create a `registration_request` view to handle sign up request
@csrf_exempt
def registration_request(request):
    """Create a new user account and log the new user in."""
    context = {}
    if _wants_json(request) and request.method == "POST":
        data = _json_body(request)
        username = data.get('userName', '')
        password = data.get('password', '')
        firstname = data.get('firstName', '')
        lastname = data.get('lastName', '')
        email = data.get('email', '')
        if User.objects.filter(username=username).exists():
            return JsonResponse({"userName": username,
                                 "error": "Already Registered"})
        User.objects.create_user(username=username, password=password,
                                  first_name=firstname, last_name=lastname,
                                  email=email)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated",
                             "firstname": firstname, "lastname": lastname})

    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        psw = request.POST['psw']
        email = request.POST.get('email', '')
        if User.objects.filter(username=username).exists():
            messages.error(request, "That username is already taken.")
            return redirect("djangoapp:registration")
        user = User.objects.create_user(username=username, password=psw,
                                        first_name=firstname, last_name=lastname,
                                        email=email)
        user.save()
        login(request, user)
        return redirect("djangoapp:index")
    return render(request, 'djangoapp/registration.html', context)


# The name used by the course material for the registration view
registration = registration_request


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    """Render the home page with the list of dealerships.

    The list can be narrowed down to a single state by adding the `state`
    query parameter, e.g. /djangoapp/?state=Kansas
    """
    context = {}
    if request.method == "GET":
        state = request.GET.get('state')
        if state:
            dealerships = get_request(f"/fetchDealers/{state}")
        else:
            dealerships = get_request("/fetchDealers")
        context["dealership_list"] = dealerships if dealerships else []
        context["selected_state"] = state
        return render(request, 'djangoapp/index.html', context)
    return HttpResponse(status=405)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    """Render the page of one dealership together with its reviews."""
    context = {}
    if request.method == "GET":
        reviews = get_request(f"/fetchReviews/dealer/{dealer_id}") or []
        for review in reviews:
            review['sentiment'] = analyze_review_sentiments(
                review.get('review', '')).get('sentiment', 'neutral')
        dealers = get_request(f"/fetchDealer/{dealer_id}") or []
        context["reviews"] = reviews
        context["dealer_id"] = dealer_id
        context["dealer"] = dealers[0] if dealers else None
        return render(request, 'djangoapp/dealer_details.html', context)
    return HttpResponse(status=405)


# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request, dealer_id):
    """Show the review form of a dealership and store a submitted review."""
    context = {}
    dealers = get_request(f"/fetchDealer/{dealer_id}") or []
    if not dealers:
        messages.error(request, "The dealership could not be found.")
        return redirect("djangoapp:index")
    dealer = dealers[0]

    if request.method == "GET":
        context["cars"] = CarModel.objects.all()
        context["dealer"] = dealer
        return render(request, 'djangoapp/add_review.html', context)

    if request.method == "POST":
        review = {}
        review["id"] = request.POST["id"]
        review["name"] = request.POST["name"]
        review["dealership"] = dealer_id
        review["review"] = request.POST["review"]
        review["purchase"] = request.POST.get("purchase")
        review["purchase_date"] = request.POST.get("purchase_date")
        # The car select box carries the primary key of the purchased car model
        car = get_object_or_404(CarModel, pk=request.POST.get("car"))
        review["car_make"] = car.car_make.name
        review["car_model"] = car.name
        review["car_year"] = car.year.year

        response = post_review({"review": review})
        if response and response.get("status") in (200, 201):
            print(f"Review posted successfully for dealer {dealer_id}")
        else:
            messages.error(request, "The review could not be saved.")
        return redirect("djangoapp:dealer_details", dealer_id=dealer_id)
    return HttpResponse(status=405)


# A JSON endpoint that returns every car make together with its car models
def get_cars(request):  # pylint: disable=unused-argument
    """Return all the car makes and models as a JSON document."""
    count = CarMake.objects.filter().count()
    if count == 0:
        initiate()
    cars = [
        {
            "CarModel": model.name,
            "CarMake": model.car_make.name,
        }
        for model in CarModel.objects.select_related('car_make')
    ]
    return JsonResponse({"status": 200, "CarModels": cars})


# A JSON endpoint that returns every dealership
def get_dealers_json(request, state="All"):
    """Return every dealership, optionally filtered on the state."""
    if state in (None, "", "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200,
                         "dealers": dealerships if dealerships is not None else []})


# A JSON endpoint that returns one dealership
def get_dealer_details_json(request, dealer_id):
    """Return the details of one dealership."""
    endpoint = f"/fetchDealer/{dealer_id}"
    dealer = get_request(endpoint)
    return JsonResponse({"status": 200, "dealer": dealer if dealer is not None else []})


# A JSON endpoint that returns the reviews of one dealership
def get_dealer_reviews_json(request, dealer_id):
    """Return the reviews of one dealership together with their sentiment."""
    endpoint = f"/fetchReviews/dealer/{dealer_id}"
    reviews = get_request(endpoint) or []
    for review in reviews:
        review['sentiment'] = analyze_review_sentiments(
            review.get('review', '')).get('sentiment', 'neutral')
    return JsonResponse({"status": 200, "reviews": reviews})


# A JSON endpoint that stores a new review
@csrf_exempt
def add_review_json(request):
    """Store a new review that is sent as a JSON document."""
    if request.method != "POST":
        return JsonResponse({"status": 400, "error": "Bad Request"}, status=400)
    data = _json_body(request)
    review = data.get('review', data)
    post_review({"review": review})
    return JsonResponse({"status": 200})


# A JSON endpoint that returns the sentiment of a review text
def analyze(request):
    """Return the sentiment label of the review text passed in the query."""
    text = request.GET.get("text", "")
    sentiment = analyze_review_sentiments(text).get("sentiment", "neutral")
    return JsonResponse({"text": text, "sentiment": sentiment})
