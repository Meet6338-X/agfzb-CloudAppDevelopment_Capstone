"""Seed the CarMake / CarModel tables of the Django application.

The course populates the database with the car makes and models below.  The
catalogue that ships with the project (``cloudant/data/carmakes.json``) is
loaded as well so that every make of the dealership group is available.
"""
import json
import os
from datetime import date

from .models import CarMake, CarModel

CAR_MAKE_DATA = [
    {'name': 'Nissan', 'description': 'Great cars. Japanese technology'},
    {'name': 'Mercedes', 'description': 'Great cars. German technology'},
    {'name': 'Audi', 'description': 'Great cars. German technology'},
    {'name': 'Kia', 'description': 'Great cars. Korean technology'},
    {'name': 'Toyota', 'description': 'Great cars. Japanese technology'},
]

CAR_MODEL_DATA = [
    {'name': 'Pathfinder', 'model_type': 'SUV', 'year': 2023, 'make': 'Nissan'},
    {'name': 'Rogue', 'model_type': 'SUV', 'year': 2023, 'make': 'Nissan'},
    {'name': 'Ariya', 'model_type': 'SUV', 'year': 2023, 'make': 'Nissan'},
    {'name': 'C-Class', 'model_type': 'Sedan', 'year': 2023, 'make': 'Mercedes'},
    {'name': 'E-Class', 'model_type': 'Sedan', 'year': 2023, 'make': 'Mercedes'},
    {'name': 'A4', 'model_type': 'Sedan', 'year': 2023, 'make': 'Audi'},
    {'name': 'A5', 'model_type': 'Sedan', 'year': 2023, 'make': 'Audi'},
    {'name': 'Sorento', 'model_type': 'SUV', 'year': 2023, 'make': 'Kia'},
    {'name': 'Carnival', 'model_type': 'SUV', 'year': 2023, 'make': 'Kia'},
    {'name': 'Corolla', 'model_type': 'Sedan', 'year': 2023, 'make': 'Toyota'},
    {'name': 'Camry', 'model_type': 'Sedan', 'year': 2023, 'make': 'Toyota'},
    {'name': 'Kluger', 'model_type': 'SUV', 'year': 2023, 'make': 'Toyota'},
]

CATALOGUE_FILES = [
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', '..', '..', 'cloudant', 'data', 'carmakes.json'),
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', 'data', 'carmakes.json'),
]


def _load_catalogue():
    """Return the car catalogue that ships with the project."""
    for candidate in CATALOGUE_FILES:
        path = os.path.abspath(candidate)
        if os.path.isfile(path):
            with open(path, encoding='utf-8') as fh:
                catalogue = json.load(fh)
            if isinstance(catalogue, dict):
                for key in ('carmakes', 'car_makes', 'carMakes', 'data'):
                    if isinstance(catalogue.get(key), list):
                        return catalogue[key]
                return []
            if isinstance(catalogue, list):
                return catalogue
    return []


def _as_date(value):
    """Convert a year, a date or an ISO string into a ``datetime.date``."""
    if isinstance(value, date):
        return value
    text = str(value)
    if len(text) == 4 and text.isdigit():
        return date(int(text), 1, 1)
    return date.fromisoformat(text[:10])


def initiate():
    """Create the car makes and car models used by the application."""
    makes = {}
    for data in CAR_MAKE_DATA:
        make, _ = CarMake.objects.get_or_create(
            name=data['name'], defaults={'description': data['description']})
        makes[data['name']] = make

    for data in CAR_MODEL_DATA:
        make = makes[data['make']]
        CarModel.objects.get_or_create(
            car_make=make,
            name=data['name'],
            defaults={
                'model_type': data['model_type'],
                'year': _as_date(data['year']),
                'dealer_id': 1,
            })

    for make_data in _load_catalogue():
        make, _ = CarMake.objects.get_or_create(
            name=make_data['name'],
            defaults={'description': make_data.get('description', '')})
        for model_data in make_data.get('car_models', []):
            CarModel.objects.get_or_create(
                car_make=make,
                name=model_data['name'],
                defaults={
                    'model_type': model_data.get('model_type', 'Sedan'),
                    'year': _as_date(model_data.get('year', '2023')),
                    'dealer_id': model_data.get('dealer_id', 1),
                })
