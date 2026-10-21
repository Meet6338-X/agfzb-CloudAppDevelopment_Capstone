FROM node:18.12.1-bullseye-slim

WORKDIR /usr/src/app

ADD package.json ./
ADD app.js ./
ADD data/dealerships.json ./data/dealerships.json
ADD data/reviews.json ./data/reviews.json

RUN npm install

EXPOSE 3030

CMD [ "node", "app.js" ]
