"""Generate the JSON documents used by the dealership database service.

The documents are the Cloudant export that ships with the project.  A MongoDB
style ``_id`` is added to every document so that the responses look exactly
like the ones produced by the MongoDB backed service.
"""
import hashlib
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
CLOUDANT = os.path.join(ROOT, "cloudant", "data")
TARGET = os.path.join(ROOT, "server", "database", "data")


def mongo_id(seed):
    """Return a deterministic 24 character hexadecimal id."""
    return hashlib.sha1(seed.encode("utf-8")).hexdigest()[:24]


def main():
    os.makedirs(TARGET, exist_ok=True)

    with open(os.path.join(CLOUDANT, "dealerships.json"), encoding="utf-8") as fh:
        dealers = json.load(fh)["dealerships"]
    with open(os.path.join(CLOUDANT, "reviews.json"), encoding="utf-8") as fh:
        reviews = json.load(fh)["reviews"]

    for doc in dealers:
        doc["_id"] = mongo_id(f"dealer-{doc['id']}")
    for doc in reviews:
        doc["_id"] = mongo_id(f"review-{doc.get('id')}")

    with open(os.path.join(TARGET, "dealerships.json"), "w", encoding="utf-8") as fh:
        json.dump({"dealerships": dealers}, fh, indent=2)
    with open(os.path.join(TARGET, "reviews.json"), "w", encoding="utf-8") as fh:
        json.dump({"reviews": reviews}, fh, indent=2)

    print(f"wrote {len(dealers)} dealerships and {len(reviews)} reviews to {TARGET}")


if __name__ == "__main__":
    main()
