# PASTE ANSWERS - Best Cars Dealership Capstone (28 tasks)

Everything below can be copied straight into the Coursera answer boxes.

### Task 1 (1 pt) - Public GitHub URL of the README.md file that contains the Project name details

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/README.md
```

### Task 2 (1 pt) - Terminal output showing the Django server running (file: django_server)

```
# The Django development server for the Best Cars Dealership app.
theia@theia-devshahm:/home/project/server$ python manage.py runserver 8000
Performing system checks...

System check identified no issues (0 silenced).
October 21, 2026 - 13:19:01
Django version 4.2.16, using settings 'djangobackend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

GET from http://localhost:3000/dealerships/get 
With status 200 
JSON RESULT: 50 dealership document(s) retrieved
[21/Oct/2026 13:19:09] "GET /djangoapp/ HTTP/1.1" 200 31677
[21/Oct/2026 13:19:09] "GET /djangoapp/about HTTP/1.1" 200 4801
```

### Task 3 (3 pts) - Public GitHub URL of server/frontend/static/About.html (updated About Us page)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/server/frontend/static/About.html
```

### Task 4 (2 pts) - Public GitHub URL of server/frontend/static/Contact.html (Contact Us page)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/server/frontend/static/Contact.html
```

### Task 5 (2 pts) - cURL command + output for a login operation (file: loginuser)

```
# Log in to the Django application with a valid username and password.

theia@theia-devshahm:/home/project/server$ curl -s -i -c cookies.txt -X POST -d "username=shahm&psw=Shahm@2024" http://localhost:8000/djangoapp/login
HTTP/1.1 302 Found
Date: Wed, 21 Oct 2026 07:49:13 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: text/html; charset=utf-8
Location: /djangoapp/
X-Frame-Options: DENY
Content-Length: 0
Vary: Cookie
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
Set-Cookie:  sessionid=fhr7pfzy2kgldqm3uea9yakgqlwxcx2r; expires=Wed, 04 Nov 2026 07:49:13 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax
```

### Task 6 (2 pts) - cURL command + output for a logout operation (file: logoutuser)

```
# Log out the user that was logged in by the previous request.

theia@theia-devshahm:/home/project/server$ curl -s -i -b cookies.txt -c cookies.txt -X GET http://localhost:8000/djangoapp/logout
HTTP/1.1 302 Found
Date: Wed, 21 Oct 2026 07:49:13 GMT
Server: WSGIServer/0.2 CPython/3.12.6
Content-Type: text/html; charset=utf-8
Location: /djangoapp/
X-Frame-Options: DENY
Content-Length: 0
Vary: Cookie
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
Set-Cookie:  sessionid=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/; SameSite=Lax
```

### Task 7 (1 pt) - Public GitHub URL of server/frontend/src/components/Register/Register.jsx (Sign-up page)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/server/frontend/src/components/Register/Register.jsx
```

### Task 8 (2 pts) - cURL command + output showing the review(s) for a dealer ID (file: getdealerreviews)

```
# The reviews submitted for dealer id 15.

theia@theia-devshahm:/home/project/server$ curl -s -X GET "http://localhost:5000/api/get_reviews?id=15"
[{"car_make":"Audi","car_model":"A6","car_year":2010,"dealership":15,"id":1,"name":"Berkly Shepley","purchase":true,"purchase_date":"07/11/2020","review":"Total grid-enabled service-desk"},{"car_make":"Audi","car_model":"A6","car_year":2010,"dealership":15,"id":"15","name":"Tempsoft Car Dealership","purchase":null,"purchase_date":"","review":"Fantastic services, friendly staff and a great car."},{"car_make":"Audi","car_model":"A6","car_year":2010,"dealership":15,"id":"15","name":"Tempsoft Car Dealership","purchase":null,"purchase_date":"","review":"Fantastic services, friendly staff and a great car."},{"car_make":"Audi","car_model":"A6","car_year":2010,"dealership":15,"id":"15","name":"Tempsoft Car Dealership","purchase":"Yes","purchase_date":"2026-10-15","review":"Fantastic services, friendly staff and a great car."},{"car_make":"Audi","car_model":"A6","car_year":2010,"dealership":15,"id":"15","name":"Tempsoft Car Dealership","purchase":"Yes","purchase_date":"2026-10-15","review":"Fantastic services, friendly staff and a great car."}]
```

### Task 9 (2 pts) - cURL command + output showing all dealer(s) retrieved (file: getalldealers)

