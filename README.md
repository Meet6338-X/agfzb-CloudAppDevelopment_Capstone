# Best Cars Dealership - Full Stack Cloud Development Capstone Project

**Project name: Best Cars Dealership - Full-Stack Cloud Development Capstone Project**

A full-stack dealership review application for *Best Cars Dealership*, a national car
retailer in the United States.  The application shows the dealership branches of the
group and lets the visitors read and publish reviews of a branch.

| Layer | Technology |
|---|---|
| Front end | React 18 (Vite) - `server/frontend` |
| Back end | Django 4.2 - `server` |
| Microservices | Node.js / Express and Python / Flask cloud functions - `functions` |
| Document store | Cloudant compatible document store - `cloudant/data` |
| CI/CD | GitHub Actions (linting) and Docker / Kubernetes - `.github/workflows` |

## Project layout

```
.
├── cloudant/data/            dealerships, reviews and car makes documents
├── functions/                the cloud functions (dealers, car makes, reviews, sentiment)
├── server/                   the Django application
│   ├── djangoapp/            models, views, urls, restapis, admin, templates
│   ├── djangobackend/        the Django project settings
│   ├── frontend/             the React front end (static/About.html, static/Contact.html,
│   │                         src/components/Register/Register.jsx, ...)
│   ├── Dockerfile            the container image of the Django application
│   ├── entrypoint.sh         the container entry point
│   └── deployment.yaml       the Kubernetes deployment and service
├── outputs/                  the captured terminal output of every lab task
└── .github/workflows/        the GitHub Actions linting workflow
```

## The application

* **Home page** - `/djangoapp/` lists the 50 dealerships of the group.  The list can
  be narrowed down to one state with the `state` query parameter, e.g.
  `/djangoapp/?state=Kansas`.
* **Dealer page** - `/djangoapp/dealer/<dealer_id>/` shows the reviews of a dealership
  together with the sentiment analysis of every review.
* **Add a review** - `/djangoapp/dealer/<dealer_id>/add_review/` posts a new review.
* **User management** - `/djangoapp/registration`, `/djangoapp/login` and
  `/djangoapp/logout`.
* **Static pages** - `/djangoapp/about` and `/djangoapp/contact`, and the standalone
  React pages `server/frontend/static/About.html` and
  `server/frontend/static/Contact.html`.
* **JSON endpoints** - `/djangoapp/carmakes` returns every car make with its car
  models and `/djangoapp/analyze?text=...` returns the sentiment of a review text.

## Running the project locally

### 1. The cloud functions

```bash
cd functions
npm install                     # the Node.js dealers / car makes function
pip install -r requirements.txt # the Python reviews / sentiment function
node get-dealership.js          # listens on http://localhost:3000
python reviews.py               # listens on http://localhost:5000
```

### 2. The Django application

```bash
cd server
pip install -r requirements.txt
python manage.py makemigrations djangoapp
python manage.py migrate
python manage.py seed_carmakes     # loads the car makes and the car models
python create_root_user.py         # creates the 'root' super user
python manage.py runserver 8000
```

The application is then available on <http://localhost:8000/djangoapp/>.
The Django server calls the cloud functions through the `DEALERS_URL`, `REVIEWS_URL`,
`POST_REVIEW_URL`, `CARMAKES_URL` and `SENTIMENT_URL` environment variables.

### 3. The React front end

```bash
cd server/frontend
npm install
npm run dev        # http://localhost:3000
npm run build
```

## Containerizing the application

```bash
docker build -t us.icr.io/$MY_NAMESPACE/dealership:latest server/
docker run -d -p 8000:8000 \
  -e DEALERS_URL=http://host.docker.internal:3000/dealerships/get \
  -e REVIEWS_URL=http://host.docker.internal:5000/api/get_reviews \
  -e POST_REVIEW_URL=http://host.docker.internal:5000/api/post_review \
  -e CARMAKES_URL=http://host.docker.internal:3000/carmakes/get \
  -e SENTIMENT_URL=http://host.docker.internal:5000/api/analyze \
  us.icr.io/$MY_NAMESPACE/dealership:latest
```

The `server/deployment.yaml` file holds the equivalent Kubernetes deployment.

## The captured lab output

Every task of the capstone assignment has its terminal output stored in the
`outputs` folder:

| File | Content |
|---|---|
| `django_server` | the Django development server running |
| `loginuser` | the cURL login request and its response |
| `logoutuser` | the cURL logout request and its response |
| `getdealerreviews` | the reviews of one dealership |
| `getalldealers` | every dealership |
| `getdealerbyid` | one dealership |
| `getdealersbyState` | the dealerships of Kansas |
| `getallcarmakes` | every car make and car model |
| `analyzereview` | the sentiment analysis of "Fantastic services" |
| `CICD` | the output of the GitHub Actions linting workflow |
| `deploymentURL` | the URL of the deployed application |

## Continuous integration

The **Lint Code** workflow (`.github/workflows/linter.yml`) lints the JavaScript
function, the Python function and the Django server on every push to `master` or
`main`.  It can also be started manually from the *Actions* tab of the repository.

## License

Apache License 2.0 - see [LICENSE](LICENSE).
