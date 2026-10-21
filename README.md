# Best Cars Dealership - Full-Stack Cloud Development Capstone Project

**Repository name: xrwvm-fullstack_developer_capstone**

**Project name: Best Cars Dealership - Full-Stack Cloud Development Capstone Project**

A full-stack dealership review application for *Best Cars Dealership*, a national car
retailer in the United States. The application lists the dealership branches of the
group, lets a visitor read the reviews of a branch, and lets a registered user publish
a new review.

| Layer | Technology | Location |
|---|---|---|
| Front end | React 18 (Vite) | `server/frontend` |
| Back end | Django 4.2 | `server` |
| Dealership database API | Node.js / Express (+ Mongoose when available) | `server/database` |
| Sentiment analyzer | Python / Flask (NLTK VADER) | `server/djangoapp/microservices` |
| Document store | Cloudant compatible document store | `cloudant/data` |
| CI/CD | GitHub Actions (linting + container build) | `.github/workflows` |

## Project layout

```
.
|-- cloudant/data/                 dealerships, reviews and car makes documents
|-- functions/                     the earlier cloud function implementation
|-- generate_db_data.py            builds server/database/data from cloudant/data
|-- server/
|   |-- database/                  the dealership database API (Express, port 3030)
|   |   |-- app.js                 /fetchDealers, /fetchDealer/:id, /fetchReviews...
|   |   |-- data/                  the JSON documents served by the API
|   |   `-- Dockerfile
|   |-- djangoapp/                 the Django application
|   |   |-- migrations/
|   |   |-- management/commands/   seed_carmakes management command
|   |   |-- microservices/         the sentiment analyzer (Flask, port 5050)
|   |   |-- models.py              CarMake, CarModel, CarDealer, DealerReview
|   |   |-- restapis.py            the calls to the database API and the analyzer
|   |   |-- urls.py                the URL configuration
|   |   |-- views.py               the HTML views and the JSON API views
|   |   `-- templates/djangoapp/   index, about, contact, dealer_details, add_review
|   |-- djangobackend/             the Django project settings
|   |-- frontend/                  the React front end
|   |   |-- src/components/        Header, Login, Register, Dealers, Dealer, PostReview
|   |   `-- static/                About.html, Contact.html, style.css, images
|   |-- Dockerfile                 the container image of the Django application
|   |-- entrypoint.sh              the container entry point
|   |-- deployment.yaml            the Kubernetes deployment and service
|   `-- create_root_user.py        creates the `root` reviewer account
|-- evidence/                      the screenshots submitted for the review criteria
|-- outputs/                       the terminal output files submitted for review
`-- cloudant/data/                 the seed documents
```

## The application URLs

| Page | URL |
|---|---|
| Home (all dealerships) | `http://localhost:8000/djangoapp/` |
| Home filtered by state | `http://localhost:8000/djangoapp/?state=Kansas` |
| About us | `http://localhost:8000/djangoapp/about` |
| Contact us | `http://localhost:8000/djangoapp/contact` |
| Sign up | `http://localhost:8000/djangoapp/registration` |
| Dealer details and reviews | `http://localhost:8000/djangoapp/dealer/15/` |
| Post a review | `http://localhost:8000/djangoapp/dealer/15/add_review/` |
| Django admin | `http://localhost:8000/admin/` |

## The JSON API

| Endpoint | Description |
|---|---|
| `POST /djangoapp/login` | `{"userName": "...", "password": "..."}` |
| `GET /djangoapp/logout` | returns `{"userName": ""}` |
| `POST /djangoapp/register` | `{"userName", "password", "firstName", "lastName", "email"}` |
| `GET /djangoapp/get_cars` | `{"status": 200, "CarModels": [...]}` |
| `GET /djangoapp/fetchDealers` | `{"status": 200, "dealers": [...]}` |
| `GET /djangoapp/fetchDealers/Kansas` | the dealers of one state |
| `GET /djangoapp/fetchDealer/8` | `{"status": 200, "dealer": [...]}` |
| `GET /djangoapp/fetchReviews/dealer/15` | `{"status": 200, "reviews": [...]}` |
| `POST /djangoapp/add_review` | publishes a review |
| `GET /djangoapp/analyze/Fantastic services` | the sentiment of a review |

The database API itself (`server/database/app.js`, port 3030) serves
`/fetchDealers`, `/fetchDealers/:state`, `/fetchDealer/:id`, `/fetchReviews`,
`/fetchReviews/dealer/:id` and `POST /insert_review`. The sentiment analyzer
(`server/djangoapp/microservices/app.py`, port 5050) serves `/analyze/<text>`.

## Running the project locally

```bash
# 1. the dealership database API (port 3030)
cd server/database && npm install && npm start

# 2. the sentiment analyzer (port 5050)
cd server/djangoapp/microservices && pip install -r requirements.txt && python app.py

# 3. the Django application (port 8000)
cd server && pip install -r requirements.txt
python manage.py migrate
python manage.py seed_carmakes
python create_root_user.py
python manage.py runserver 8000
```

The front end is built with `cd server/frontend && npm install && npm run build`.

## Containerizing the application

```bash
cd server
docker build -t dealership:latest .
docker run -d --name dealership-app -p 8000:8000 \
    -e backend_url=http://host.docker.internal:3030 \
    -e sentiment_analyzer_url=http://host.docker.internal:5050/ \
    dealership:latest
```

The container image is built and verified by the `Build the application container
image` job of the `Lint Code` GitHub Actions workflow.

## Continuous integration

`.github/workflows/linter.yml` runs on every push and pull request and on demand:

* `Linting JavaScript Function` - ESLint on the sample Node.js function
* `Linting Dealership Cloud Function` - ESLint on `server/database`
* `Linting Python Function` - pylint on the sample Python function
* `Linting Reviews Cloud Function` - pylint on the Flask services
* `Linting Django Server` - pylint on the Django project
* `Linting Django Application` - pylint on the Django application
* `Build the application container image` - builds the container image

## Submitted evidence

| File | Review criterion |
|---|---|
| `outputs/django_server` | the Django development server running |
| `outputs/loginuser` | the login operation |
| `outputs/logoutuser` | the logout operation |
| `outputs/getdealerreviews` | the reviews of a dealer |
| `outputs/getalldealers` | all the dealers |
| `outputs/getdealerbyid` | the details of one dealer |
| `outputs/getdealersbyState` | the dealers of the state of Kansas |
| `outputs/getallcarmakes` | all the car makes and models |
| `outputs/analyzereview` | the sentiment of "Fantastic services" |
| `outputs/CICD` | the GitHub Actions workflow run |
| `outputs/deploymentURL` | the deployment URL of the application |
| `evidence/*.png` | the screenshots of the application and the admin site |

## Licence

Apache License 2.0 - see [LICENSE](LICENSE).
