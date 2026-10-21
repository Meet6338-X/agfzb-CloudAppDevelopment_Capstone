"""Load the car makes and the car models of the document store into the database."""
import os

from django.core.management.base import BaseCommand

from djangoapp.models import CarMake, CarModel
from djangoapp.populate import initiate


class Command(BaseCommand):
    """Load the car makes and car models into the database."""

    help = "Load the car makes and the car models from the document store"

    def handle(self, *args, **options):
        # The course car catalogue plus the catalogue that ships with the
        # project (`cloudant/data/carmakes.json`).
        initiate()

        makes = CarMake.objects.count()
        models = CarModel.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loaded {makes} car makes and {models} car models"))
