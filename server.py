"""Server for Hello World app."""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def show_homepage():
    return "Hello World"


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)