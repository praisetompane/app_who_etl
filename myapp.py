from flask import Flask

def create_app():
    """Create the app."""
    app = Flask(__name__)
    @app.route('/', methods=['GET'])
    def index():
        return 'hello world' 

    return app

if __name__ == "__main__":
    create_app()