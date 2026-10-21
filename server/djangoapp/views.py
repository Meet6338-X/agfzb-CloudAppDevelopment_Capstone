"""Django views for the Best Cars Dealership capstone application."""
import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import CarModel
from .restapis import (CARMAKES_URL, DEALERS_URL, POST_REVIEW_URL, REVIEWS_URL,
                        analyze_review_sentiments, get_car_makes_from_cf,
                        get_dealer_by_id_from_cf, get_dealer_reviews_from_cf,
                        get_dealers_from_cf, post_request)

logger = logging.getLogger(__name__)


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
def login_request(request):
    """Log a user in with the username / password sent by the login form."""
    context = {}
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


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    """Log the current user out and return to the home page."""
    print(f"Log out the user `{request.user.username}`")
    logout(request)
    return redirect("djangoapp:index")


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    """Create a new user account and log the new user in."""
    context = {}
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


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    """Render the home page with the list of dealerships.

    The list can be narrowed down to a single state by adding the `state`
    query parameter, e.g. /djangoapp/?state=Kansas
    """
    context = {}
    if request.method == "GET":
        state = request.GET.get('state')
        dealerships = get_dealers_from_cf(DEALERS_URL, state=state) if state \
            else get_dealers_from_cf(DEALERS_URL)
        context["dealership_list"] = dealerships
        context["selected_state"] = state
        return render(request, 'djangoapp/index.html', context)
    return HttpResponse(status=405)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    """Render the page of one dealership together with its reviews."""
    context = {}
    if request.method == "GET":
        url = reviews_url_with_id(dealer_id)
        reviews = get_dealer_reviews_from_cf(url)
        dealer = get_dealer_by_id_from_cf(DEALERS_URL, dealer_id)
        context["reviews"] = reviews
        context["dealer_id"] = dealer_id
        context["dealer"] = dealer[1] if len(dealer) > 1 else None
        return render(request, 'djangoapp/dealer_details.html', context)
    return HttpResponse(status=405)


# Create a `add_review` view to submit a review
@csrf_exempt
def add_review(request, dealer_id):
    """Show the review form of a dealership and store a submitted review."""
    context = {}
    dealer = get_dealer_by_id_from_cf(DEALERS_URL, dealer_id)
    if len(dealer) < 2:
        messages.error(request, "The dealership could not be found.")
        return redirect("djangoapp:index")
    dealer = dealer[1]

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

        response = post_request(POST_REVIEW_URL, json_payload={"review": review})
        if response is not None and response.status_code in (200, 201):
            print(f"Review posted successfully for dealer {dealer_id}")
        else:
            messages.error(request, "The review could not be saved.")
        return redirect("djangoapp:dealer_details", dealer_id=dealer_id)
    return HttpResponse(status=405)


# The URL of the reviews of one dealership
def reviews_url_with_id(dealer_id):
    """Build the URL of the cloud function that returns the reviews."""
    return f"{REVIEWS_URL}?id={dealer_id}"


# A JSON endpoint that returns every car make together with its car models
def get_carmakes(request):  # pylint: disable=unused-argument
    """Return all the car makes and car models as a JSON document."""
    car_makes = get_car_makes_from_cf(CARMAKES_URL)
    if not car_makes:
        # Fall back on the local database when the cloud function is down
        car_makes = [
            {
                "id": make.id,
                "name": make.name,
                "description": make.description,
                "car_models": [
                    {"id": car.id, "name": car.name, "dealer_id": car.dealer_id,
                     "model_type": car.model_type, "year": car.year.year}
                    for car in CarModel.objects.filter(car_make=make)
                ],
            }
            for make in CarModel.objects.select_related('car_make')
            .values_list('car_make', flat=True).distinct()
        ]
    return JsonResponse({"car_makes": car_makes}, safe=False)


# A JSON endpoint that returns the sentiment of a review text
def analyze(request):
    """Return the sentiment label of the review text passed in the query."""
    text = request.GET.get("text", "")
    sentiment = analyze_review_sentiments(text)
    return JsonResponse({"text": text, "sentiment": sentiment}, safe=False)
