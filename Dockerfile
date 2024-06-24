# pull official base image
FROM python:3.12-slim

# set working directory
WORKDIR /app

# set environment variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip \
    pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install

COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "python_veneto_web.apps.run:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]

