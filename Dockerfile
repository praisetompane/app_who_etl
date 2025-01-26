# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11

EXPOSE 8080

WORKDIR /app_etl

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY . .

# Install pip requirements
RUN python -m pip install -r requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" app_etl && chown -R app_etl /app_etl
USER app_etl

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--config", "gunicorn_config.py"]
