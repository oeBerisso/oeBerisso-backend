FROM python:3.7.5

ENV FLASK_ENV=development
ENV FLASK_APP "run.py"

RUN mkdir /app
WORKDIR /app

add . .

RUN pip install -r requirements.txt

EXPOSE 5000:5000

CMD flask run