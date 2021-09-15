#sudo html webpage
from flask import Flask, render_template

app = Flask(__name__)

# / is url
@app.route("/")
def index():
  return render_template("index.html")
#jinja will render template
@app.route("/something-else.html")
def something_else():
  return render_template("else.html")

@app.route("/index.css")
def style():
  return app.send_static_file("index.css")

@app.route("/index.js")
def client_code():
  return app.send_static_file("index.js")

app.run(host="0.0.0.0", port=50000)
