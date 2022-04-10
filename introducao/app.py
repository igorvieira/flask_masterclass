from crypt import methods

from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
  return "<a href='/posts'>Posts 2</a>"

@app.route("/redirect")
def redirect_path():
  return redirect(url_for("response"))

@app.route("/response")
def response():
  return "uma resposta do servidor"

@app.route("/posts")
@app.route("/posts/<int:id>")
def posts(id):
  titulo = request.args.get("titulo")

  data = dict(
    path=request.path,
    referrer=request.referrer,
    content_type=request.content_type,
    method=request.method,
    titulo=titulo,
    id=id if id else 0
  )
  return data

if __name__ == "_main_":
  app.run()
