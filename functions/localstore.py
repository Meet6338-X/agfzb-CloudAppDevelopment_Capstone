"""Local document store used by the cloud functions.

When the IBM Cloudant service is configured (the `CLOUDANT_URL` and
`CLOUDANT_APIKEY` environment variables are set) the documents are read
from and written to Cloudant.  Without those credentials the very same
documents are kept in the JSON files of the `cloudant/data` folder, which
makes it possible to run the complete application offline.
"""
import json
import os

try:
    from ibm_cloudant import Cloudant
except ImportError:  # the offline document store is used when Cloudant is absent
    Cloudant = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "cloudant", "data")

CLOUDANT_URL = os.environ.get("CLOUDANT_URL", "")
CLOUDANT_APIKEY = os.environ.get("CLOUDANT_APIKEY", "")


def _path(filename):
    """Return the path of a document file of the local store."""
    return os.path.join(DATA_DIR, filename)


def _read(filename):
    """Read a document file of the local store."""
    with open(_path(filename), "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload


def _write(filename, payload):
    """Write a document file of the local store."""
    with open(_path(filename), "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def get_documents(database, filename):
    """Return every document of a database.

    `database` is the name of the Cloudant database ('dealerships',
    'reviews' or 'carmakes') and `filename` the name of the JSON file that
    holds the documents in the local store.
    """
    if CLOUDANT_URL and CLOUDANT_APIKEY and Cloudant is not None:
        client = Cloudant(
            {"apikey": CLOUDANT_APIKEY},
            url=CLOUDANT_URL,
            username="apikey",
        )
        database = client.database(database)
        documents = []
        for doc in database.get_all_docs(include_docs=True).get_result()["rows"]:
            documents.append(doc["doc"])
        return documents

    store_file = _path(filename)
    if not os.path.exists(store_file):
        payload = _read(filename)
        _write(filename, payload)
    payload = _read(filename)
    return payload[list(payload.keys())[0]]


def add_document(database, filename, collection, document):
    """Add a document to a database and return it."""
    if CLOUDANT_URL and CLOUDANT_APIKEY and Cloudant is not None:
        client = Cloudant(
            {"apikey": CLOUDANT_APIKEY},
            url=CLOUDANT_URL,
            username="apikey",
        )
        client.database(database).create_document(document)
        return document

    store_file = _path(filename)
    if not os.path.exists(store_file):
        payload = _read(filename)
        _write(filename, payload)
    payload = _read(filename)
    documents = payload[collection]
    document = dict(document)
    document.setdefault("id", len(documents) + 1)
    documents.append(document)
    _write(filename, payload)
    return document