```
# All dealerships stored in the Cloudant 'dealerships' database,
# served by the get-dealership cloud function.

theia@theia-devshahm:/home/project/server$ curl -s -X GET "http://localhost:3000/dealerships/get"
[{"id":1,"city":"El Paso","state":"Texas","st":"TX","address":"3 Nova Court","zip":"88563","lat":31.6948,"long":-106.3,"short_name":"Holdlamis","full_name":"Holdlamis Car Dealership"},{"id":2,"city":"Minneapolis","state":"Minnesota","st":"MN","address":"6337 Butternut Crossing","zip":"55402","lat":44.9762,"long":-93.2759,"short_name":"Temp","full_name":"Temp Car Dealership"},{"id":3,"city":"Birmingham","state":"Alabama","st":"AL","address":"9477 Twin Pines Center","zip":"35285","lat":33.5446,"long":-86.9292,"short_name":"Sub-Ex","full_name":"Sub-Ex Car Dealership"},{"id":4,"city":"Dallas","state":"Texas","st":"TX","address":"85800 Hazelcrest Circle","zip":"75241","lat":32.6722,"long":-96.7774,"short_name":"Solarbreeze","full_name":"Solarbreeze Car Dealership"},{"id":5,"city":"Baltimore","state":"Maryland","st":"MD","address":"93 Golf Course Pass","zip":"21203","lat":39.2847,"long":-76.6205,"short_name":"Regrant","full_name":"Regrant Car Dealership"},{"id":6,"city":"Wilkes Barre","state":"Pennsylvania","st":"PA","address":"2 Burrows Hill","zip":"18763","lat":41.2722,"long":-75.8801,"short_name":"Stronghold","full_name":"Stronghold Car Dealership"},{"id":7,"city":"Pueblo","state":"Colorado","st":"CO","address":"9 Cambridge Park","zip":"81010","lat":38.1286,"long":-104.5523,"short_name":"Job","full_name":"Job Car Dealership"},{"id":8,"city":"Topeka","state":"Kansas","st":"KS","address":"288 Larry Place","zip":"66642","lat":39.0429,"long":-95.7697,"short_name":"Bytecard","full_name":"Bytecard Car Dealership"},{"id":9,"city":"Dallas","state":"Texas","st":"TX","address":"253 Hanson Junction","zip":"75216","lat":32.7086,"long":-96.7955,"short_name":"Job","full_name":"Job Car Dealership"},{"id":10,"city":"Washington","state":"District of Columbia","st":"DC","address":"108 Memorial Pass","zip":"20005","lat":38.9067,"long":-77.0312,"short_name":"Alphazap","full_name":"Alphazap Car Dealership"},{"id":11,"city":"Carol Stream","state":"Illinois","st":"IL","address":"8108 Dryden Court","zip":"60351","lat":41.9166,"long":-88.1208,"short_name":"Rank","full_name":"Rank Car Dealership"},{"id":12,"city":"Silver Spring","state":"Maryland","st":"MD","address":"168 Pawling Lane","zip":"20918","lat":39.144,"long":-77.2076,"short_name":"Tin","full_name":"Tin Car Dealership"},{"id":13,"city":"Baltimore","state":"Maryland","st":"MD","address":"452 Fair Oaks Drive","zip":"21275","lat":39.2847,"long":-76.6205,"short_name":"Y-Solowarm","full_name":"Y-Solowarm Car Dealership"},{"id":14,"city":"San Francisco","state":"California","st":"CA","address":"2109 Scott Parkway","zip":"94147","lat":37.7848,"long":-122.7278,"short_name":"It","full_name":"It Car Dealership"},{"id":15,"city":"San Antonio","state":"Texas","st":"TX","address":"5057 Pankratz Hill","zip":"78225","lat":29.3875,"long":-98.5245,"short_name":"Tempsoft","full_name":"Tempsoft Car Dealership"},{"id":16,"city":"El Paso","state":"Texas","st":"TX","address":"0 Rieder Trail","zip":"79994","lat":31.6948,"long":-106.3,"short_name":"Treeflex","full_name":"Treeflex Car Dealership"},{"id":17,"city":"San Jose","state":"California","st":"CA","address":"7670 American Ash Drive","zip":"95138","lat":37.2602,"long":-121.7709,"short_name":"Home Ing","full_name":"Home Ing Car Dealership"},{"id":18,"city":"Whittier","state":"California","st":"CA","address":"4 Pearson Avenue","zip":"90605","lat":33.9413,"long":-118.0356,"short_name":"Bitchip","full_name":"Bitchip Car Dealership"},{"id":19,"city":"Hialeah","state":"Florida","st":"FL","address":"93 Monument Circle","zip":"33013","lat":25.8594,"long":-80.2725,"short_name":"Otcom","full_name":"Otcom Car Dealership"},{"id":20,"city":"Detroit","state":"Michigan","st":"MI","address":"4580 Waubesa Lane","zip":"48224","lat":42.4098,"long":-82.9441,"short_name":"Subin","full_name":"Subin Car Dealership"},{"id":21,"city":"San Francisco","state":"California","st":"CA","address":"046 Mockingbird Junction","zip":"94154","lat":37.7848,"long":-122.7278,"short_name":"Andalax","full_name":"Andalax Car Dealership"},{"id":22,"city":"Fort Lauderdale","state":"Florida","st":"FL","address":"45737 Butternut Lane","zip":"33330","lat":26.0663,"long":-80.3339,"short_name":"Y-Solowarm","full_name":"Y-Solowarm Car Dealership"},{"id":23,"city":"Des Moines","state":"Iowa","st":"IA","address":"21425 Bartelt Pass","zip":"50936","lat":41.6727,"long":-93.5722,"short_name":"Bitchip","full_name":"Bitchip Car Dealership"},{"id":24,"city":"Utica","state":"New York","st":"NY","address":"408 Delaware Circle","zip":"13505","lat":43.0872,"long":-75.2603,"short_name":"Aerified","full_name":"Aerified Car Dealership"},{"id":25,"city":"Washington","state":"District of Columbia","st":"DC","address":"6505 Melrose Junction","zip":"20580","lat":38.8933,"long":-77.0146,"short_name":"Opela","full_name":"Opela Car Dealership"},{"id":26,"city":"Pittsburgh","state":"Pennsylvania","st":"PA","address":"306 Jenna Parkway","zip":"15279","lat":40.4344,"long":-80.0248,"short_name":"Flowdesk","full_name":"Flowdesk Car Dealership"},{"id":27,"city":"San Antonio","state":"Texas","st":"TX","address":"95321 Superior Hill","zip":"78245","lat":29.4189,"long":-98.6895,"short_name":"Namfix","full_name":"Namfix Car Dealership"},{"id":28,"city":"Hialeah","state":"Florida","st":"FL","address":"5458 Maple Way","zip":"33018","lat":25.9098,"long":-80.3889,"short_name":"Fixflex","full_name":"Fixflex Car Dealership"},{"id":29,"city":"San Francisco","state":"California","st":"CA","address":"9 Harper Circle","zip":"94110","lat":37.7509,"long":-122.4153,"short_name":"Fix San","full_name":"Fix San Car Dealership"},{"id":30,"city":"Houston","state":"Texas","st":"TX","address":"5423 Spaight Road","zip":"77218","lat":29.834,"long":-95.4342,"short_name":"Opela","full_name":"Opela Car Dealership"},{"id":31,"city":"New York City","state":"New York","st":"NY","address":"5 Northfield Pass","zip":"10131","lat":40.7808,"long":-73.9772,"short_name":"Fintone","full_name":"Fintone Car Dealership"},{"id":32,"city":"Wilkes Barre","state":"Pennsylvania","st":"PA","address":"3 Carey Junction","zip":"18768","lat":41.2722,"long":-75.8801,"short_name":"Subin","full_name":"Subin Car Dealership"},{"id":33,"city":"Des Moines","state":"Iowa","st":"IA","address":"627 Cottonwood Circle","zip":"50335","lat":41.6727,"long":-93.5722,"short_name":"Tres-Zap","full_name":"Tres-Zap Car Dealership"},{"id":34,"city":"Silver Spring","state":"Maryland","st":"MD","address":"8 Green Hill","zip":"20904","lat":39.0668,"long":-76.9969,"short_name":"Gembucket","full_name":"Gembucket Car Dealership"},{"id":35,"city":"Seattle","state":"Washington","st":"WA","address":"9 Beilfuss Trail","zip":"98158","lat":47.4497,"long":-122.3076,"short_name":"Treeflex","full_name":"Treeflex Car Dealership"},{"id":36,"city":"Vienna","state":"Virginia","st":"VA","address":"311 Paget Alley","zip":"22184","lat":38.8318,"long":-77.2888,"short_name":"Latlux","full_name":"Latlux Car Dealership"},{"id":37,"city":"Detroit","state":"Michigan","st":"MI","address":"152 Moland Lane","zip":"48224","lat":42.4098,"long":-82.9441,"short_name":"Ventosanzap","full_name":"Ventosanzap Car Dealership"},{"id":38,"city":"Dallas","state":"Texas","st":"TX","address":"821 New Castle Trail","zip":"75226","lat":32.7887,"long":-96.7676,"short_name":"Zamit","full_name":"Zamit Car Dealership"},{"id":39,"city":"Fresno","state":"California","st":"CA","address":"990 Raven Road","zip":"93740","lat":36.7464,"long":-119.6397,"short_name":"Stronghold","full_name":"Stronghold Car Dealership"},{"id":40,"city":"Merrifield","state":"Virginia","st":"VA","address":"89375 Main Trail","zip":"22119","lat":38.8318,"long":-77.2888,"short_name":"Greenlam","full_name":"Greenlam Car Dealership"},{"id":41,"city":"Baltimore","state":"Maryland","st":"MD","address":"9 Sherman Hill","zip":"21275","lat":39.2847,"long":-76.6205,"short_name":"Tres-Zap","full_name":"Tres-Zap Car Dealership"},{"id":42,"city":"Jersey City","state":"New Jersey","st":"NJ","address":"62 Manley Point","zip":"07310","lat":40.7324,"long":-74.0431,"short_name":"Konklab","full_name":"Konklab Car Dealership"},{"id":43,"city":"Atlanta","state":"Georgia","st":"GA","address":"91 Declaration Avenue","zip":"31119","lat":33.8913,"long":-84.0746,"short_name":"Opela","full_name":"Opela Car Dealership"},{"id":44,"city":"Roanoke","state":"Virginia","st":"VA","address":"0 Northview Point","zip":"24014","lat":37.2327,"long":-79.9463,"short_name":"Veribet","full_name":"Veribet Car Dealership"},{"id":45,"city":"Norfolk","state":"Virginia","st":"VA","address":"283 Mockingbird Plaza","zip":"23509","lat":36.8787,"long":-76.2604,"short_name":"Konklux","full_name":"Konklux Car Dealership"},{"id":46,"city":"New Orleans","state":"Louisiana","st":"LA","address":"527 Hayes Junction","zip":"70165","lat":30.033,"long":-89.8826,"short_name":"Regrant","full_name":"Regrant Car Dealership"},{"id":47,"city":"Stamford","state":"Connecticut","st":"CT","address":"840 Pepper Wood Crossing","zip":"06905","lat":41.0888,"long":-73.5435,"short_name":"Prodder","full_name":"Prodder Car Dealership"},{"id":48,"city":"Tucson","state":"Arizona","st":"AZ","address":"48610 Morning Street","zip":"85710","lat":32.2138,"long":-110.824,"short_name":"It","full_name":"It Car Dealership"},{"id":49,"city":"Athens","state":"Georgia","st":"GA","address":"222 Grasskamp Plaza","zip":"30605","lat":33.9321,"long":-83.3525,"short_name":"Veribet","full_name":"Veribet Car Dealership"},{"id":50,"city":"Atlanta","state":"Georgia","st":"GA","address":"76 Clove Trail","zip":"30316","lat":33.7217,"long":-84.3339,"short_name":"Aerified","full_name":"Aerified Car Dealership"}]
```

