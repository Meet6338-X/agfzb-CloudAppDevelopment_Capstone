"""Load the car makes and the car models of the Cloudant store into the database."""
import json
import os
from datetime import datetime

from django.core.management.base import BaseCommand

from djangoapp.models import CarMake, CarModel

# The car makes are shipped with the application. They are looked up in the
# `data` folder of the server and in the `cloudant/data` folder of the
# repository, so that the very same command works in the container image and
# in a development checkout.
CANDIDATE_FILES = [
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))),
        "cloudant", "data", "carmakes.json"),
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))),
        "data", "carmakes.json"),
]

DATA_FILE = next(
    (path for path in CANDIDATE_FILES if os.path.exists(path)), CANDIDATE_FILES[0])


class Command(BaseCommand):
    """Load the car makes and car models of the document store into the database."""

    help = "Load the car makes and car models from the Cloudant document store"

    def handle(self, *args, **options):
        payload = None
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as handle:
                payload = json.load(handle)
        else:
            # The document store is not part of the container image: the car
            # makes are then read from the cloud function.
            import requests

            from djangoapp.restapis import CARMAKES_URL

            response = requests.get(CARMAKES_URL, timeout=30)
            response.raise_for_status()
            payload = {"carmakes": response.json()}

        makes = 0
        models = 0
        for make_doc in payload["carmakes"]:
            make, _ = CarMake.objects.get_or_create(
                name=make_doc["name"],
                defaults={"description": make_doc.get("description", "")})
            makes += 1
            for model_doc in make_doc["car_models"]:
                year = model_doc["year"]
                if isinstance(year, str):
                    year = datetime.strptime(year[:10], "%Y-%m-%d").date()
                CarModel.objects.update_or_create(
                    id=model_doc["id"],
                    defaults={
                        "car_make": make,
                        "dealer_id": model_doc["dealer_id"],
                        "name": model_doc["name"],
                        "model_type": model_doc["model_type"],
                        "year": year,
                    })
                models += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Loaded {makes} car makes and {models} car models"))
