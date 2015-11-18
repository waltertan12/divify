from flask import Flask, render_template, Markup
from lib.image_div import ImageDiv

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/div')
def div():
  image = ImageDiv("./image/tvq7ts.jpg")
  d = image.divify()
  return render_template("divs.html", divs=d)

@app.route('/<name>')
def name(name=None):
  return render_template("name.html", name=name)

if __name__ == '__main__':
  app.run()