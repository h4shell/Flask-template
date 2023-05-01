from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
conf = {
  "host" : "0.0.0.0",
  "port" : 5000
}

@app.route("/")
def homepage():
  username = "h4shell"
  return render_template('www/index.html', user=username)

if __name__ == "__main__":
  print(f'Server: http://{conf["host"}:{conf["port"}')
  # app.run(host="0.0.0.0", port=5000, debug=True)
  from waitress import serve
  serve(app, host=conf["host"], port=conf["port"]
