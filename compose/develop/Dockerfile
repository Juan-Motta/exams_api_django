FROM --platform=linux/x86_64 python:3.11-slim


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
  # Psycopg2 dependencies
  && apt install -y gcc \
  # Postgres dependencies
  && apt install -y libpq-dev \
  # Geo dependencies
  && apt install -y gdal-bin libproj-dev \
  # Translations dependencies
  && apt install -y gettext\
  # pango dependencies
  && apt install -y libcogl-pango-dev \
  && apt install -y libcairo2-dev 

RUN ldconfig

COPY ./requirements ./requirements
RUN pip install -r ./requirements/develop.txt

COPY ./compose/develop/django/start /start
RUN sed -i 's/\r//g' /start
RUN chmod +x /start


WORKDIR /app

COPY . .
