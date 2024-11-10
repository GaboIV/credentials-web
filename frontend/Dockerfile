FROM node:14

WORKDIR /app
COPY . /app

RUN npm install -g @angular/cli && npm install

CMD ["ng", "serve", "--host", "0.0.0.0"]