from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/<name>')
def name(name=None):
  return render_template("name.html", name=name)

if __name__ == '__main__':
  app.run()