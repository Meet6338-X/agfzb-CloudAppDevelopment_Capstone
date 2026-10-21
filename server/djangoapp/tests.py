"""Tests of the djangoapp application."""
from django.test import TestCase

from .models import CarMake, CarModel


class CarMakeTest(TestCase):
    """Verify the behaviour of the car make model."""

    def test_create_car_make(self):
        """A car make can be created and is rendered with its name."""
        make = CarMake.objects.create(name="Audi", description="A German make")
        self.assertEqual(str(make), "Audi")
        self.assertEqual(make.description, "A German make")

    def test_create_car_model(self):
        """A car model belongs to a car make and is rendered with it."""
        make = CarMake.objects.create(name="Audi", description="A German make")
        model = CarModel.objects.create(
            car_make=make, dealer_id=8, name="A6",
            model_type=CarModel.SEDAN, year="2010-01-01")
        self.assertEqual(model.car_make, make)
        self.assertIn("A6", str(model))
