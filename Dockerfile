FROM python:3.11

EXPOSE 8080

WORKDIR /app_who_etl

ENV PYTHONUNBUFFERED=1

COPY . .

RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" app_who_etl && chown -R app_who_etl /app_who_etl
USER app_who_etl

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
