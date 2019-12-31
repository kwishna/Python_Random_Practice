from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    url_for,
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
	return "Hello World"


if __name__ == "__main__":
	app.run("0.0.0.0", "8181", debug=None, load_dotenv=True)