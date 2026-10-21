"""URL configuration of the djangoapp application.

Two families of routes are registered:

* the HTML pages of the template application, and
* the JSON API that proxies the dealership database service and the
  sentiment analyzer service.
"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # --- static pages -----------------------------------------------------
    path(route='about', view=views.about, name="about"),
    path(route='contact', view=views.contact, name="contact"),

    # --- user management --------------------------------------------------
    path(route='login', view=views.login_request, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='register', view=views.registration_request, name='register'),
    path(route='registration', view=views.registration_request,
         name='registration'),

    # --- car makes and models --------------------------------------------
    path(route='get_cars', view=views.get_cars, name='getcars'),
    path(route='carmakes', view=views.get_cars, name='carmakes'),

    # --- dealerships ------------------------------------------------------
    path(route='get_dealers', view=views.get_dealers_json, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealers_json,
         name='get_dealers_by_state'),
    path(route='fetchDealers', view=views.get_dealers_json,
         name='fetch_dealers'),
    path(route='fetchDealers/<str:state>', view=views.get_dealers_json,
         name='fetch_dealers_by_state'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details_json,
         name='dealer_details_json'),
    path(route='fetchDealer/<int:dealer_id>', view=views.get_dealer_details_json,
         name='fetch_dealer'),

    # --- reviews ----------------------------------------------------------
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews_json,
         name='dealer_reviews'),
    path(route='fetchReviews/dealer/<int:dealer_id>',
         view=views.get_dealer_reviews_json, name='fetch_dealer_reviews'),
    path(route='add_review', view=views.add_review_json, name='add_review_json'),

    # --- sentiment analysis ------------------------------------------------
    path(route='analyze', view=views.analyze, name='analyze'),
    path(route='analyze/<path:input_txt>', view=views.analyze,
         name='analyze_text'),

    # --- html pages -------------------------------------------------------
    path(route='', view=views.get_dealerships, name='index'),
    path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details,
         name='dealer_details'),
    path(route='dealer/<int:dealer_id>/add_review/', view=views.add_review,
         name="add_review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
