# build image
FROM mcr.microsoft.com/devcontainers/python:3.13 AS builder

WORKDIR /app_who_etl

ENV PIPENV_VENV_IN_PROJECT=1

ADD Pipfile.lock Pipfile /app_who_etl/

RUN pipenv sync

# prodcution image
FROM python:3.13-slim-bookworm AS production

RUN apt-get update && apt-get install libpq5 -y

EXPOSE 8080

WORKDIR /app_who_etl

ENV PYTHONUNBUFFERED=1

COPY . .

RUN mkdir .venv

COPY --from=builder  /app_who_etl/.venv/ .venv

RUN adduser -u 5678 --disabled-password --gecos "" app_who_etl && chown -R app_who_etl /app_who_etl
USER app_who_etl

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