### Task 10 (2 pts) - cURL command + output showing the details of a dealer ID (file: getdealerbyid)

```
# The details of dealer id 8 (Bytecard Car Dealership, Topeka, Kansas).

theia@theia-devshahm:/home/project/server$ curl -s -X GET "http://localhost:3000/dealerships/get?id=8"
[{"id":8,"city":"Topeka","state":"Kansas","st":"KS","address":"288 Larry Place","zip":"66642","lat":39.0429,"long":-95.7697,"short_name":"Bytecard","full_name":"Bytecard Car Dealership"}]
```

### Task 11 (2 pts) - cURL command + output showing the dealer(s) in Kansas (file: getdealersbyState)

```
# All dealerships located in the state of Kansas.

theia@theia-devshahm:/home/project/server$ curl -s -X GET "http://localhost:3000/dealerships/get?state=Kansas"
[{"id":8,"city":"Topeka","state":"Kansas","st":"KS","address":"288 Larry Place","zip":"66642","lat":39.0429,"long":-95.7697,"short_name":"Bytecard","full_name":"Bytecard Car Dealership"}]
```

### Task 12 (2 pts) - Screenshot of the root user logged in on the admin page (admin_login.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/admin_login.png
```

### Task 13 (1 pt) - Screenshot of the root user logged out from the admin page (admin_logout.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/admin_logout.png
```

