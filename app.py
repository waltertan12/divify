from flask import Flask, render_template, Markup
from PIL import Image

class ImageDiv:
  def __init__(self, filename):
    self.image_object = Image.open(filename)
    self.height = self.image_object.size[0]
    self.width = self.image_object.size[1]
    
  def divify(self):
    divs = "<div class='new-image' style='height: 300px; width: 550px; display: inline;'>"
    pixels = self.image_object.load()
    for x in range(0, self.height):
      for y in range(0, self.width):
        color = pixels[x, y]
        divs += "<div class='tiny-div' "
        divs += "style='background-color: "
        divs += "rgb({0}, {1}, {2});'>".format(color[0], color[1], color[2])
        divs += "</div>"
    divs += "</div>"
    return divs

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