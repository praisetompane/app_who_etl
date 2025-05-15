import os


workers = int(os.environ.get("GUNICORN_PROCESSES", "2"))

threads = int(os.environ.get("GUNICORN_THREADS", "4"))

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

port = os.environ.get("PORT")
bind = os.environ.get("GUNICORN_BIND", f"0.0.0.0:{port}")

wsgi_app = "src.app_who_etl.app:create_app()"

forwarded_allow_ips = "*"

secure_scheme_headers = {"X-Forwarded-Proto": "https"}
