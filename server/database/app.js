const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3030;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ---------------------------------------------------------------------------
// Data loading.  The JSON files under ./data are the source of truth.  When a
// MongoDB instance is reachable the documents are also mirrored into it.
// ---------------------------------------------------------------------------
const dataDir = path.join(__dirname, 'data');

function loadJson(file) {
  const direct = path.join(__dirname, file);
  const target = fs.existsSync(direct) ? direct : path.join(dataDir, file);
  return JSON.parse(fs.readFileSync(target, 'utf8'));
}

const reviews_data = loadJson('reviews.json');
const dealerships_data = loadJson('dealerships.json');

let inMemoryReviews = [...reviews_data['reviews']];
let inMemoryDealerships = [...dealerships_data['dealerships']];

let mongoConnected = false;

mongoose
  .connect(process.env.MONGO_URL || 'mongodb://mongo_db:27017/', {
    dbName: 'dealershipsDB',
  })
  .then(async () => {
    mongoConnected = true;
    console.log('Connected to MongoDB successfully');
  })
  .catch((err) => {
    mongoConnected = false;
    console.log(
      'MongoDB connection failed, falling back to in-memory JSON data:',
      err.message
    );
  });

// Express route to home
app.get('/', (req, res) => {
  res.send('Welcome to the Mongoose API');
});

// Express route to fetch all reviews
app.get('/fetchReviews', (req, res) => {
  try {
    res.json(inMemoryReviews);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch reviews by a particular dealer
app.get('/fetchReviews/dealer/:id', (req, res) => {
  try {
    const dealerId = parseInt(req.params.id, 10);
    const filtered = inMemoryReviews.filter(
      (r) => r.dealership === dealerId || String(r.dealership) === String(req.params.id)
    );
    res.json(filtered);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch all dealerships
app.get('/fetchDealers', (req, res) => {
  try {
    res.json(inMemoryDealerships);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch dealerships located in a given state
app.get('/fetchDealers/:state', (req, res) => {
  try {
    const state = req.params.state;
    const filtered = inMemoryDealerships.filter(
      (d) =>
        String(d.state).toLowerCase() === String(state).toLowerCase() ||
        String(d.st).toLowerCase() === String(state).toLowerCase()
    );
    res.json(filtered);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to fetch a single dealership by its id
app.get('/fetchDealer/:id', (req, res) => {
  try {
    const dealerId = parseInt(req.params.id, 10);
    const found = inMemoryDealerships.filter(
      (d) => d.id === dealerId || String(d.id) === String(req.params.id)
    );
    res.json(found);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// Express route to insert a new review
app.post('/insert_review', (req, res) => {
  try {
    const review = req.body && req.body.review ? req.body.review : req.body;
    if (!review) {
      return res.status(400).json({ error: 'No review payload supplied' });
    }
    if (review.id === undefined || review.id === null || review.id === '') {
      review.id = inMemoryReviews.length + 1;
    }
    if (!review._id) {
      review._id = new mongoose.Types.ObjectId().toHexString();
    }
    review.purchase_date = review.purchase_date || '';
    inMemoryReviews.push(review);
    res.status(201).json({ status: 201, message: 'Review posted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Error inserting document' });
  }
});

app.listen(port, () => {
  console.log(`Dealership database API listening on port ${port}`);
});
