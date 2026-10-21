"""Generate the `carmakes` document collection of the Cloudant store."""
import json
import os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)))
DEALERS = os.path.join(BASE, "cloudant", "data", "dealerships.json")
OUT = os.path.join(BASE, "cloudant", "data", "carmakes.json")

MAKES = [
    ("Audi", "German engineering with a focus on comfort and technology.", [
        ("A6", "Sedan", 2010), ("A4", "Sedan", 2018), ("Q5", "SUV", 2019),
        ("Q7", "SUV", 2021)]),
    ("BMW", "The ultimate driving machine, built for the German road.", [
        ("3 Series", "Sedan", 2015), ("X3", "SUV", 2019), ("X5", "SUV", 2020),
        ("M3", "Sedan", 2016)]),
    ("Chevrolet", "American value with a dealership network in every state.", [
        ("Silverado 1500", "WAGON", 2017), ("Equinox", "SUV", 2020),
        ("Malibu", "Sedan", 2018), ("Tahoe", "SUV", 2021)]),
    ("Ford", "The truck brand that built America.", [
        ("F-150", "WAGON", 2016), ("Escape", "SUV", 2019),
        ("Explorer", "SUV", 2020), ("Mustang", "Sedan", 2015)]),
    ("Honda", "Reliable, efficient and built for everyday driving.", [
        ("Civic", "Sedan", 2019), ("Accord", "Sedan", 2018),
        ("CR-V", "SUV", 2020), ("Pilot", "SUV", 2021)]),
    ("Jeep", "Capable off roaders for every adventure.", [
        ("Wrangler", "SUV", 2020), ("Grand Cherokee", "SUV", 2019),
        ("Cherokee", "SUV", 2018), ("Compass", "SUV", 2021)]),
    ("Nissan", "Japanese value with a strong crossover line up.", [
        ("Altima", "Sedan", 2019), ("Sentra", "Sedan", 2020),
        ("Rogue", "SUV", 2019), ("Pathfinder", "SUV", 2021)]),
    ("Toyota", "The benchmark of reliability and resale value.", [
        ("Camry", "Sedan", 2019), ("Corolla", "Sedan", 2020),
        ("RAV4", "SUV", 2019), ("Highlander", "SUV", 2020)]),
    ("Volkswagen", "German engineering with a practical footprint.", [
        ("Jetta", "Sedan", 2018), ("Passat", "Sedan", 2017),
        ("Tiguan", "SUV", 2020), ("Atlas", "SUV", 2019)]),
    ("Tesla", "Electric mobility with over the air updates.", [
        ("Model 3", "Sedan", 2021), ("Model S", "Sedan", 2020),
        ("Model Y", "SUV", 2021), ("Model X", "SUV", 2020)]),
]

with open(DEALERS, "r", encoding="utf-8") as handle:
    dealers = json.load(handle)["dealerships"]

car_makes = []
model_id = 1
for index, (name, description, models) in enumerate(MAKES, start=1):
    car_models = []
    for model_name, model_type, year in models:
        dealer = dealers[(model_id - 1) % len(dealers)]
        car_models.append({
            "id": model_id,
            "name": model_name,
            "dealer_id": dealer["id"],
            "model_type": model_type,
            "year": f"{year}-01-01T00:00:00.000Z",
        })
        model_id += 1
    car_makes.append({
        "id": index,
        "name": name,
        "description": description,
        "car_models": car_models,
    })

with open(OUT, "w", encoding="utf-8") as handle:
    json.dump({"carmakes": car_makes}, handle, indent=2)

print(f"wrote {OUT} with {len(car_makes)} car makes and {model_id - 1} car models")