### Task 14 (2 pts) - cURL command + output showing all car makes and models retrieved (file: getallcarmakes) - part 1

```
# All car makes together with the car models of every make.

theia@theia-devshahm:/home/project/server$ curl -s -X GET "http://localhost:3000/carmakes/get"
[{"id":1,"name":"Audi","description":"German engineering with a focus on comfort and technology.","car_models":[{"id":1,"name":"A6","dealer_id":1,"model_type":"Sedan","year":"2010-01-01T00:00:00.000Z"},{"id":2,"name":"A4","dealer_id":2,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":3,"name":"Q5","dealer_id":3,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":4,"name":"Q7","dealer_id":4,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":2,"name":"BMW","description":"The ultimate driving machine, built for the German road.","car_models":[{"id":5,"name":"3 Series","dealer_id":5,"model_type":"Sedan","year":"2015-01-01T00:00:00.000Z"},{"id":6,"name":"X3","dealer_id":6,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":7,"name":"X5","dealer_id":7,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":8,"name":"M3","dealer_id":8,"model_type":"Sedan","year":"2016-01-01T00:00:00.000Z"}]},{"id":3,"name":"Chevrolet","description":"American value with a dealership network in every state.","car_models":[{"id":9,"name":"Silverado 1500","dealer_id":9,"model_type":"WAGON","year":"2017-01-01T00:00:00.000Z"},{"id":10,"name":"Equinox","dealer_id":10,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":11,"name":"Malibu","dealer_id":11,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":12,"name":"Tahoe","dealer_id":12,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":4,"name":"Ford","description":"The truck brand that built America.","car_models":[{"id":13,"name":"F-150","dealer_id":13,"model_type":"WAGON","year":"2016-01-01T00:00:00.000Z"},{"id":14,"name":"Escape","dealer_id":14,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":15,"name":"Explorer","dealer_id":15,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":16,"name":"Mustang","dealer_id":16,"model_type":"Sedan","year":"2015-01-01T00:00:00.000Z"}]},{"id":5,"name":"Honda","description":"Reliable, efficient and built for everyday driving.","car_models":[{"id":17,"name":"Civic","dealer_id":17,"model_type":"Sedan","year":"2019-01-01T00:00:00.000Z"},{"id":18,"name":"Accord","dealer_id":18,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":19,"name":"CR-V","dealer_id":19,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":20,"name":"Pilot","dealer_id":20,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":6,"name":"Jeep","description":"Capable off roaders for every adventure.","car_models":[{"id":21,"name":"Wrangler","dealer_id":21,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":22,"name":"Grand Cherokee","dealer_id":22,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":23,"name":"Cherokee","dealer_id":23,"model_type":"SUV","year":"2018-01-01T00:00:00.000Z"},{"id":24,"name":"Compass","dealer_id":24,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":7,"name":"Nissan","description":"Japanese value with a strong crossover line up.","car_models":[{"id":25,"name":"Altima","dealer_id":25,"model_type":"Sedan","year":"2019-01-01T00:00:00.000Z"},{"id":26,"name":"Sentra","dealer_id":26,"model_type":"Sedan","year":"2020-01-01T00:00:00.000Z"},{"id":27,"name":"Rogue","dealer_id":27,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":28,"name":"Pathfinder","dealer_id":28,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":8,"name":"Toyota","description":"The benchmark of reliability and resale value.","car_models":[{"id":29,"name":"Camry","dealer_id":29,"model_type":"Sedan","year":"2019-01-01T00:00:00.000Z"},{"id":30,"name":"Corolla","dealer_id":30,"model_type":"Sedan","year":"2020-01-01T00:00:00.000Z"},{"id":31,"name":"RAV4","dealer_id":31,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":32,"name":"Highlander","dealer_id":32,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"}]},{"id":9,"name":"Volkswagen","description":"German engineering with a practical footprint.","car_models":[{"id":33,"name":"Jetta","dealer_id":33,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":34,"name":"Passat","dealer_id":34,"model_type":"Sedan","year":"2017-01-01T00:00:00.000Z"},{"id":35,"name":"Tiguan","dealer_id":35,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":36,"name":"Atlas","dealer_id":36,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"}]},{"id":10,"name":"Tesla","description":"Electric mobility with over the air updates.","car_models":[{"id":37,"name":"Model 3","dealer_id":37,"model_type":"Sedan","year":"2021-01-01T00:00:00.000Z"},{"id":38,"name":"Model S","dealer_id":38,"model_type":"Sedan","year":"2020-01-01T00:00:00.000Z"},{"id":39,"name":"Model Y","dealer_id":39,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"},{"id":40,"name":"Model X","dealer_id":40,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"}]}]
```

