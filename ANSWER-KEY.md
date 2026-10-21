# Best Cars Dealership - Full-Stack Cloud Development Capstone Project

**Final assignment answer key - 28 tasks / 50 points**

* Repository: https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone
* Repository name: xrwvm-fullstack_developer_capstone
* Project name: Best Cars Dealership - Full-Stack Cloud Development Capstone Project
* Deployed application URL: https://xrwvm-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/djangoapp
* Application user: `shahm` / `Shahm@2024`   |   Django admin (root user): `root` / `root`

| # | Pts | What to submit | Where it lives |
|---|-----|----------------|-----------------|
| 1 | 1 pt | Public GitHub URL of the README.md file that contains the Project name details | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/README.md |
| 2 | 1 pt | Terminal output showing the Django server running (file: django_server) | `outputs/django_server` |
| 3 | 3 pts | Public GitHub URL of server/frontend/static/About.html (updated About Us page) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/server/frontend/static/About.html |
| 4 | 2 pts | Public GitHub URL of server/frontend/static/Contact.html (Contact Us page) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/server/frontend/static/Contact.html |
| 5 | 2 pts | cURL command + output for a login operation (file: loginuser) | `outputs/loginuser` |
| 6 | 2 pts | cURL command + output for a logout operation (file: logoutuser) | `outputs/logoutuser` |
| 7 | 1 pt | Public GitHub URL of server/frontend/src/components/Register/Register.jsx (Sign-up page) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/server/frontend/src/components/Register/Register.jsx |
| 8 | 2 pts | cURL command + output showing the review(s) for a dealer ID (file: getdealerreviews) | `outputs/getdealerreviews` |
| 9 | 2 pts | cURL command + output showing all dealer(s) retrieved (file: getalldealers) | `outputs/getalldealers` |
| 10 | 2 pts | cURL command + output showing the details of a dealer ID (file: getdealerbyid) | `outputs/getdealerbyid` |
| 11 | 2 pts | cURL command + output showing the dealer(s) in Kansas (file: getdealersbyState) | `outputs/getdealersbyState` |
| 12 | 2 pts | Screenshot of the root user logged in on the admin page (admin_login.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/admin_login.png |
| 13 | 1 pt | Screenshot of the root user logged out from the admin page (admin_logout.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/admin_logout.png |
| 14 | 2 pts | cURL command + output showing all car makes and models retrieved (file: getallcarmakes) - part 1 | `outputs/getallcarmakes` |
| 15 | 2 pts | cURL command + output showing all car makes and models retrieved (file: getallcarmakes) - part 2 | `outputs/getallcarmakes` |
| 16 | 2 pts | cURL command + output showing the sentiment analysis of "Fantastic services" (file: analyzereview) | `outputs/analyzereview` |
| 17 | 1 pt | Screenshot of the dealers on the home page before logging in (get_dealers.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/get_dealers.png |
| 18 | 2 pts | Screenshot of the dealers after logging in (get_dealers_loggedin.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/get_dealers_loggedin.png |
| 19 | 2 pts | Screenshot of the dealers filtered by State (dealersbystate.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/dealersbystate.png |
| 20 | 1 pt | Screenshot of the dealer page with its reviews (dealer_id_reviews.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/dealer_id_reviews.png |
| 21 | 1 pt | Screenshot of the Post Review page after entering the review, before submission (dealership_review_submission.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/dealership_review_submission.png |
| 22 | 2 pts | Screenshot of the posted review (added_review.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/added_review.png |
| 23 | 3 pts | Terminal output of the GitHub Actions workflow running successfully (file: CICD) | `outputs/CICD` |
| 24 | 1 pt | Deployment URL of the Django application (file: deploymentURL) | `outputs/deploymentURL` |
| 25 | 2 pts | Screenshot of the deployed landing page (deployed_landingpage.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_landingpage.png |
| 26 | 2 pts | Screenshot of the deployed logged-in page (deployed_loggedin.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_loggedin.png |
| 27 | 2 pts | Screenshot of the dealer details page opened through the deployment (deployed_dealer_detail.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_dealer_detail.png |
| 28 | 2 pts | Screenshot of the review displayed in the deployed application (deployed_add_review.png) | https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_add_review.png |

---

## Task 1 (1 pt) - Public GitHub URL of the README.md file that contains the Project name details

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/README.md
```

> The repository name is **xrwvm-fullstack_developer_capstone** and the README.md starts with the project name heading **"Best Cars Dealership - Full-Stack Cloud Development Capstone Project"** followed by the project breakdown, the repository layout, the list of application URLs, the local run instructions and the CI/CD section.

## Task 2 (1 pt) - Terminal output showing the Django server running (file: django_server)

**File to submit:** `outputs/django_server`

```
# The Django development server of the Best Cars Dealership app.

Command: python manage.py runserver 8000

Performing system checks...

System check identified no issues (0 silenced).
October 21, 2026 - 21:20:10
Django version 4.2.16, using settings 'djangobackend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Task 3 (3 pts) - Public GitHub URL of server/frontend/static/About.html (updated About Us page)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/server/frontend/static/About.html
```

> The page contains the Bootstrap CSS link, the local stylesheets `/static/style.css` and `/static/bootstrap.min.css`, a hero image, the "Welcome to Best Cars dealership, home to the best cars in North America. We deal in sale of domestic and imported cars at reasonable prices." description and a 4 member team section. Each team member has a **name, role, brief details, email ID and a realistic photo** (Shahm Dar - Full Stack Developer, Aisha Rahman - Backend Developer, Omar Khalid - Cloud Engineer, Sara Ahmed - UI/UX Designer).

## Task 4 (2 pts) - Public GitHub URL of server/frontend/static/Contact.html (Contact Us page)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/server/frontend/static/Contact.html
```

> The page contains the Bootstrap CSS link, the stylesheet links `/static/style.css` and `/static/bootstrap.min.css`, a **navigation bar where "Contact Us" carries the class `nav-link active`**, the images `/static/contactus.png` and `/static/cars.jpeg`, the head-office address (100 Dealerships Way, Suite 500, Austin, TX 78701), the phone number +1 (800) 555-CARS (2277), the email IDs contact@dealerships.com and support@dealerships.com and the operating hours.

## Task 5 (2 pts) - cURL command + output for a login operation (file: loginuser)

**File to submit:** `outputs/loginuser`

```
# Log in with a valid user name and password.

Command: curl.exe -i -c cookie.txt -X POST -H "Content-Type: application/json" -d "{\"userName\": \"shahm\", \"password\": \"Shahm@2024\"}" http://localhost:8000/djangoapp/login

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:17 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 89
Vary: Cookie
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
Set-Cookie:  sessionid=jd5gwc7y5m89g8b5ibt8op2wf681fzco; expires=Wed, 04 Nov 2026 15:50:17 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax

{"userName": "shahm", "status": "Authenticated", "firstname": "Shahm", "lastname": "Dar"}
```

## Task 6 (2 pts) - cURL command + output for a logout operation (file: logoutuser)

**File to submit:** `outputs/logoutuser`

```
# Log out the user that was logged in by the previous request.

Command: curl.exe -i -b cookie.txt -c cookie.txt http://localhost:8000/djangoapp/logout

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:17 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 16
Vary: Cookie
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
Set-Cookie:  sessionid=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/; SameSite=Lax

{"userName": ""}
```

## Task 7 (1 pt) - Public GitHub URL of server/frontend/src/components/Register/Register.jsx (Sign-up page)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/server/frontend/src/components/Register/Register.jsx
```

> The repository is **xrwvm-fullstack_developer_capstone**. The component renders **all five input fields - Username, First Name, Last Name, Email and Password - and a Register button** which posts the JSON body `{userName, password, firstName, lastName, email}` to the Django `djangoapp/register` endpoint.

## Task 8 (2 pts) - cURL command + output showing the review(s) for a dealer ID (file: getdealerreviews)

**File to submit:** `outputs/getdealerreviews`

```
# The reviews that were submitted for dealer id 15.

Command: curl.exe -i http://localhost:8000/djangoapp/fetchReviews/dealer/15

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:21 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 590
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"status": 200, "reviews": [{"id": 1, "name": "Berkly Shepley", "dealership": 15, "review": "Total grid-enabled service-desk", "purchase": true, "purchase_date": "07/11/2020", "car_make": "Audi", "car_model": "A6", "car_year": 2010, "_id": "c8f5c174d0eed5be98693ce0", "sentiment": "neutral"}, {"id": 15, "name": "Tempsoft Car Dealership", "dealership": 15, "review": "Fantastic services, friendly staff and a great car.", "purchase": "Yes", "purchase_date": "2026-10-15", "car_make": "Audi", "car_model": "A6", "car_year": 2010, "_id": "c4617564b1254f0d244dfe76", "sentiment": "positive"}]}
```

## Task 9 (2 pts) - cURL command + output showing all dealer(s) retrieved (file: getalldealers)

**File to submit:** `outputs/getalldealers`

```
# Every dealership that is stored in the dealerships database.

Command: curl.exe -i http://localhost:8000/djangoapp/fetchDealers

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:22 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 12400
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"status": 200, "dealers": [{"id": 1, "city": "El Paso", "state": "Texas", "st": "TX", "address": "3 Nova Court", "zip": "88563", "lat": 31.6948, "long": -106.3, "short_name": "Holdlamis", "full_name": "Holdlamis Car Dealership", "_id": "2cc1a01bd81c4f980f4453fc"}, {"id": 2, "city": "Minneapolis", "state": "Minnesota", "st": "MN", "address": "6337 Butternut Crossing", "zip": "55402", "lat": 44.9762, "long": -93.2759, "short_name": "Temp", "full_name": "Temp Car Dealership", "_id": "7a0cc189e38bfa43aa19a477"}, {"id": 3, "city": "Birmingham", "state": "Alabama", "st": "AL", "address": "9477 Twin Pines Center", "zip": "35285", "lat": 33.5446, "long": -86.9292, "short_name": "Sub-Ex", "full_name": "Sub-Ex Car Dealership", "_id": "07d5f560b838fb23954190f1"}, {"id": 4, "city": "Dallas", "state": "Texas", "st": "TX", "address": "85800 Hazelcrest Circle", "zip": "75241", "lat": 32.6722, "long": -96.7774, "short_name": "Solarbreeze", "full_name": "Solarbreeze Car Dealership", "_id": "ea05c52c69e3de8dd9fa3bff"}, {"id": 5, "city": "Baltimore", "state": "Maryland", "st": "MD", "address": "93 Golf Course Pass", "zip": "21203", "lat": 39.2847, "long": -76.6205, "short_name": "Regrant", "full_name": "Regrant Car Dealership", "_id": "62e190cf091f10ea5179faef"}, {"id": 6, "city": "Wilkes Barre", "state": "Pennsylvania", "st": "PA", "address": "2 Burrows Hill", "zip": "18763", "lat": 41.2722, "long": -75.8801, "short_name": "Stronghold", "full_name": "Stronghold Car Dealership", "_id": "120dbe3db39c7a0ad031e674"}, {"id": 7, "city": "Pueblo", "state": "Colorado", "st": "CO", "address": "9 Cambridge Park", "zip": "81010", "lat": 38.1286, "long": -104.5523, "short_name": "Job", "full_name": "Job Car Dealership", "_id": "7e52256f102ea699b7f70e32"}, {"id": 8, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "288 Larry Place", "zip": "66642", "lat": 39.0429, "long": -95.7697, "short_name": "Bytecard", "full_name": "Bytecard Car Dealership", "_id": "5a17d839866dd31614427921"}, {"id": 9, "city": "Dallas", "state": "Texas", "st": "TX", "address": "253 Hanson Junction", "zip": "75216", "lat": 32.7086, "long": -96.7955, "short_name": "Job", "full_name": "Job Car Dealership", "_id": "f7a8da0d68ac2faa1203959b"}, {"id": 10, "city": "Washington", "state": "District of Columbia", "st": "DC", "address": "108 Memorial Pass", "zip": "20005", "lat": 38.9067, "long": -77.0312, "short_name": "Alphazap", "full_name": "Alphazap Car Dealership", "_id": "084ed6c78cdea4203eabd5ca"}, {"id": 11, "city": "Carol Stream", "state": "Illinois", "st": "IL", "address": "8108 Dryden Court", "zip": "60351", "lat": 41.9166, "long": -88.1208, "short_name": "Rank", "full_name": "Rank Car Dealership", "_id": "b5ce45a0bc72e971839dd147"}, {"id": 12, "city": "Silver Spring", "state": "Maryland", "st": "MD", "address": "168 Pawling Lane", "zip": "20918", "lat": 39.144, "long": -77.2076, "short_name": "Tin", "full_name": "Tin Car Dealership", "_id": "980f55cc4ab4126666d69094"}, {"id": 13, "city": "Baltimore", "state": "Maryland", "st": "MD", "address": "452 Fair Oaks Drive", "zip": "21275", "lat": 39.2847, "long": -76.6205, "short_name": "Y-Solowarm", "full_name": "Y-Solowarm Car Dealership", "_id": "644f9763b6c7d1566316e8d8"}, {"id": 14, "city": "San Francisco", "state": "California", "st": "CA", "address": "2109 Scott Parkway", "zip": "94147", "lat": 37.7848, "long": -122.7278, "short_name": "It", "full_name": "It Car Dealership", "_id": "2a0f39cdddf3b716557f95df"}, {"id": 15, "city": "San Antonio", "state": "Texas", "st": "TX", "address": "5057 Pankratz Hill", "zip": "78225", "lat": 29.3875, "long": -98.5245, "short_name": "Tempsoft", "full_name": "Tempsoft Car Dealership", "_id": "57f99c3cb5e0c58b09775c23"}, {"id": 16, "city": "El Paso", "state": "Texas", "st": "TX", "address": "0 Rieder Trail", "zip": "79994", "lat": 31.6948, "long": -106.3, "short_name": "Treeflex", "full_name": "Treeflex Car Dealership", "_id": "5d5ab9b4a5b5c818a5290238"}, {"id": 17, "city": "San Jose", "state": "California", "st": "CA", "address": "7670 American Ash Drive", "zip": "95138", "lat": 37.2602, "long": -121.7709, "short_name": "Home Ing", "full_name": "Home Ing Car Dealership", "_id": "b2b28883104a45c27150bacd"}, {"id": 18, "city": "Whittier", "state": "California", "st": "CA", "address": "4 Pearson Avenue", "zip": "90605", "lat": 33.9413, "long": -118.0356, "short_name": "Bitchip", "full_name": "Bitchip Car Dealership", "_id": "b8a1233d7a0ab87c79007358"}, {"id": 19, "city": "Hialeah", "state": "Florida", "st": "FL", "address": "93 Monument Circle", "zip": "33013", "lat": 25.8594, "long": -80.2725, "short_name": "Otcom", "full_name": "Otcom Car Dealership", "_id": "a6b529222985bb77696d4753"}, {"id": 20, "city": "Detroit", "state": "Michigan", "st": "MI", "address": "4580 Waubesa Lane", "zip": "48224", "lat": 42.4098, "long": -82.9441, "short_name": "Subin", "full_name": "Subin Car Dealership", "_id": "4a5b0cc6ee3b1fa197e39a2e"}, {"id": 21, "city": "San Francisco", "state": "California", "st": "CA", "address": "046 Mockingbird Junction", "zip": "94154", "lat": 37.7848, "long": -122.7278, "short_name": "Andalax", "full_name": "Andalax Car Dealership", "_id": "fccab8774db9652f1962e7d1"}, {"id": 22, "city": "Fort Lauderdale", "state": "Florida", "st": "FL", "address": "45737 Butternut Lane", "zip": "33330", "lat": 26.0663, "long": -80.3339, "short_name": "Y-Solowarm", "full_name": "Y-Solowarm Car Dealership", "_id": "f07a6ec9adb639b330a70879"}, {"id": 23, "city": "Des Moines", "state": "Iowa", "st": "IA", "address": "21425 Bartelt Pass", "zip": "50936", "lat": 41.6727, "long": -93.5722, "short_name": "Bitchip", "full_name": "Bitchip Car Dealership", "_id": "78215035756092b265f37126"}, {"id": 24, "city": "Utica", "state": "New York", "st": "NY", "address": "408 Delaware Circle", "zip": "13505", "lat": 43.0872, "long": -75.2603, "short_name": "Aerified", "full_name": "Aerified Car Dealership", "_id": "2173c0d24fb51318e98f9b87"}, {"id": 25, "city": "Washington", "state": "District of Columbia", "st": "DC", "address": "6505 Melrose Junction", "zip": "20580", "lat": 38.8933, "long": -77.0146, "short_name": "Opela", "full_name": "Opela Car Dealership", "_id": "c7545b12278aa5bbec4c094b"}, {"id": 26, "city": "Pittsburgh", "state": "Pennsylvania", "st": "PA", "address": "306 Jenna Parkway", "zip": "15279", "lat": 40.4344, "long": -80.0248, "short_name": "Flowdesk", "full_name": "Flowdesk Car Dealership", "_id": "9c1c9b58a921f0a4bb081bda"}, {"id": 27, "city": "San Antonio", "state": "Texas", "st": "TX", "address": "95321 Superior Hill", "zip": "78245", "lat": 29.4189, "long": -98.6895, "short_name": "Namfix", "full_name": "Namfix Car Dealership", "_id": "59a0604dd1b733406aa15c3e"}, {"id": 28, "city": "Hialeah", "state": "Florida", "st": "FL", "address": "5458 Maple Way", "zip": "33018", "lat": 25.9098, "long": -80.3889, "short_name": "Fixflex", "full_name": "Fixflex Car Dealership", "_id": "d05b32bffff616b337a7a412"}, {"id": 29, "city": "San Francisco", "state": "California", "st": "CA", "address": "9 Harper Circle", "zip": "94110", "lat": 37.7509, "long": -122.4153, "short_name": "Fix San", "full_name": "Fix San Car Dealership", "_id": "c5eb4fc92328956ec1db4087"}, {"id": 30, "city": "Houston", "state": "Texas", "st": "TX", "address": "5423 Spaight Road", "zip": "77218", "lat": 29.834, "long": -95.4342, "short_name": "Opela", "full_name": "Opela Car Dealership", "_id": "e63c539798bbd3755b0ec164"}, {"id": 31, "city": "New York City", "state": "New York", "st": "NY", "address": "5 Northfield Pass", "zip": "10131", "lat": 40.7808, "long": -73.9772, "short_name": "Fintone", "full_name": "Fintone Car Dealership", "_id": "e4ddec2c1eb8ec16ef1c3152"}, {"id": 32, "city": "Wilkes Barre", "state": "Pennsylvania", "st": "PA", "address": "3 Carey Junction", "zip": "18768", "lat": 41.2722, "long": -75.8801, "short_name": "Subin", "full_name": "Subin Car Dealership", "_id": "82ba7f54d66c3b125a37e8eb"}, {"id": 33, "city": "Des Moines", "state": "Iowa", "st": "IA", "address": "627 Cottonwood Circle", "zip": "50335", "lat": 41.6727, "long": -93.5722, "short_name": "Tres-Zap", "full_name": "Tres-Zap Car Dealership", "_id": "91f9ab4005a89ddeb9aa8312"}, {"id": 34, "city": "Silver Spring", "state": "Maryland", "st": "MD", "address": "8 Green Hill", "zip": "20904", "lat": 39.0668, "long": -76.9969, "short_name": "Gembucket", "full_name": "Gembucket Car Dealership", "_id": "de0091c3de0ac91ba9a647c1"}, {"id": 35, "city": "Seattle", "state": "Washington", "st": "WA", "address": "9 Beilfuss Trail", "zip": "98158", "lat": 47.4497, "long": -122.3076, "short_name": "Treeflex", "full_name": "Treeflex Car Dealership", "_id": "f0ac8c1c842393a7bca8663e"}, {"id": 36, "city": "Vienna", "state": "Virginia", "st": "VA", "address": "311 Paget Alley", "zip": "22184", "lat": 38.8318, "long": -77.2888, "short_name": "Latlux", "full_name": "Latlux Car Dealership", "_id": "5ce465dd01cc233e6c964a8b"}, {"id": 37, "city": "Detroit", "state": "Michigan", "st": "MI", "address": "152 Moland Lane", "zip": "48224", "lat": 42.4098, "long": -82.9441, "short_name": "Ventosanzap", "full_name": "Ventosanzap Car Dealership", "_id": "603742ffaca4748f70bf3036"}, {"id": 38, "city": "Dallas", "state": "Texas", "st": "TX", "address": "821 New Castle Trail", "zip": "75226", "lat": 32.7887, "long": -96.7676, "short_name": "Zamit", "full_name": "Zamit Car Dealership", "_id": "b4b6121d984443df9ea2c833"}, {"id": 39, "city": "Fresno", "state": "California", "st": "CA", "address": "990 Raven Road", "zip": "93740", "lat": 36.7464, "long": -119.6397, "short_name": "Stronghold", "full_name": "Stronghold Car Dealership", "_id": "b453a9e273f1dabd36b1d540"}, {"id": 40, "city": "Merrifield", "state": "Virginia", "st": "VA", "address": "89375 Main Trail", "zip": "22119", "lat": 38.8318, "long": -77.2888, "short_name": "Greenlam", "full_name": "Greenlam Car Dealership", "_id": "e18052ad3c301abc2eabb8f7"}, {"id": 41, "city": "Baltimore", "state": "Maryland", "st": "MD", "address": "9 Sherman Hill", "zip": "21275", "lat": 39.2847, "long": -76.6205, "short_name": "Tres-Zap", "full_name": "Tres-Zap Car Dealership", "_id": "27728ceb64b919e6e9b23919"}, {"id": 42, "city": "Jersey City", "state": "New Jersey", "st": "NJ", "address": "62 Manley Point", "zip": "07310", "lat": 40.7324, "long": -74.0431, "short_name": "Konklab", "full_name": "Konklab Car Dealership", "_id": "d3e2c0387342e3f0fd802f87"}, {"id": 43, "city": "Atlanta", "state": "Georgia", "st": "GA", "address": "91 Declaration Avenue", "zip": "31119", "lat": 33.8913, "long": -84.0746, "short_name": "Opela", "full_name": "Opela Car Dealership", "_id": "d21635dca3a294f1cd70acc2"}, {"id": 44, "city": "Roanoke", "state": "Virginia", "st": "VA", "address": "0 Northview Point", "zip": "24014", "lat": 37.2327, "long": -79.9463, "short_name": "Veribet", "full_name": "Veribet Car Dealership", "_id": "0eca895ffda13b1090699126"}, {"id": 45, "city": "Norfolk", "state": "Virginia", "st": "VA", "address": "283 Mockingbird Plaza", "zip": "23509", "lat": 36.8787, "long": -76.2604, "short_name": "Konklux", "full_name": "Konklux Car Dealership", "_id": "6bf8624bfedca1852a13b0a7"}, {"id": 46, "city": "New Orleans", "state": "Louisiana", "st": "LA", "address": "527 Hayes Junction", "zip": "70165", "lat": 30.033, "long": -89.8826, "short_name": "Regrant", "full_name": "Regrant Car Dealership", "_id": "5b3a2e67d441f9ff3264678c"}, {"id": 47, "city": "Stamford", "state": "Connecticut", "st": "CT", "address": "840 Pepper Wood Crossing", "zip": "06905", "lat": 41.0888, "long": -73.5435, "short_name": "Prodder", "full_name": "Prodder Car Dealership", "_id": "e326e7d54a8c5477a2f06524"}, {"id": 48, "city": "Tucson", "state": "Arizona", "st": "AZ", "address": "48610 Morning Street", "zip": "85710", "lat": 32.2138, "long": -110.824, "short_name": "It", "full_name": "It Car Dealership", "_id": "da209ace8817f3b565d5f409"}, {"id": 49, "city": "Athens", "state": "Georgia", "st": "GA", "address": "222 Grasskamp Plaza", "zip": "30605", "lat": 33.9321, "long": -83.3525, "short_name": "Veribet", "full_name": "Veribet Car Dealership", "_id": "c2696290db5af3cfac1f7386"}, {"id": 50, "city": "Atlanta", "state": "Georgia", "st": "GA", "address": "76 Clove Trail", "zip": "30316", "lat": 33.7217, "long": -84.3339, "short_name": "Aerified", "full_name": "Aerified Car Dealership", "_id": "d99c46efc3d5813d1165e10e"}]}
```

## Task 10 (2 pts) - cURL command + output showing the details of a dealer ID (file: getdealerbyid)

**File to submit:** `outputs/getdealerbyid`

```
# The details of dealer id 8 (Bytecard Car Dealership, Topeka, Kansas).

Command: curl.exe -i http://localhost:8000/djangoapp/fetchDealer/8

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:22 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 268
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"status": 200, "dealer": [{"id": 8, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "288 Larry Place", "zip": "66642", "lat": 39.0429, "long": -95.7697, "short_name": "Bytecard", "full_name": "Bytecard Car Dealership", "_id": "5a17d839866dd31614427921"}]}
```

## Task 11 (2 pts) - cURL command + output showing the dealer(s) in Kansas (file: getdealersbyState)

**File to submit:** `outputs/getdealersbyState`

```
# Every dealership that is located in the state of Kansas.

Command: curl.exe -i http://localhost:8000/djangoapp/fetchDealers/Kansas

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:22 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 269
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"status": 200, "dealers": [{"id": 8, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "288 Larry Place", "zip": "66642", "lat": 39.0429, "long": -95.7697, "short_name": "Bytecard", "full_name": "Bytecard Car Dealership", "_id": "5a17d839866dd31614427921"}]}
```

## Task 12 (2 pts) - Screenshot of the root user logged in on the admin page (admin_login.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/admin_login.png
```

> The Django admin site shows "WELCOME, ROOT" in the top-right user tools after logging in with **root / root**.

## Task 13 (1 pt) - Screenshot of the root user logged out from the admin page (admin_logout.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/admin_logout.png
```

> The admin logout confirmation page: "Logged out. Thanks for spending some quality time with the web site today."

## Task 14 (2 pts) - cURL command + output showing all car makes and models retrieved (file: getallcarmakes) - part 1

**File to submit:** `outputs/getallcarmakes`

```
# Every car make together with the car models of that make.

Command: curl.exe -i http://localhost:8000/djangoapp/get_cars

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:23 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 2125
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"status": 200, "CarModels": [{"CarModel": "A6", "CarMake": "Audi"}, {"CarModel": "A4", "CarMake": "Audi"}, {"CarModel": "Q5", "CarMake": "Audi"}, {"CarModel": "Q7", "CarMake": "Audi"}, {"CarModel": "3 Series", "CarMake": "BMW"}, {"CarModel": "X3", "CarMake": "BMW"}, {"CarModel": "X5", "CarMake": "BMW"}, {"CarModel": "M3", "CarMake": "BMW"}, {"CarModel": "Silverado 1500", "CarMake": "Chevrolet"}, {"CarModel": "Equinox", "CarMake": "Chevrolet"}, {"CarModel": "Malibu", "CarMake": "Chevrolet"}, {"CarModel": "Tahoe", "CarMake": "Chevrolet"}, {"CarModel": "F-150", "CarMake": "Ford"}, {"CarModel": "Escape", "CarMake": "Ford"}, {"CarModel": "Explorer", "CarMake": "Ford"}, {"CarModel": "Mustang", "CarMake": "Ford"}, {"CarModel": "Civic", "CarMake": "Honda"}, {"CarModel": "Accord", "CarMake": "Honda"}, {"CarModel": "CR-V", "CarMake": "Honda"}, {"CarModel": "Pilot", "CarMake": "Honda"}, {"CarModel": "Wrangler", "CarMake": "Jeep"}, {"CarModel": "Grand Cherokee", "CarMake": "Jeep"}, {"CarModel": "Cherokee", "CarMake": "Jeep"}, {"CarModel": "Compass", "CarMake": "Jeep"}, {"CarModel": "Altima", "CarMake": "Nissan"}, {"CarModel": "Sentra", "CarMake": "Nissan"}, {"CarModel": "Rogue", "CarMake": "Nissan"}, {"CarModel": "Pathfinder", "CarMake": "Nissan"}, {"CarModel": "Camry", "CarMake": "Toyota"}, {"CarModel": "Corolla", "CarMake": "Toyota"}, {"CarModel": "RAV4", "CarMake": "Toyota"}, {"CarModel": "Highlander", "CarMake": "Toyota"}, {"CarModel": "Jetta", "CarMake": "Volkswagen"}, {"CarModel": "Passat", "CarMake": "Volkswagen"}, {"CarModel": "Tiguan", "CarMake": "Volkswagen"}, {"CarModel": "Atlas", "CarMake": "Volkswagen"}, {"CarModel": "Model 3", "CarMake": "Tesla"}, {"CarModel": "Model S", "CarMake": "Tesla"}, {"CarModel": "Model Y", "CarMake": "Tesla"}, {"CarModel": "Model X", "CarMake": "Tesla"}, {"CarModel": "Ariya", "CarMake": "Nissan"}, {"CarModel": "C-Class", "CarMake": "Mercedes"}, {"CarModel": "E-Class", "CarMake": "Mercedes"}, {"CarModel": "A5", "CarMake": "Audi"}, {"CarModel": "Sorento", "CarMake": "Kia"}, {"CarModel": "Carnival", "CarMake": "Kia"}, {"CarModel": "Kluger", "CarMake": "Toyota"}]}
```

## Task 15 (2 pts) - cURL command + output showing all car makes and models retrieved (file: getallcarmakes) - part 2

**File to submit:** `outputs/getallcarmakes`

```
# Every car make together with the car models of that make.

Command: curl.exe -i http://localhost:8000/djangoapp/get_cars

HTTP/1.1 200 OK
Date: Wed, 21 Oct 2026 15:50:23 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 2125
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"status": 200, "CarModels": [{"CarModel": "A6", "CarMake": "Audi"}, {"CarModel": "A4", "CarMake": "Audi"}, {"CarModel": "Q5", "CarMake": "Audi"}, {"CarModel": "Q7", "CarMake": "Audi"}, {"CarModel": "3 Series", "CarMake": "BMW"}, {"CarModel": "X3", "CarMake": "BMW"}, {"CarModel": "X5", "CarMake": "BMW"}, {"CarModel": "M3", "CarMake": "BMW"}, {"CarModel": "Silverado 1500", "CarMake": "Chevrolet"}, {"CarModel": "Equinox", "CarMake": "Chevrolet"}, {"CarModel": "Malibu", "CarMake": "Chevrolet"}, {"CarModel": "Tahoe", "CarMake": "Chevrolet"}, {"CarModel": "F-150", "CarMake": "Ford"}, {"CarModel": "Escape", "CarMake": "Ford"}, {"CarModel": "Explorer", "CarMake": "Ford"}, {"CarModel": "Mustang", "CarMake": "Ford"}, {"CarModel": "Civic", "CarMake": "Honda"}, {"CarModel": "Accord", "CarMake": "Honda"}, {"CarModel": "CR-V", "CarMake": "Honda"}, {"CarModel": "Pilot", "CarMake": "Honda"}, {"CarModel": "Wrangler", "CarMake": "Jeep"}, {"CarModel": "Grand Cherokee", "CarMake": "Jeep"}, {"CarModel": "Cherokee", "CarMake": "Jeep"}, {"CarModel": "Compass", "CarMake": "Jeep"}, {"CarModel": "Altima", "CarMake": "Nissan"}, {"CarModel": "Sentra", "CarMake": "Nissan"}, {"CarModel": "Rogue", "CarMake": "Nissan"}, {"CarModel": "Pathfinder", "CarMake": "Nissan"}, {"CarModel": "Camry", "CarMake": "Toyota"}, {"CarModel": "Corolla", "CarMake": "Toyota"}, {"CarModel": "RAV4", "CarMake": "Toyota"}, {"CarModel": "Highlander", "CarMake": "Toyota"}, {"CarModel": "Jetta", "CarMake": "Volkswagen"}, {"CarModel": "Passat", "CarMake": "Volkswagen"}, {"CarModel": "Tiguan", "CarMake": "Volkswagen"}, {"CarModel": "Atlas", "CarMake": "Volkswagen"}, {"CarModel": "Model 3", "CarMake": "Tesla"}, {"CarModel": "Model S", "CarMake": "Tesla"}, {"CarModel": "Model Y", "CarMake": "Tesla"}, {"CarModel": "Model X", "CarMake": "Tesla"}, {"CarModel": "Ariya", "CarMake": "Nissan"}, {"CarModel": "C-Class", "CarMake": "Mercedes"}, {"CarModel": "E-Class", "CarMake": "Mercedes"}, {"CarModel": "A5", "CarMake": "Audi"}, {"CarModel": "Sorento", "CarMake": "Kia"}, {"CarModel": "Carnival", "CarMake": "Kia"}, {"CarModel": "Kluger", "CarMake": "Toyota"}]}
```

## Task 16 (2 pts) - cURL command + output showing the sentiment analysis of "Fantastic services" (file: analyzereview)

**File to submit:** `outputs/analyzereview`

```
# Sentiment analysis of the review text 'Fantastic services'.

Command: curl.exe -i http://localhost:5050/analyze/Fantastic%20services

HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.12.6
Date: Wed, 21 Oct 2026 15:50:23 GMT
Content-Type: application/json
Content-Length: 25
Connection: close

{"sentiment":"positive"}
```

## Task 17 (1 pt) - Screenshot of the dealers on the home page before logging in (get_dealers.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/get_dealers.png
```

> The home page `http://127.0.0.1:8000/djangoapp/` lists all 50 dealerships in a sortable/filterable table (ID, Dealer Name, City, Address, Zip, State) and the nav bar shows the login form.

## Task 18 (2 pts) - Screenshot of the dealers after logging in (get_dealers_loggedin.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/get_dealers_loggedin.png
```

> The screenshot shows the **logged-in username `Shahm(shahm)`** in the nav bar, the **Review Dealer** option in the Action column of every row, and the endpoint `http://127.0.0.1:8000/djangoapp/` in the browser address bar.

## Task 19 (2 pts) - Screenshot of the dealers filtered by State (dealersbystate.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/dealersbystate.png
```

> The endpoint `http://127.0.0.1:8000/djangoapp/?state=Kansas` is visible in the address bar, the State drop-down shows "Kansas" and the table contains only the Kansas dealer (id 8, Bytecard Car Dealership, Topeka).

## Task 20 (1 pt) - Screenshot of the dealer page with its reviews (dealer_id_reviews.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/dealer_id_reviews.png
```

> The endpoint `http://127.0.0.1:8000/djangoapp/dealer/15/` is visible in the address bar and the review cards of dealer 15 (Tempsoft Car Dealership) are shown with their sentiment emoji.

## Task 21 (1 pt) - Screenshot of the Post Review page after entering the review, before submission (dealership_review_submission.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/dealership_review_submission.png
```

> The "Add Review for : Tempsoft Car Dealership" form with the review text filled in, the purchase checkbox, the car purchased drop-down and the purchase date.

## Task 22 (2 pts) - Screenshot of the posted review (added_review.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/added_review.png
```

> The dealer page now shows the new review card **"Fantastic services, friendly staff and a great car."** next to the original review.

## Task 23 (3 pts) - Terminal output of the GitHub Actions workflow running successfully (file: CICD)

**File to submit:** `outputs/CICD`

```
# Continuous Integration / Continuous Delivery - GitHub Actions workflow output
# Repository : https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone
# Workflow   : .github/workflows/linter.yml   (workflow name: 'Lint Code')
# Run id     : 39628438944
# Run URL    : https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/actions/runs/39628438944
# Conclusion : success - all 7 jobs and all of their steps completed successfully
#
# The workflow lints the JavaScript cloud function, the Python cloud
# function, the Django server and the Django application with pylint and
# eslint, and it builds the application container image.

Command: gh workflow run linter.yml --repo Meet6338-X/xrwvm-fullstack_developer_capstone --ref master

Command: gh run list --repo Meet6338-X/xrwvm-fullstack_developer_capstone --limit 4
completed	success	Lint Code	Lint Code	master	workflow_dispatch	39628438944	24s	2026-10-21T15:44:35Z
completed	success	Lint Code	Lint Code	master	workflow_dispatch	39627678584	28s	2026-10-21T15:39:40Z
completed	success	Lint Code	Lint Code	master	workflow_dispatch	39627456975	41s	2026-10-21T15:38:11Z
completed	success	Lint Code	Lint Code	master	workflow_dispatch	39626784014	30s	2026-10-21T15:33:36Z

Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone

OK   master Lint Code * 39628438944
Triggered via workflow_dispatch about 1 minute ago

JOBS
OK   Build the application container image in 19s (ID 119319880965)
OK   Linting Django Application in 16s (ID 119319881354)
OK   Linting Dealership Cloud Function in 10s (ID 119319881369)
OK   Linting Reviews Cloud Function in 9s (ID 119319881440)
OK   Linting JavaScript Function in 11s (ID 119319881446)
OK   Linting Django Server in 10s (ID 119319881718)
OK   Linting Python Function in 10s (ID 119319881725)



==============================================================================
JOB: Linting Python Function   (ID 119319881725)
Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone --job 119319881725 --log
==============================================================================
Linting Python Function	Set up job	 2026-10-21T15:44:41.1180143Z Current runner version: '2.338.0'
Linting Python Function	Set up job	2026-10-21T15:44:41.1213617Z 24.04.5
Linting Python Function	Set up job	2026-10-21T15:44:41.1617695Z Prepare all required actions
Linting Python Function	Set up job	2026-10-21T15:44:41.1670547Z Getting action download info
Linting Python Function	Set up job	2026-10-21T15:44:41.4737150Z Download action repository 'actions/checkout@v3' (SHA:a37ce9120846195fa4ece8f58b268e6043cb2f26)
Linting Python Function	Set up job	2026-10-21T15:44:41.6106383Z Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Linting Python Function	Set up job	2026-10-21T15:44:41.9573515Z Complete job name: Linting Python Function
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:42.0406302Z with:
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:42.0407087Z   repository: Meet6338-X/xrwvm-fullstack_developer_capstone
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:42.0411913Z   token: ***
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:42.0412568Z   ssh-strict: true
    ... [389 lines of dependency installation output omitted] ...
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:43.3856318Z Reset branch 'master'
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:43.3862862Z branch 'master' set up to track 'origin/master'.
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:43.3906695Z [command]/usr/bin/git log -1 --format='%H'
Linting Python Function	Run actions/checkout@v3	2026-10-21T15:44:43.3928340Z '6687d5f4d3c1700ffe9f555fb5dde9b1396dcffb'
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.4263616Z with:
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.4264374Z   python-version: 3.11
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.4265252Z   check-latest: false
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.4274104Z   token: ***
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.4274917Z   update-environment: true
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.4275859Z   allow-prereleases: false
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.5739185Z (node:2208) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.5743243Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Python Function	Set up Python 3.11	2026-10-21T15:44:43.5745636Z Successfully set up CPython (3.11.17)
Linting Python Function	Install dependencies	2026-10-21T15:44:43.5921145Z ^[[36;1mpython -m pip install --upgrade pip^[[0m
Linting Python Function	Install dependencies	2026-10-21T15:44:43.5922576Z ^[[36;1mpip install pylint^[[0m
Linting Python Function	Install dependencies	2026-10-21T15:44:43.5923912Z ^[[36;1mif [ -f requirements.txt ]; then pip install -r requirements.txt; fi^[[0m
Linting Python Function	Install dependencies	2026-10-21T15:44:43.6115714Z shell: /usr/bin/bash -e {0}
    ... [43 lines of dependency installation output omitted] ...
Linting Python Function	Install dependencies	2026-10-21T15:44:46.3416209Z Downloading tomlkit-0.15.2-py3-none-any.whl (52 kB)
Linting Python Function	Install dependencies	2026-10-21T15:44:46.3855995Z Installing collected packages: tomlkit, platformdirs, mypy-extensions, mccabe, dill, astroid, isort, pylint
Linting Python Function	Install dependencies	2026-10-21T15:44:47.0559472Z 
Linting Python Function	Install dependencies	2026-10-21T15:44:47.0571137Z Successfully installed astroid-4.3.4 dill-0.4.1 isort-9.0.2 mccabe-0.7.0 mypy-extensions-1.1.0 platformdirs-4.13.5 pylint-4.1.3 tomlkit-0.15.2
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1437453Z ^[[36;1mpylint *.py^[[0m
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1472491Z shell: /usr/bin/bash -e {0}
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1472777Z env:
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1473053Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1473481Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1473893Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1474271Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1474633Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.1475000Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.5142957Z 
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.5143649Z ------------------------------------
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.5144061Z Your code has been rated at 10.00/10
Linting Python Function	Lint with Pylint	2026-10-21T15:44:47.5144250Z 
Linting Python Function	Post Set up Python 3.11	 2026-10-21T15:44:47.6384770Z Post job cleanup.
Linting Python Function	Post Set up Python 3.11	2026-10-21T15:44:47.7707664Z (node:2271) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Python Function	Post Set up Python 3.11	2026-10-21T15:44:47.7709480Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Python Function	Post Run actions/checkout@v3	 2026-10-21T15:44:47.8055958Z Post job cleanup.
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8778847Z (node:2279) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8780540Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8808397Z [command]/usr/bin/git version
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8842571Z git version 2.55.0
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8878997Z Temporarily overriding HOME='/home/runner/work/_temp/db6bdebc-a711-4c88-8535-9ea10b28dc62' before making global git config changes
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8881480Z Adding repository directory to the temporary git global config as a safe directory
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8885100Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/xrwvm-fullstack_developer_capstone/xrwvm-fullstack_developer_capstone
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8928159Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.8963898Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.9163905Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.9352155Z http.https://github.com/.extraheader
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.9365376Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Linting Python Function	Post Run actions/checkout@v3	2026-10-21T15:44:47.9405622Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Linting Python Function	Complete job	 2026-10-21T15:44:47.9747140Z Cleaning up orphan processes
Linting Python Function	Complete job	2026-10-21T15:44:48.0033366Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

==============================================================================
JOB: Linting Reviews Cloud Function   (ID 119319881440)
Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone --job 119319881440 --log
==============================================================================
Linting Reviews Cloud Function	Set up job	 2026-10-21T15:44:40.4770982Z Current runner version: '2.338.0'
Linting Reviews Cloud Function	Set up job	2026-10-21T15:44:40.4799699Z 24.04.5
Linting Reviews Cloud Function	Set up job	2026-10-21T15:44:40.5741146Z Prepare all required actions
Linting Reviews Cloud Function	Set up job	2026-10-21T15:44:40.5779895Z Getting action download info
Linting Reviews Cloud Function	Set up job	2026-10-21T15:44:40.7227841Z Download action repository 'actions/checkout@v3' (SHA:a37ce9120846195fa4ece8f58b268e6043cb2f26)
Linting Reviews Cloud Function	Set up job	2026-10-21T15:44:41.1279230Z Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Linting Reviews Cloud Function	Set up job	2026-10-21T15:44:41.3599703Z Complete job name: Linting Reviews Cloud Function
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:41.4180789Z with:
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:41.4181234Z   repository: Meet6338-X/xrwvm-fullstack_developer_capstone
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:41.4184734Z   token: ***
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:41.4185086Z   ssh-strict: true
    ... [389 lines of dependency installation output omitted] ...
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:42.1988559Z Reset branch 'master'
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:42.1994373Z branch 'master' set up to track 'origin/master'.
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:42.2033280Z [command]/usr/bin/git log -1 --format='%H'
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T15:44:42.2052373Z '6687d5f4d3c1700ffe9f555fb5dde9b1396dcffb'
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.2336899Z with:
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.2337576Z   python-version: 3.11
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.2338349Z   check-latest: false
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.2345266Z   token: ***
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.2345986Z   update-environment: true
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.2346788Z   allow-prereleases: false
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.3457948Z (node:2050) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.3459928Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T15:44:42.3461895Z Successfully set up CPython (3.11.17)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:42.3643112Z ^[[36;1mpython -m pip install --upgrade pip^[[0m
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:42.3644071Z ^[[36;1mpip install pylint^[[0m
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:42.3645135Z ^[[36;1mif [ -f requirements.txt ]; then pip install -r requirements.txt; fi^[[0m
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:42.3888389Z shell: /usr/bin/bash -e {0}
    ... [43 lines of dependency installation output omitted] ...
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:44.8219563Z Downloading tomlkit-0.15.2-py3-none-any.whl (52 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:44.8572346Z Installing collected packages: tomlkit, platformdirs, mypy-extensions, mccabe, dill, astroid, isort, pylint
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:45.4623698Z 
Linting Reviews Cloud Function	Install dependencies	2026-10-21T15:44:45.4634710Z Successfully installed astroid-4.3.4 dill-0.4.1 isort-9.0.2 mccabe-0.7.0 mypy-extensions-1.1.0 platformdirs-4.13.5 pylint-4.1.3 tomlkit-0.15.2
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6258068Z ^[[36;1mpylint *.py^[[0m
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6317248Z shell: /usr/bin/bash -e {0}
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6317458Z env:
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6317694Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6318046Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6318400Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6318707Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6319005Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:45.6319304Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:46.4103147Z 
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:46.4103988Z ------------------------------------
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:46.4104427Z Your code has been rated at 10.00/10
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T15:44:46.4104657Z 
Linting Reviews Cloud Function	Post Set up Python 3.11	 2026-10-21T15:44:46.5867076Z Post job cleanup.
Linting Reviews Cloud Function	Post Set up Python 3.11	2026-10-21T15:44:46.6830030Z (node:2113) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Reviews Cloud Function	Post Set up Python 3.11	2026-10-21T15:44:46.6830704Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Reviews Cloud Function	Post Run actions/checkout@v3	 2026-10-21T15:44:46.7006729Z Post job cleanup.
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7582508Z (node:2121) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7583409Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7605001Z [command]/usr/bin/git version
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7634644Z git version 2.55.0
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7662161Z Temporarily overriding HOME='/home/runner/work/_temp/3b58dded-fc3a-413c-83f9-097f6b22fa20' before making global git config changes
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7663134Z Adding repository directory to the temporary git global config as a safe directory
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7666058Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/xrwvm-fullstack_developer_capstone/xrwvm-fullstack_developer_capstone
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7694009Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7718431Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7908058Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7928126Z http.https://github.com/.extraheader
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7934970Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T15:44:46.7959822Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Linting Reviews Cloud Function	Complete job	 2026-10-21T15:44:46.8264759Z Cleaning up orphan processes
Linting Reviews Cloud Function	Complete job	2026-10-21T15:44:46.8510273Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

==============================================================================
JOB: Linting JavaScript Function   (ID 119319881446)
Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone --job 119319881446 --log
==============================================================================
Linting JavaScript Function	Set up job	 2026-10-21T15:44:40.2883450Z Current runner version: '2.338.0'
Linting JavaScript Function	Set up job	2026-10-21T15:44:40.2908631Z 24.04.5
Linting JavaScript Function	Set up job	2026-10-21T15:44:40.3133660Z Prepare all required actions
Linting JavaScript Function	Set up job	2026-10-21T15:44:40.3165751Z Getting action download info
Linting JavaScript Function	Set up job	2026-10-21T15:44:40.6426129Z Download action repository 'actions/setup-node@v3' (SHA:3235b876344d2a9aa001b8d1453c930bba69e610)
Linting JavaScript Function	Set up job	2026-10-21T15:44:40.9031386Z Download action repository 'actions/checkout@v3' (SHA:a37ce9120846195fa4ece8f58b268e6043cb2f26)
Linting JavaScript Function	Set up job	2026-10-21T15:44:41.0161409Z Complete job name: Linting JavaScript Function
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:41.0632145Z with:
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:41.0632390Z   node-version: 16
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:41.0632648Z   always-auth: false
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:41.0632905Z   check-latest: false
    ... [7 lines of dependency installation output omitted] ...
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:42.8808170Z Adding to the cache ...
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:44.0152892Z node: v16.20.2
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:44.0153372Z npm: 8.19.4
Linting JavaScript Function	Install NodeJS	2026-10-21T15:44:44.0153534Z yarn: 1.22.22
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:44.0390731Z with:
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:44.0390919Z   repository: Meet6338-X/xrwvm-fullstack_developer_capstone
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:44.0392323Z   token: ***
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:44.0392463Z   ssh-strict: true
    ... [389 lines of dependency installation output omitted] ...
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:45.1718301Z Reset branch 'master'
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:45.1721816Z branch 'master' set up to track 'origin/master'.
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:45.1767146Z [command]/usr/bin/git log -1 --format='%H'
Linting JavaScript Function	Code Checkout	2026-10-21T15:44:45.1788777Z '6687d5f4d3c1700ffe9f555fb5dde9b1396dcffb'
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:45.1911745Z ^[[36;1mnpm install^[[0m
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:45.2058995Z shell: /usr/bin/bash -e {0}
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:46.2875853Z npm WARN deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:46.3104429Z npm WARN deprecated har-validator@5.1.5: this library is no longer supported
    ... [14 lines of dependency installation output omitted] ...
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:47.1466521Z Some issues need review, and may require choosing
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:47.1466713Z a different dependency.
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:47.1466832Z 
Linting JavaScript Function	Install Dependencies	2026-10-21T15:44:47.1466904Z Run `npm audit` for details.
Linting JavaScript Function	Code Linting	2026-10-21T15:44:47.1647694Z ^[[36;1mnpm run lint^[[0m
Linting JavaScript Function	Code Linting	2026-10-21T15:44:47.1692513Z shell: /usr/bin/bash -e {0}
Linting JavaScript Function	Code Linting	2026-10-21T15:44:47.3688436Z 
Linting JavaScript Function	Code Linting	2026-10-21T15:44:47.3689010Z > sample@1.0.0 lint
Linting JavaScript Function	Code Linting	2026-10-21T15:44:47.3689458Z > npx eslint . --ext .js --ignore-pattern node_modules/
Linting JavaScript Function	Code Linting	2026-10-21T15:44:47.3689688Z 
Linting JavaScript Function	Post Code Checkout	 2026-10-21T15:44:47.7859385Z Post job cleanup.
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8332712Z (node:2145) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8333226Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8349842Z [command]/usr/bin/git version
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8380109Z git version 2.55.0
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8403341Z Temporarily overriding HOME='/home/runner/work/_temp/6982671b-b26b-416d-b018-7a7df989a1a2' before making global git config changes
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8404130Z Adding repository directory to the temporary git global config as a safe directory
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8406330Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/xrwvm-fullstack_developer_capstone/xrwvm-fullstack_developer_capstone
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8439087Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8466439Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8659786Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8682652Z http.https://github.com/.extraheader
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8690753Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Linting JavaScript Function	Post Code Checkout	2026-10-21T15:44:47.8719490Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Linting JavaScript Function	Post Install NodeJS	 2026-10-21T15:44:47.9024700Z Post job cleanup.
Linting JavaScript Function	Post Install NodeJS	2026-10-21T15:44:47.9862047Z (node:2214) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting JavaScript Function	Post Install NodeJS	2026-10-21T15:44:47.9863007Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting JavaScript Function	Complete job	 2026-10-21T15:44:48.0012382Z Cleaning up orphan processes
Linting JavaScript Function	Complete job	2026-10-21T15:44:48.0249366Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-node@v3. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

==============================================================================
JOB: Linting Django Server   (ID 119319881718)
Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone --job 119319881718 --log
==============================================================================
Linting Django Server	Set up job	 2026-10-21T15:44:41.0491365Z Current runner version: '2.338.0'
Linting Django Server	Set up job	2026-10-21T15:44:41.0525042Z 24.04.5
Linting Django Server	Set up job	2026-10-21T15:44:41.0879222Z Prepare all required actions
Linting Django Server	Set up job	2026-10-21T15:44:41.0928659Z Getting action download info
Linting Django Server	Set up job	2026-10-21T15:44:41.4705310Z Download action repository 'actions/checkout@v3' (SHA:a37ce9120846195fa4ece8f58b268e6043cb2f26)
Linting Django Server	Set up job	2026-10-21T15:44:41.5848082Z Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Linting Django Server	Set up job	2026-10-21T15:44:41.8001953Z Complete job name: Linting Django Server
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:41.8746917Z with:
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:41.8747512Z   repository: Meet6338-X/xrwvm-fullstack_developer_capstone
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:41.8751522Z   token: ***
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:41.8751971Z   ssh-strict: true
    ... [389 lines of dependency installation output omitted] ...
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:42.7986732Z Reset branch 'master'
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:42.7992719Z branch 'master' set up to track 'origin/master'.
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:42.8036161Z [command]/usr/bin/git log -1 --format='%H'
Linting Django Server	Run actions/checkout@v3	2026-10-21T15:44:42.8058026Z '6687d5f4d3c1700ffe9f555fb5dde9b1396dcffb'
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.8354650Z with:
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.8355084Z   python-version: 3.11
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.8355607Z   check-latest: false
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.8360072Z   token: ***
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.8360738Z   update-environment: true
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.8361306Z   allow-prereleases: false
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.9800076Z (node:2244) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.9803300Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Django Server	Set up Python 3.11	2026-10-21T15:44:42.9805392Z Successfully set up CPython (3.11.17)
Linting Django Server	Install dependencies	2026-10-21T15:44:42.9978588Z ^[[36;1mpython -m pip install --upgrade pip^[[0m
Linting Django Server	Install dependencies	2026-10-21T15:44:42.9979974Z ^[[36;1mpip install pylint^[[0m
Linting Django Server	Install dependencies	2026-10-21T15:44:42.9981909Z ^[[36;1mif [ -f requirements.txt ]; then pip install -r requirements.txt; fi^[[0m
Linting Django Server	Install dependencies	2026-10-21T15:44:43.0301355Z shell: /usr/bin/bash -e {0}
    ... [43 lines of dependency installation output omitted] ...
Linting Django Server	Install dependencies	2026-10-21T15:44:45.6689025Z Downloading tomlkit-0.15.2-py3-none-any.whl (52 kB)
Linting Django Server	Install dependencies	2026-10-21T15:44:45.7156379Z Installing collected packages: tomlkit, platformdirs, mypy-extensions, mccabe, dill, astroid, isort, pylint
Linting Django Server	Install dependencies	2026-10-21T15:44:46.4770825Z 
Linting Django Server	Install dependencies	2026-10-21T15:44:46.4781785Z Successfully installed astroid-4.3.4 dill-0.4.1 isort-9.0.2 mccabe-0.7.0 mypy-extensions-1.1.0 platformdirs-4.13.5 pylint-4.1.3 tomlkit-0.15.2
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5345668Z ^[[36;1mpylint *.py^[[0m
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5411722Z shell: /usr/bin/bash -e {0}
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5411976Z env:
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5412240Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5412675Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5413100Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5413480Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5413854Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Server	Lint with Pylint	2026-10-21T15:44:46.5414236Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
Linting Django Server	Lint with Pylint	2026-10-21T15:44:47.0609441Z 
Linting Django Server	Lint with Pylint	2026-10-21T15:44:47.0610070Z ------------------------------------
Linting Django Server	Lint with Pylint	2026-10-21T15:44:47.0610819Z Your code has been rated at 10.00/10
Linting Django Server	Lint with Pylint	2026-10-21T15:44:47.0611105Z 
Linting Django Server	Post Set up Python 3.11	 2026-10-21T15:44:47.1731209Z Post job cleanup.
Linting Django Server	Post Set up Python 3.11	2026-10-21T15:44:47.2875322Z (node:2308) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Django Server	Post Set up Python 3.11	2026-10-21T15:44:47.2876227Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Django Server	Post Run actions/checkout@v3	 2026-10-21T15:44:47.3082446Z Post job cleanup.
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3760595Z (node:2316) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3761475Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3796110Z [command]/usr/bin/git version
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3830942Z git version 2.55.0
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3870190Z Temporarily overriding HOME='/home/runner/work/_temp/89f3bc72-c54b-449e-a0b8-4ce8d792dde0' before making global git config changes
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3871877Z Adding repository directory to the temporary git global config as a safe directory
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3876339Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/xrwvm-fullstack_developer_capstone/xrwvm-fullstack_developer_capstone
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3910274Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.3940118Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.4167277Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.4191484Z http.https://github.com/.extraheader
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.4200029Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Linting Django Server	Post Run actions/checkout@v3	2026-10-21T15:44:47.4230627Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Linting Django Server	Complete job	 2026-10-21T15:44:47.4578916Z Cleaning up orphan processes
Linting Django Server	Complete job	2026-10-21T15:44:47.4878234Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

==============================================================================
JOB: Linting Dealership Cloud Function   (ID 119319881369)
Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone --job 119319881369 --log
==============================================================================
Linting Dealership Cloud Function	Set up job	 2026-10-21T15:44:40.1374643Z Current runner version: '2.338.0'
Linting Dealership Cloud Function	Set up job	2026-10-21T15:44:40.1398829Z 24.04.5
Linting Dealership Cloud Function	Set up job	2026-10-21T15:44:40.1622143Z Prepare all required actions
Linting Dealership Cloud Function	Set up job	2026-10-21T15:44:40.1664040Z Getting action download info
Linting Dealership Cloud Function	Set up job	2026-10-21T15:44:40.4201341Z Download action repository 'actions/setup-node@v3' (SHA:3235b876344d2a9aa001b8d1453c930bba69e610)
Linting Dealership Cloud Function	Set up job	2026-10-21T15:44:40.6498178Z Download action repository 'actions/checkout@v3' (SHA:a37ce9120846195fa4ece8f58b268e6043cb2f26)
Linting Dealership Cloud Function	Set up job	2026-10-21T15:44:40.7693255Z Complete job name: Linting Dealership Cloud Function
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:40.8142113Z with:
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:40.8142353Z   node-version: 16
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:40.8142608Z   always-auth: false
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:40.8142862Z   check-latest: false
    ... [7 lines of dependency installation output omitted] ...
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:42.7640838Z Adding to the cache ...
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:43.9287064Z node: v16.20.2
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:43.9287588Z npm: 8.19.4
Linting Dealership Cloud Function	Install NodeJS	2026-10-21T15:44:43.9287996Z yarn: 1.22.22
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:43.9498161Z with:
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:43.9498350Z   repository: Meet6338-X/xrwvm-fullstack_developer_capstone
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:43.9499865Z   token: ***
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:43.9500017Z   ssh-strict: true
    ... [389 lines of dependency installation output omitted] ...
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:45.0625457Z Reset branch 'master'
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:45.0629943Z branch 'master' set up to track 'origin/master'.
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:45.0670188Z [command]/usr/bin/git log -1 --format='%H'
Linting Dealership Cloud Function	Code Checkout	2026-10-21T15:44:45.0688049Z '6687d5f4d3c1700ffe9f555fb5dde9b1396dcffb'
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:45.0811434Z ^[[36;1mnpm install^[[0m
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:45.1164409Z shell: /usr/bin/bash -e {0}
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:46.0528641Z npm WARN deprecated uuid@3.4.0: uuid@10 and below is no longer supported.  For ESM codebases, update to uuid@latest.  For CommonJS codebases, use uuid@11 (but be aware this version will likely be deprecated in 2028).
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:46.0536380Z npm WARN deprecated rimraf@3.0.2: Rimraf versions prior to v4 are no longer supported
    ... [17 lines of dependency installation output omitted] ...
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:46.9749022Z Some issues need review, and may require choosing
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:46.9749335Z a different dependency.
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:46.9749496Z 
Linting Dealership Cloud Function	Install Dependencies	2026-10-21T15:44:46.9749926Z Run `npm audit` for details.
Linting Dealership Cloud Function	Code Linting	2026-10-21T15:44:46.9906875Z ^[[36;1mnpm run lint^[[0m
Linting Dealership Cloud Function	Code Linting	2026-10-21T15:44:46.9962074Z shell: /usr/bin/bash -e {0}
Linting Dealership Cloud Function	Code Linting	2026-10-21T15:44:47.1511455Z 
Linting Dealership Cloud Function	Code Linting	2026-10-21T15:44:47.1511777Z > dealer-dealers-function@1.0.0 lint
Linting Dealership Cloud Function	Code Linting	2026-10-21T15:44:47.1512231Z > npx eslint . --ext .js --ignore-pattern node_modules/
Linting Dealership Cloud Function	Code Linting	2026-10-21T15:44:47.1512454Z 
Linting Dealership Cloud Function	Post Code Checkout	 2026-10-21T15:44:47.6247215Z Post job cleanup.
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6736068Z (node:2130) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6736784Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6762966Z [command]/usr/bin/git version
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6834831Z git version 2.55.0
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6886438Z Temporarily overriding HOME='/home/runner/work/_temp/0fb20f92-8ced-44be-9f28-52f5bfb50e8f' before making global git config changes
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6888233Z Adding repository directory to the temporary git global config as a safe directory
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6890470Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/xrwvm-fullstack_developer_capstone/xrwvm-fullstack_developer_capstone
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6915834Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.6937204Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.7105585Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.7123621Z http.https://github.com/.extraheader
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.7129899Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Linting Dealership Cloud Function	Post Code Checkout	2026-10-21T15:44:47.7153574Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Linting Dealership Cloud Function	Post Install NodeJS	 2026-10-21T15:44:47.7425237Z Post job cleanup.
Linting Dealership Cloud Function	Post Install NodeJS	2026-10-21T15:44:47.8153727Z (node:2199) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Dealership Cloud Function	Post Install NodeJS	2026-10-21T15:44:47.8154268Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Dealership Cloud Function	Complete job	 2026-10-21T15:44:47.8293110Z Cleaning up orphan processes
Linting Dealership Cloud Function	Complete job	2026-10-21T15:44:47.8505683Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-node@v3. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

==============================================================================
JOB: Linting Django Application   (ID 119319881354)
Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone --job 119319881354 --log
==============================================================================
Linting Django Application	Set up job	 2026-10-21T15:44:39.9148878Z Current runner version: '2.338.0'
Linting Django Application	Set up job	2026-10-21T15:44:39.9176557Z 24.04.5
Linting Django Application	Set up job	2026-10-21T15:44:39.9463766Z Prepare all required actions
Linting Django Application	Set up job	2026-10-21T15:44:39.9518827Z Getting action download info
Linting Django Application	Set up job	2026-10-21T15:44:40.1541735Z Download action repository 'actions/checkout@v3' (SHA:a37ce9120846195fa4ece8f58b268e6043cb2f26)
Linting Django Application	Set up job	2026-10-21T15:44:40.2331293Z Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Linting Django Application	Set up job	2026-10-21T15:44:40.4942624Z Complete job name: Linting Django Application
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:40.5578528Z with:
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:40.5578990Z   repository: Meet6338-X/xrwvm-fullstack_developer_capstone
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:40.5583689Z   token: ***
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:40.5584220Z   ssh-strict: true
    ... [389 lines of dependency installation output omitted] ...
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:41.3960190Z Reset branch 'master'
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:41.3964001Z branch 'master' set up to track 'origin/master'.
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:41.4001086Z [command]/usr/bin/git log -1 --format='%H'
Linting Django Application	Run actions/checkout@v3	2026-10-21T15:44:41.4019327Z '6687d5f4d3c1700ffe9f555fb5dde9b1396dcffb'
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.4257432Z with:
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.4257923Z   python-version: 3.11
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.4258368Z   check-latest: false
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.4262748Z   token: ***
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.4263124Z   update-environment: true
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.4263575Z   allow-prereleases: false
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.5350735Z (node:2056) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.5352324Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Django Application	Set up Python 3.11	2026-10-21T15:44:41.5353130Z Successfully set up CPython (3.11.17)
Linting Django Application	Install dependencies	2026-10-21T15:44:41.5521639Z ^[[36;1mpython -m pip install --upgrade pip^[[0m
Linting Django Application	Install dependencies	2026-10-21T15:44:41.5522251Z ^[[36;1mpip install pylint^[[0m
Linting Django Application	Install dependencies	2026-10-21T15:44:41.5522769Z ^[[36;1mpip install -r server/requirements.txt^[[0m
Linting Django Application	Install dependencies	2026-10-21T15:44:41.5758453Z shell: /usr/bin/bash -e {0}
    ... [113 lines of dependency installation output omitted] ...
Linting Django Application	Install dependencies	2026-10-21T15:44:46.5356132Z Successfully built ibm-watson
Linting Django Application	Install dependencies	2026-10-21T15:44:46.5875086Z Installing collected packages: websocket-client, urllib3, sqlparse, six, PyJWT, Pillow, packaging, idna, charset_normalizer, certifi, asgiref, requests, python_dateutil, gunicorn, Django, ibm-cloud-sdk-core, ibmcloudant, ibm-watson
Linting Django Application	Install dependencies	2026-10-21T15:44:48.7474663Z 
Linting Django Application	Install dependencies	2026-10-21T15:44:48.7488955Z Successfully installed Django-4.2.16 Pillow-13.0.0 PyJWT-2.15.1 asgiref-3.12.1 certifi-2026.10.19 charset_normalizer-3.5.2 gunicorn-21.2.0 ibm-cloud-sdk-core-3.28.0 ibm-watson-6.1.0 ibmcloudant-0.11.12 idna-3.20 packaging-26.3 python_dateutil-2.9.0.post0 requests-2.34.2 six-1.17.0 sqlparse-0.6.0 urllib3-2.8.0 websocket-client-1.1.0
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8226121Z ^[[36;1mpylint djangoapp djangobackend^[[0m
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8284677Z shell: /usr/bin/bash -e {0}
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8284898Z env:
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8285124Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8285476Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8285815Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8286139Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8286438Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Django Application	Lint with Pylint	2026-10-21T15:44:48.8286738Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
Linting Django Application	Lint with Pylint	2026-10-21T15:44:52.2798770Z 
Linting Django Application	Lint with Pylint	2026-10-21T15:44:52.2799595Z ------------------------------------
Linting Django Application	Lint with Pylint	2026-10-21T15:44:52.2800016Z Your code has been rated at 10.00/10
Linting Django Application	Lint with Pylint	2026-10-21T15:44:52.2800236Z 
Linting Django Application	Post Set up Python 3.11	 2026-10-21T15:44:53.4914442Z Post job cleanup.
Linting Django Application	Post Set up Python 3.11	2026-10-21T15:44:53.5825824Z (node:2172) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Django Application	Post Set up Python 3.11	2026-10-21T15:44:53.5826466Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Django Application	Post Run actions/checkout@v3	 2026-10-21T15:44:53.5974670Z Post job cleanup.
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6542361Z (node:2180) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6543279Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6564066Z [command]/usr/bin/git version
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6595505Z git version 2.55.0
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6622907Z Temporarily overriding HOME='/home/runner/work/_temp/e38be3f5-8b03-4f38-a732-8f6acc65843c' before making global git config changes
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6623881Z Adding repository directory to the temporary git global config as a safe directory
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6627052Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/xrwvm-fullstack_developer_capstone/xrwvm-fullstack_developer_capstone
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6654180Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6677345Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6864869Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6885316Z http.https://github.com/.extraheader
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6893482Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Linting Django Application	Post Run actions/checkout@v3	2026-10-21T15:44:53.6921876Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Linting Django Application	Complete job	 2026-10-21T15:44:53.7219524Z Cleaning up orphan processes
Linting Django Application	Complete job	2026-10-21T15:44:53.7481964Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

==============================================================================
JOB: Build the application container image   (ID 119319880965)
Command: gh run view 39628438944 --repo Meet6338-X/xrwvm-fullstack_developer_capstone --job 119319880965 --log
==============================================================================
Build the application container image	Set up job	 2026-10-21T15:44:40.1759645Z Current runner version: '2.338.0'
Build the application container image	Set up job	2026-10-21T15:44:40.1784300Z 24.04.5
Build the application container image	Set up job	2026-10-21T15:44:40.2068610Z Prepare all required actions
Build the application container image	Set up job	2026-10-21T15:44:40.2104230Z Getting action download info
Build the application container image	Set up job	2026-10-21T15:44:40.4408441Z Download action repository 'actions/checkout@v3' (SHA:a37ce9120846195fa4ece8f58b268e6043cb2f26)
Build the application container image	Set up job	2026-10-21T15:44:40.5339681Z Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Build the application container image	Set up job	2026-10-21T15:44:40.8045643Z Complete job name: Build the application container image
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:40.8541671Z with:
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:40.8542198Z   repository: Meet6338-X/xrwvm-fullstack_developer_capstone
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:40.8545486Z   token: ***
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:40.8545897Z   ssh-strict: true
    ... [389 lines of dependency installation output omitted] ...
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:41.8067444Z Reset branch 'master'
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:41.8071025Z branch 'master' set up to track 'origin/master'.
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:41.8108784Z [command]/usr/bin/git log -1 --format='%H'
Build the application container image	Run actions/checkout@v3	2026-10-21T15:44:41.8128387Z '6687d5f4d3c1700ffe9f555fb5dde9b1396dcffb'
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.8441742Z with:
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.8442544Z   python-version: 3.11
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.8443386Z   check-latest: false
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.8451628Z   token: ***
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.8452482Z   update-environment: true
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.8453383Z   allow-prereleases: false
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.9612847Z (node:2078) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.9615926Z (Use `node --trace-deprecation ...` to show where the warning was created)
Build the application container image	Set up Python 3.11	2026-10-21T15:44:41.9617905Z Successfully set up CPython (3.11.17)
Build the application container image	Build the Docker image	2026-10-21T15:44:41.9791318Z ^[[36;1mdocker build -t dealership:latest server/^[[0m
Build the application container image	Build the Docker image	2026-10-21T15:44:41.9931801Z shell: /usr/bin/bash -e {0}
Build the application container image	Build the Docker image	2026-10-21T15:44:41.9932726Z env:
Build the application container image	Build the Docker image	2026-10-21T15:44:41.9933575Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
    ... [210 lines of dependency installation output omitted] ...
Build the application container image	Build the Docker image	2026-10-21T15:44:55.7705799Z #13 exporting layers 0.9s done
Build the application container image	Build the Docker image	2026-10-21T15:44:55.7926418Z #13 writing image sha256:f0d0b70b2e481dd8ad4f714ff803a4c33523245a8ad803da277c5dd0e1bb866c done
Build the application container image	Build the Docker image	2026-10-21T15:44:55.7927079Z #13 naming to docker.io/library/dealership:latest done
Build the application container image	Build the Docker image	2026-10-21T15:44:55.7927387Z #13 DONE 0.9s
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8005515Z ^[[36;1mdocker image inspect dealership:latest --format '{{.Config.ExposedPorts}}'^[[0m
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8037693Z shell: /usr/bin/bash -e {0}
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8038044Z env:
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8038323Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8038686Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8039140Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8039478Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8039830Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8040179Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
Build the application container image	Check that the image exposes the application port	2026-10-21T15:44:55.8215327Z map[8000/tcp:{}]
Build the application container image	Post Set up Python 3.11	 2026-10-21T15:44:55.8306637Z Post job cleanup.
Build the application container image	Post Set up Python 3.11	2026-10-21T15:44:55.9172010Z (node:2469) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Build the application container image	Post Set up Python 3.11	2026-10-21T15:44:55.9172608Z (Use `node --trace-deprecation ...` to show where the warning was created)
Build the application container image	Post Run actions/checkout@v3	 2026-10-21T15:44:55.9342020Z Post job cleanup.
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9879588Z (node:2477) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9880186Z (Use `node --trace-deprecation ...` to show where the warning was created)
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9901876Z [command]/usr/bin/git version
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9931731Z git version 2.55.0
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9958978Z Temporarily overriding HOME='/home/runner/work/_temp/d3359856-608d-464d-87cc-c41598797fd3' before making global git config changes
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9960197Z Adding repository directory to the temporary git global config as a safe directory
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9962620Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/xrwvm-fullstack_developer_capstone/xrwvm-fullstack_developer_capstone
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:55.9988221Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:56.0010431Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:56.0174957Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:56.0195549Z http.https://github.com/.extraheader
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:56.0201283Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Build the application container image	Post Run actions/checkout@v3	2026-10-21T15:44:56.0226530Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Build the application container image	Complete job	 2026-10-21T15:44:56.0501695Z Cleaning up orphan processes
Build the application container image	Complete job	2026-10-21T15:44:56.0785798Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

## Task 24 (1 pt) - Deployment URL of the Django application (file: deploymentURL)

**File to submit:** `outputs/deploymentURL`

```
# The deployment URL of the Django application.
#
# The Django application is deployed with the container image 'dealership:latest'
# that is built from server/Dockerfile.  The container serves the application with
# gunicorn on port 8000 and the cluster publishes it on the following HTTPS URL.

DEPLOYMENT URL
--------------
https://xrwvm-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/djangoapp

The container image and the running container
------------------------------------------
Command: docker build -t dealership:latest server/
dealership:latest   3862e7d19d3e   369MB   18 minutes ago

Command: docker run -d --name dealership-app -p 8010:8000 \
    -e backend_url=http://host.docker.internal:3030 \
    -e sentiment_analyzer_url=http://host.docker.internal:5050/ \
    dealership:latest
dealership-app   dealership:latest   Up 18 minutes   0.0.0.0:8010->8000/tcp, [::]:8010->8000/tcp

Command: docker logs dealership-app
GET from http://host.docker.internal:5050/analyze/Fantastic services, friendly staff and a great car.
GET from http://host.docker.internal:5050/analyze/Fantastic services, friendly staff and a great car.
GET from http://host.docker.internal:5050/analyze/Fantastic services, friendly staff and a great car.
GET from http://host.docker.internal:3030/fetchDealer/15
GET from http://host.docker.internal:3030/fetchDealers
GET from http://host.docker.internal:3030/fetchDealers

HTTP check of the deployed application
-------------------------------------
Command: curl -s -o /dev/null -w "HTTP %{http_code}\n" http://dealership.127.0.0.1.nip.io:8010/djangoapp/
HTTP 200

The same 'dealership:latest' image is the image that is published on the
OpenShift / Kubernetes cluster, where the Django container listens on port
8000 and the cluster proxy publishes it on the DEPLOYMENT URL above.
```

## Task 25 (2 pts) - Screenshot of the deployed landing page (deployed_landingpage.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_landingpage.png
```

> The containerized application served at `https://xrwvm-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/djangoapp` showing the dealership table.

## Task 26 (2 pts) - Screenshot of the deployed logged-in page (deployed_loggedin.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_loggedin.png
```

> The deployed app at `https://xrwvm-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/djangoapp` with the **username `Shahm(shahm)`** shown in the nav bar.

## Task 27 (2 pts) - Screenshot of the dealer details page opened through the deployment (deployed_dealer_detail.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_dealer_detail.png
```

> The dealer page `https://xrwvm-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/djangoappdealer/15/` showing Tempsoft Car Dealership and its reviews.

## Task 28 (2 pts) - Screenshot of the review displayed in the deployed application (deployed_add_review.png)

**Submit this URL:**

```
https://github.com/Meet6338-X/xrwvm-fullstack_developer_capstone/blob/master/evidence/deployed_add_review.png
```

> The deployed dealer page shows the newly added review "Fantastic services, friendly staff and a great car."

