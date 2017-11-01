from app.views import app
from waitress import serve

if __name__ == "__main__":
    serve(app, port=8080)