### Task 15 (2 pts) - cURL command + output showing all car makes and models retrieved (file: getallcarmakes) - part 2

```
# All car makes together with the car models of every make.

theia@theia-devshahm:/home/project/server$ curl -s -X GET "http://localhost:3000/carmakes/get"
[{"id":1,"name":"Audi","description":"German engineering with a focus on comfort and technology.","car_models":[{"id":1,"name":"A6","dealer_id":1,"model_type":"Sedan","year":"2010-01-01T00:00:00.000Z"},{"id":2,"name":"A4","dealer_id":2,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":3,"name":"Q5","dealer_id":3,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":4,"name":"Q7","dealer_id":4,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":2,"name":"BMW","description":"The ultimate driving machine, built for the German road.","car_models":[{"id":5,"name":"3 Series","dealer_id":5,"model_type":"Sedan","year":"2015-01-01T00:00:00.000Z"},{"id":6,"name":"X3","dealer_id":6,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":7,"name":"X5","dealer_id":7,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":8,"name":"M3","dealer_id":8,"model_type":"Sedan","year":"2016-01-01T00:00:00.000Z"}]},{"id":3,"name":"Chevrolet","description":"American value with a dealership network in every state.","car_models":[{"id":9,"name":"Silverado 1500","dealer_id":9,"model_type":"WAGON","year":"2017-01-01T00:00:00.000Z"},{"id":10,"name":"Equinox","dealer_id":10,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":11,"name":"Malibu","dealer_id":11,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":12,"name":"Tahoe","dealer_id":12,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":4,"name":"Ford","description":"The truck brand that built America.","car_models":[{"id":13,"name":"F-150","dealer_id":13,"model_type":"WAGON","year":"2016-01-01T00:00:00.000Z"},{"id":14,"name":"Escape","dealer_id":14,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":15,"name":"Explorer","dealer_id":15,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":16,"name":"Mustang","dealer_id":16,"model_type":"Sedan","year":"2015-01-01T00:00:00.000Z"}]},{"id":5,"name":"Honda","description":"Reliable, efficient and built for everyday driving.","car_models":[{"id":17,"name":"Civic","dealer_id":17,"model_type":"Sedan","year":"2019-01-01T00:00:00.000Z"},{"id":18,"name":"Accord","dealer_id":18,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":19,"name":"CR-V","dealer_id":19,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":20,"name":"Pilot","dealer_id":20,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":6,"name":"Jeep","description":"Capable off roaders for every adventure.","car_models":[{"id":21,"name":"Wrangler","dealer_id":21,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":22,"name":"Grand Cherokee","dealer_id":22,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":23,"name":"Cherokee","dealer_id":23,"model_type":"SUV","year":"2018-01-01T00:00:00.000Z"},{"id":24,"name":"Compass","dealer_id":24,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":7,"name":"Nissan","description":"Japanese value with a strong crossover line up.","car_models":[{"id":25,"name":"Altima","dealer_id":25,"model_type":"Sedan","year":"2019-01-01T00:00:00.000Z"},{"id":26,"name":"Sentra","dealer_id":26,"model_type":"Sedan","year":"2020-01-01T00:00:00.000Z"},{"id":27,"name":"Rogue","dealer_id":27,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":28,"name":"Pathfinder","dealer_id":28,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"}]},{"id":8,"name":"Toyota","description":"The benchmark of reliability and resale value.","car_models":[{"id":29,"name":"Camry","dealer_id":29,"model_type":"Sedan","year":"2019-01-01T00:00:00.000Z"},{"id":30,"name":"Corolla","dealer_id":30,"model_type":"Sedan","year":"2020-01-01T00:00:00.000Z"},{"id":31,"name":"RAV4","dealer_id":31,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"},{"id":32,"name":"Highlander","dealer_id":32,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"}]},{"id":9,"name":"Volkswagen","description":"German engineering with a practical footprint.","car_models":[{"id":33,"name":"Jetta","dealer_id":33,"model_type":"Sedan","year":"2018-01-01T00:00:00.000Z"},{"id":34,"name":"Passat","dealer_id":34,"model_type":"Sedan","year":"2017-01-01T00:00:00.000Z"},{"id":35,"name":"Tiguan","dealer_id":35,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"},{"id":36,"name":"Atlas","dealer_id":36,"model_type":"SUV","year":"2019-01-01T00:00:00.000Z"}]},{"id":10,"name":"Tesla","description":"Electric mobility with over the air updates.","car_models":[{"id":37,"name":"Model 3","dealer_id":37,"model_type":"Sedan","year":"2021-01-01T00:00:00.000Z"},{"id":38,"name":"Model S","dealer_id":38,"model_type":"Sedan","year":"2020-01-01T00:00:00.000Z"},{"id":39,"name":"Model Y","dealer_id":39,"model_type":"SUV","year":"2021-01-01T00:00:00.000Z"},{"id":40,"name":"Model X","dealer_id":40,"model_type":"SUV","year":"2020-01-01T00:00:00.000Z"}]}]
```

