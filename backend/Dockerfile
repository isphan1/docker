FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN mkdir /usr/src/app

RUN mkdir /usr/src/app/staticfiles

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["/bin/bash", "/usr/src/app/entrypoint.sh"]

