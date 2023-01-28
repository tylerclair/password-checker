import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def my_form_post():
    data = json.loads(request.data)
    text = data["text"]
    processed_text = text.upper()
    return processed_text


if __name__ == "__main__":
    app.run(debug=True)
