from flask import Flask, session, redirect, url_for, escape, request, render_template, Response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/js")
# def javascript():
#     return url_for('static', filename='main.js')


@app.route("/sprites.png")
def sprites():
    return url_for('static', filename='bubble-sprites.png')


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")