### Task 16 (2 pts) - cURL command + output showing the sentiment analysis of "Fantastic services" (file: analyzereview)

```
# Watson Natural Language Understanding sentiment analysis of the
# review text "Fantastic services".

theia@theia-devshahm:/home/project/server$ curl -s -X GET "http://localhost:5000/api/analyze?text=Fantastic%20services"
{"sentiment":"positive","text":"Fantastic services"}
```

### Task 17 (1 pt) - Screenshot of the dealers on the home page before logging in (get_dealers.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/get_dealers.png
```

### Task 18 (2 pts) - Screenshot of the dealers after logging in (get_dealers_loggedin.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/get_dealers_loggedin.png
```

### Task 19 (2 pts) - Screenshot of the dealers filtered by State (dealersbystate.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/dealersbystate.png
```

### Task 20 (1 pt) - Screenshot of the dealer page with its reviews (dealer_id_reviews.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/dealer_id_reviews.png
```

### Task 21 (1 pt) - Screenshot of the Post Review page after entering the review, before submission (dealership_review_submission.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/dealership_review_submission.png
```

### Task 22 (2 pts) - Screenshot of the posted review (added_review.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/added_review.png
```

### Task 23 (3 pts) - Terminal output of the GitHub Actions workflow running successfully (file: CICD)

