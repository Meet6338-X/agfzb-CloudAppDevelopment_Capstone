"""Django models of the Best Cars Dealership application."""
from django.db import models


# Create your models here.

class CarMake(models.Model):
    """A car manufacturer sold by the Best Cars Dealership network."""

    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=True, max_length=500)

    def __str__(self):
        return str(self.name)


class CarModel(models.Model):
    """A car model. Each model belongs to a CarMake and to a dealership."""

    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=255)

    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "WAGON"
    TYPE_CHOICES = (
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    )

    model_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()

    def __str__(self):
        return f"{self.car_make} {self.name} ({self.year})".strip()


class CarDealer:
    """Plain Python class holding the data of a dealership document.

    All the fields come from the `dealerships` document of the Cloudant
    `dealerships` database.
    """

    def __init__(self, id, city, state, st, address, zip, lat, long, short_name, full_name):
        # Dealer id
        self.id = id
        # Dealer city
        self.city = city
        # Dealer state
        self.state = state
        # Dealer state abbreviation
        self.st = st
        # Dealer address
        self.address = address
        # Dealer zip
        self.zip = zip
        # Location latitude
        self.lat = lat
        # Location longitude
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer full name
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name


class DealerReview:
    """Plain Python class holding the data of a review document.

    All the fields come from the `reviews` document of the Cloudant
    `reviews` database.
    """

    def __init__(self, id, name, dealership, review, purchase, purchase_date,
                 car_make, car_model, car_year, sentiment="neutral"):
        self.id = id
        self.name = name  # reviewer name
        self.dealership = dealership
        self.review = review  # review text
        self.purchase = purchase  # did the reviewer purchase the car?
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment  # sentiment analysis of the review text

    def __str__(self):
        return 'Reviewer: ' + str(self.name) + ' Review: ' + str(self.review)
