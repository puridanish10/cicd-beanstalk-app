import os
from flask import Flask

application = Flask(__name__)


@application.route("/")
def home():
    env = os.environ.get("APP_ENV", "not set")
    return f"<h1>Version 2</h1><p>Environment: {env}</p>"


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
