from PIL import Image

class ImageDiv:
  def __init__(self, filename):
    self.image_object = Image.open(filename)
    self.height = self.image_object.size[1]
    self.width = self.image_object.size[0]
    
  def divify(self):
    divs = "<div class='new-image' "
    divs += "style='height: {0}px; ".format(self.height*2)
    divs += "width: {0}px;'>".format(self.width*2)
    pixels = self.image_object.load()
    for x in range(0, self.height):
      for y in range(0, self.width):
        color = pixels[y, x]
        divs += "<div class='tiny-div' "
        divs += "style='background-color: "
        divs += "rgb({0}, {1}, {2})'>".format(color[0], color[1], color[2])
        divs += "</div>"
    divs += "</div>"
    return divs
