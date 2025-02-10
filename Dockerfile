FROM python:3.11

EXPOSE 8080

WORKDIR /app_etl

ENV PYTHONUNBUFFERED=1

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update

COPY . .

RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" app_etl && chown -R app_etl /app_etl
USER app_etl

CMD ["gunicorn", "--config", "gunicorn_config.py"]
