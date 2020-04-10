FROM node:13.12.0-alpine3.10

RUN mkdir -p /trun/frontend
WORKDIR /trun/frontend

COPY ./package.json /trun/frontend
COPY ./package-lock.json /trun/frontend

RUN npm install

COPY . /trun/frontend

CMD ["npm", "start"]
