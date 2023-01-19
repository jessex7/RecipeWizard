# syntax=docker/dockerfile:1

FROM python:3.12.0a4-bullseye
# ENV POETRY_VERSION=${1.3.2}
RUN pip install "poetry==1.3.2"
WORKDIR /recipewizard
COPY pyproject.toml poetry.lock /recipewizard/
RUN poetry install