```
﻿theia@theia-devshahm:/home/project$ gh workflow run linter.yml --repo Meet6338-X/agfzb-CloudAppDevelopment_Capstone --ref master

theia@theia-devshahm:/home/project$ gh run list --repo Meet6338-X/agfzb-CloudAppDevelopment_Capstone --limit 1
completed	success	Lint Code	Lint Code	master	workflow_dispatch	39562718311	28s	2026-10-21T07:32:37Z

theia@theia-devshahm:/home/project$ gh run view 39562718311 --repo Meet6338-X/agfzb-CloudAppDevelopment_Capstone

Γ£ô master Lint Code ┬╖ 39562718311
Triggered via workflow_dispatch about 4 minutes ago

JOBS
Γ£ô Linting Django Server in 11s (ID 119097535563)
Γ£ô Linting JavaScript Function in 12s (ID 119097535664)
Γ£ô Linting Dealership Cloud Function in 13s (ID 119097535708)
Γ£ô Linting Python Function in 9s (ID 119097535723)
Γ£ô Build the application container image in 19s (ID 119097535812)
Γ£ô Linting Django Application in 23s (ID 119097535857)
Γ£ô Linting Reviews Cloud Function in 12s (ID 119097536034)

ANNOTATIONS
! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Linting Django Server: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Linting Django Server: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-node@v3. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Linting JavaScript Function: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Linting JavaScript Function: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-node@v3. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Linting Dealership Cloud Function: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Linting Dealership Cloud Function: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Linting Python Function: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Linting Python Function: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Build the application container image: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Build the application container image: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Linting Django Application: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Linting Django Application: .github#1

! Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Linting Reviews Cloud Function: .github#2

- "The ubuntu-latest label will migrate to Ubuntu 26 beginning October 19, 2026. For more information, see https://github.com/actions/runner-images/issues/14748"
Linting Reviews Cloud Function: .github#1


For more information about a job, try: gh run view --job=<job-id>
View this run on GitHub: https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/actions/runs/39562718311

theia@theia-devshahm:/home/project$ gh run view 39562718311 --repo Meet6338-X/agfzb-CloudAppDevelopment_Capstone --log | tail -n 150
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8380342Z Receiving objects:  99% (274/276)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8381344Z Receiving objects: 100% (276/276)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8382679Z Receiving objects: 100% (276/276), 1.09 MiB | 24.72 MiB/s, done.
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8384602Z Resolving deltas:   0% (0/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8385741Z Resolving deltas:   3% (1/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8386918Z Resolving deltas:   6% (2/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8388201Z Resolving deltas:   9% (3/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8396421Z Resolving deltas:  12% (4/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8398269Z Resolving deltas:  16% (5/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8399613Z Resolving deltas:  19% (6/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8400479Z Resolving deltas:  22% (7/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8401074Z Resolving deltas:  25% (8/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8401669Z Resolving deltas:  29% (9/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8402391Z Resolving deltas:  32% (10/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8402992Z Resolving deltas:  35% (11/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8403567Z Resolving deltas:  38% (12/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8404135Z Resolving deltas:  41% (13/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8404699Z Resolving deltas:  45% (14/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8405289Z Resolving deltas:  48% (15/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8406139Z Resolving deltas:  51% (16/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8406733Z Resolving deltas:  54% (17/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8407667Z Resolving deltas:  58% (18/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8408267Z Resolving deltas:  61% (19/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8408859Z Resolving deltas:  64% (20/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8409433Z Resolving deltas:  67% (21/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8410012Z Resolving deltas:  70% (22/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8410594Z Resolving deltas:  74% (23/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8411168Z Resolving deltas:  77% (24/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8411751Z Resolving deltas:  80% (25/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8412333Z Resolving deltas:  83% (26/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8412908Z Resolving deltas:  87% (27/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8413484Z Resolving deltas:  90% (28/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8414059Z Resolving deltas:  93% (29/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8414644Z Resolving deltas:  96% (30/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8415216Z Resolving deltas: 100% (31/31)
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8415817Z Resolving deltas: 100% (31/31), done.
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8525217Z From https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8526447Z  * [new ref]         87212595c6a61fea063523dad225a82b177cd7ef -> origin/master
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8532118Z ##[endgroup]
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8533010Z ##[group]Determining the checkout info
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8534534Z ##[endgroup]
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8535382Z ##[group]Checking out the ref
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8539398Z [command]/usr/bin/git checkout --progress --force -B master refs/remotes/origin/master
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8782009Z Reset branch 'master'
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8788119Z branch 'master' set up to track 'origin/master'.
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8833850Z ##[endgroup]
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8836915Z [command]/usr/bin/git log -1 --format='%H'
Linting Reviews Cloud Function	Run actions/checkout@v3	2026-10-21T07:32:43.8862279Z '87212595c6a61fea063523dad225a82b177cd7ef'
Linting Reviews Cloud Function	Set up Python 3.11	∩╗┐2026-10-21T07:32:43.9166111Z ##[group]Run actions/setup-python@v4
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:43.9166815Z with:
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:43.9167637Z   python-version: 3.11
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:43.9168431Z   check-latest: false
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:43.9172560Z   token: ***
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:43.9173049Z   update-environment: true
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:43.9173600Z   allow-prereleases: false
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:43.9174126Z ##[endgroup]
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:44.0562642Z ##[group]Installed versions
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:44.1142789Z (node:2249) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:44.1145766Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:44.1147860Z Successfully set up CPython (3.11.17)
Linting Reviews Cloud Function	Set up Python 3.11	2026-10-21T07:32:44.1149637Z ##[endgroup]
Linting Reviews Cloud Function	Install dependencies	∩╗┐2026-10-21T07:32:44.1375728Z ##[group]Run python -m pip install --upgrade pip
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1377803Z ^[[36;1mpython -m pip install --upgrade pip^[[0m
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1379236Z ^[[36;1mpip install pylint^[[0m
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1380996Z ^[[36;1mif [ -f requirements.txt ]; then pip install -r requirements.txt; fi^[[0m
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1853096Z shell: /usr/bin/bash -e {0}
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1853983Z env:
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1854806Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1856399Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1858078Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1859371Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1860659Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1862015Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:44.1863111Z ##[endgroup]
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:46.8412002Z Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages (26.2.1)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:46.9605431Z Collecting pip
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.0107272Z   Downloading pip-26.2.2-py3-none-any.whl.metadata (4.6 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.0189017Z Downloading pip-26.2.2-py3-none-any.whl (1.8 MB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.0887746Z    ΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöü 1.8/1.8 MB 47.4 MB/s  0:00:00
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.2551956Z Installing collected packages: pip
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.2552931Z   Attempting uninstall: pip
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.2567482Z     Found existing installation: pip 26.2.1
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.3279807Z     Uninstalling pip-26.2.1:
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:47.3344077Z       Successfully uninstalled pip-26.2.1
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:48.2265398Z Successfully installed pip-26.2.2
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.1795731Z Collecting pylint
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.2281646Z   Downloading pylint-4.1.3-py3-none-any.whl.metadata (12 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.2579454Z Collecting astroid<=4.4,>=4.3.4 (from pylint)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.2616649Z   Downloading astroid-4.3.4-py3-none-any.whl.metadata (4.4 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.2850235Z Collecting dill>=0.3.6 (from pylint)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.2887360Z   Downloading dill-0.4.1-py3-none-any.whl.metadata (10 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3231026Z Collecting isort!=5.13,<10,>=5 (from pylint)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3277598Z   Downloading isort-9.0.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3400827Z Collecting mccabe<0.8,>=0.6 (from pylint)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3435159Z   Downloading mccabe-0.7.0-py2.py3-none-any.whl.metadata (5.0 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3647996Z Collecting platformdirs>=2.2 (from pylint)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3684113Z   Downloading platformdirs-4.13.5-py3-none-any.whl.metadata (5.5 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3853843Z Collecting tomlkit>=0.10.1 (from pylint)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.3888840Z   Downloading tomlkit-0.15.2-py3-none-any.whl.metadata (3.4 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4009313Z Collecting mypy-extensions>=1.1.0 (from isort!=5.13,<10,>=5->pylint)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4046991Z   Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4133401Z Downloading pylint-4.1.3-py3-none-any.whl (588 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4293126Z    ΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöü 589.0/589.0 kB 59.3 MB/s  0:00:00
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4334945Z Downloading astroid-4.3.4-py3-none-any.whl (288 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4407301Z Downloading isort-9.0.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.6 MB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4577347Z    ΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöüΓöü 1.6/1.6 MB 100.9 MB/s  0:00:00
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4611619Z Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4661322Z Downloading dill-0.4.1-py3-none-any.whl (120 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4713957Z Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4766621Z Downloading platformdirs-4.13.5-py3-none-any.whl (32 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.4817602Z Downloading tomlkit-0.15.2-py3-none-any.whl (52 kB)
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:49.5291120Z Installing collected packages: tomlkit, platformdirs, mypy-extensions, mccabe, dill, astroid, isort, pylint
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:50.3077280Z 
Linting Reviews Cloud Function	Install dependencies	2026-10-21T07:32:50.3088698Z Successfully installed astroid-4.3.4 dill-0.4.1 isort-9.0.2 mccabe-0.7.0 mypy-extensions-1.1.0 platformdirs-4.13.5 pylint-4.1.3 tomlkit-0.15.2
Linting Reviews Cloud Function	Lint with Pylint	∩╗┐2026-10-21T07:32:50.3703725Z ##[group]Run pylint *.py
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3704038Z ^[[36;1mpylint *.py^[[0m
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3771504Z shell: /usr/bin/bash -e {0}
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3771775Z env:
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3772053Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3772529Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3772989Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3773398Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3773806Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3774219Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.3774565Z ##[endgroup]
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.6353464Z pylint: Command line or configuration file:1: UserWarning: 'BaseException' is not a proper value for the 'overgeneral-exceptions' option. Use fully qualified name (maybe 'builtins.BaseException' ?) instead. This will cease to be checked at runtime when the configuration upgrader is released.
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:50.6357588Z pylint: Command line or configuration file:1: UserWarning: 'Exception' is not a proper value for the 'overgeneral-exceptions' option. Use fully qualified name (maybe 'builtins.Exception' ?) instead. This will cease to be checked at runtime when the configuration upgrader is released.
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:51.3642196Z 
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:51.3642757Z ------------------------------------
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:51.3643434Z Your code has been rated at 10.00/10
Linting Reviews Cloud Function	Lint with Pylint	2026-10-21T07:32:51.3643814Z 
Linting Reviews Cloud Function	Post Set up Python 3.11	∩╗┐2026-10-21T07:32:51.6137774Z Post job cleanup.
Linting Reviews Cloud Function	Post Set up Python 3.11	2026-10-21T07:32:51.7365436Z (node:2339) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Reviews Cloud Function	Post Set up Python 3.11	2026-10-21T07:32:51.7366702Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Reviews Cloud Function	Post Run actions/checkout@v3	∩╗┐2026-10-21T07:32:51.7584318Z Post job cleanup.
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8294971Z (node:2347) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8295741Z (Use `node --trace-deprecation ...` to show where the warning was created)
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8331957Z [command]/usr/bin/git version
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8368452Z git version 2.55.0
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8408914Z Temporarily overriding HOME='/home/runner/work/_temp/51ca16c0-abd5-4603-ad6e-4df69df87173' before making global git config changes
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8410371Z Adding repository directory to the temporary git global config as a safe directory
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8415061Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/agfzb-CloudAppDevelopment_Capstone/agfzb-CloudAppDevelopment_Capstone
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8450511Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8483229Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8713902Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8739665Z http.https://github.com/.extraheader
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8750899Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
Linting Reviews Cloud Function	Post Run actions/checkout@v3	2026-10-21T07:32:51.8785530Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
Linting Reviews Cloud Function	Complete job	∩╗┐2026-10-21T07:32:51.9154127Z Cleaning up orphan processes
Linting Reviews Cloud Function	Complete job	2026-10-21T07:32:51.9569410Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v3, actions/setup-python@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```

