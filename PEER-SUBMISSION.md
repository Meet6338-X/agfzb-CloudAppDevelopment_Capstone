# Peer-Graded Submission (Option 2) — Field Values

Course: **Full Stack Application Development Capstone Project**
Peer-graded item: `Option 2: Peer-Graded Submission and Evaluation` (50 points)

## Text fields

| Field | Value |
|---|---|
| Project Title | `Best Cars Dealership - Full-Stack Cloud Development Capstone` |
| Task 1 — public GitHub repo URL | `https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone` |
| Task 24 — deployment URL | `http://dealership.127.0.0.1.nip.io:8010/djangoapp/` |

## Uploaded files (26) → task mapping

All files live in `evidence/` in this repository.

| Task | File | Points |
|---|---|---|
| 2 | `django_server.png` | 1 |
| 3 | `about_us.png` | 3 |
| 4 | `contact_us.png` | 2 |
| 5 | `login.png` | 2 |
| 6 | `logout.png` | 2 |
| 7 | `sign-up.png` | 1 |
| 8 | `dealer_review.png` | 2 |
| 9 | `dealerships.png` | 2 |
| 10 | `dealer_details.png` | 2 |
| 11 | `kansasDealers.png` | 2 |
| 12 | `admin_login.png` | 2 |
| 13 | `admin_logout.png` | 1 |
| 14 | `cars.png` | 2 |
| 15 | `car_models.png` | 2 |
| 16 | `sentiment_analyzer.png` | 2 |
| 17 | `get_dealers.png` | 1 |
| 18 | `get_dealers_loggedin.png` | 2 |
| 19 | `dealersbystate.png` | 2 |
| 20 | `dealer_id_reviews.png` | 1 |
| 21 | `dealership_review_submission.png` | 1 |
| 22 | `added_review.png` | 2 |
| 23 | `CICD.png` | 3 |
| 25 | `deployed_landingpage.png` | 2 |
| 26 | `deployed_loggedin.png` | 2 |
| 27 | `deployed_dealer_detail.png` | 2 |
| 28 | `deployed_add_review.png` | 2 |

## What the screenshots show

- **Tasks 8–11** hit the Express/Mongo API service directly (`http://127.0.0.1:3030/fetchReviews/dealer/15`,
  `/fetchDealers`, `/fetchDealer/8`, `/fetchDealers/Kansas`) — the endpoint is visible in the address bar.
- **Task 14** hits the Django proxy `http://127.0.0.1:8000/djangoapp/get_cars`.
- **Task 16** hits the sentiment microservice `http://127.0.0.1:5050/analyze/Fantastic%20services`.
- **Tasks 17–22** are the Django pages (`/djangoapp/`, `/djangoapp/?state=Kansas`, `/djangoapp/dealer/15/`,
  `/djangoapp/dealer/15/add_review/`).
- **Tasks 25–28** are the Dockerised deployment reached through
  `http://dealership.127.0.0.1.nip.io:8010/djangoapp/` — the same URL that is entered for Task 24.
- **Task 23** is the successful GitHub Actions run
  (`https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/actions/runs/39628438944` — 7/7 jobs green).
- **Task 2** is a real `cmd.exe` window running `python manage.py runserver 8000`.

## Services used to produce the evidence

| Service | Port | Purpose |
|---|---|---|
| `server/database/app.js` (Express + optional Mongoose) | 3030 | `/fetchDealers`, `/fetchDealer/:id`, `/fetchDealers/:state`, `/fetchReviews/dealer/:id` |
| `server/djangoapp/microservices/app.py` (Flask + nltk VADER) | 5050 | `/analyze/<text>` |
| Django (`manage.py runserver 8000`) | 8000 | HTML pages + JSON proxy API under `/djangoapp/` |
| Docker container `dealership-app` (image `dealership:latest`) | 8010 | the deployed application |

Application user `shahm` / `Shahm@2024`; Django admin superuser `root` / `root`.
