/**
 * Cloud function that returns the dealerships and the car makes.
 *
 * The function exposes two endpoints:
 *
 *   GET /dealerships/get            -> every dealership
 *   GET /dealerships/get?state=...  -> the dealerships of one state
 *   GET /dealerships/get?id=...     -> one dealership
 *   GET /carmakes/get               -> every car make with its car models
 */
const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(express.json());

const DATA_DIR = path.join(__dirname, '..', 'cloudant', 'data');
const CLOUDANT_URL = process.env.CLOUDANT_URL || '';
const CLOUDANT_APIKEY = process.env.CLOUDANT_APIKEY || '';

/**
 * Read a document file of the local store (used when Cloudant is not
 * configured so that the application can run offline).
 */
function readLocal(fileName) {
  const payload = JSON.parse(fs.readFileSync(path.join(DATA_DIR, fileName), 'utf8'));
  return payload[Object.keys(payload)[0]];
}

/**
 * Return every document of a Cloudant database.
 */
async function getDocuments(database, fileName) {
  if (CLOUDANT_URL && CLOUDANT_APIKEY) {
    const Cloudant = require('@cloudant/cloudant');
    const client = new Cloudant({ apikey: CLOUDANT_APIKEY });
    const docs = await client.database(database).allDocs({ include_docs: true });
    return docs.rows.map((row) => row.doc);
  }
  return readLocal(fileName);
}

app.get('/dealerships/get', async (req, res) => {
  const { state, id } = req.query;
  const selector = {};
  if (state) {
    selector.state = state;
  }
  if (id) {
    selector.id = parseInt(id, 10);
  }

  const documents = await getDocuments('dealerships', 'dealerships.json');
  const result = documents.filter((doc) => {
    if (state && doc.state !== state) {
      return false;
    }
    if (id && parseInt(doc.id, 10) !== parseInt(id, 10)) {
      return false;
    }
    return true;
  });
  res.json(result);
});

app.get('/carmakes/get', async (req, res) => {
  const documents = await getDocuments('carmakes', 'carmakes.json');
  const carMakes = documents.map((make) => ({
    id: make.id,
    name: make.name,
    description: make.description,
    car_models: make.car_models,
  }));
  res.json(carMakes);
});

app.get('/', (req, res) => {
  res.json({
    message: 'Best Cars Dealership cloud function',
    endpoints: ['/dealerships/get', '/carmakes/get'],
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Dealers function listening on port ${PORT}`);
});

module.exports = app;