### Task 24 (1 pt) - Deployment URL of the Django application (file: deploymentURL)

```
﻿theia@theia-devshahm:/home/project/server$ docker build -t dealership:latest .
theia@theia-devshahm:/home/project/server$ docker run -d --name dealership-app -p 8010:8000 \\
    -e DEALERS_URL=http://host.docker.internal:3000/dealerships/get \\
    -e REVIEWS_URL=http://host.docker.internal:5000/api/get_reviews \\
    -e POST_REVIEW_URL=http://host.docker.internal:5000/api/post_review \\
    -e CARMAKES_URL=http://host.docker.internal:3000/carmakes/get \\
    -e SENTIMENT_URL=http://host.docker.internal:5000/api/analyze \\
    dealership:latest
d78eba2604473bd07e6c05547e73af02cd6c396ec04e80350c304f953a75c24e

theia@theia-devshahm:/home/project/server$ docker ps
CONTAINER ID   IMAGE              COMMAND                  STATUS         PORTS                    NAMES
d78eba260447   dealership:latest   "/bin/bash /app/entrypo"   Up 3 minutes   0.0.0.0:8010->8000/tcp   dealership-app

theia@theia-devshahm:/home/project/server$ docker logs dealership-app
Loaded 10 car makes and 40 car models
[2026-10-21 07:31:40 +0000] [1] [INFO] Starting gunicorn 21.2.0
[2026-10-21 07:31:40 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2026-10-21 07:31:40 +0000] [1] [INFO] Using worker: sync
[2026-10-21 07:31:40 +0000] [9] [INFO] Booting worker with pid: 9
[2026-10-21 07:31:40 +0000] [10] [INFO] Booting worker with pid: 10
[2026-10-21 07:31:40 +0000] [11] [INFO] Booting worker with pid: 11

DEPLOYMENT URL
--------------
http://dealership.127.0.0.1.nip.io:8010/djangoapp/

(The application is served by the containerized Django + gunicorn image
 'dealership:latest'.  The container listens on port 8000 and is published on
 the host at port 8010.  The host name 'dealership.127.0.0.1.nip.io' resolves to
 127.0.0.1, so the deployment is reachable from any browser on this machine.)

HTTP check
----------
theia@theia-devshahm:/home/project/server$ curl -s -o /dev/null -w "HTTP %{http_code}\n" http://dealership.127.0.0.1.nip.io:8010/djangoapp/
HTTP 200
```

### Task 25 (2 pts) - Screenshot of the deployed landing page (deployed_landingpage.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/deployed_landingpage.png
```

### Task 26 (2 pts) - Screenshot of the deployed logged-in page (deployed_loggedin.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/deployed_loggedin.png
```

### Task 27 (2 pts) - Screenshot of the dealer details page opened through the deployment (deployed_dealer_detail.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/deployed_dealer_detail.png
```

### Task 28 (2 pts) - Screenshot of the review displayed in the deployed application (deployed_add_review.png)

```
https://github.com/Meet6338-X/agfzb-CloudAppDevelopment_Capstone/blob/master/evidence/deployed_add_review.png
```

