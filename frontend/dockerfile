FROM node:lts

LABEL mainteiner="agustin.vanza@gmail.com"

WORKDIR /usr/src/app

COPY . .

RUN yarn

EXPOSE 8080

CMD [ "yarn", "serve" ]