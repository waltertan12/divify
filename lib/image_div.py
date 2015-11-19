from PIL import Image
import math

class ImageDiv:
  def __init__(self, filename):
    self.image_object = Image.open(filename)
    self.height = self.image_object.size[1]
    self.width = self.image_object.size[0]
    
  def divify(self):
    half_height =  math.floor(self.height / 2)
    outer_div = "<div class='new-image' "
    outer_div += "style='height: {0}px; ".format(self.height*2)
    outer_div += "width: {0}px;'>".format(self.width*2)
    first_half = ""
    second_half = ""
    pixels = self.image_object.load()
    for x in range(0, half_height):
      for y in range(0, self.width):
        color_one = pixels[y, x]
        color_two = pixels[y, half_height + x]
        first_half  += self.create_div(color_one)
        second_half += self.create_div(color_two)
    outer_div = outer_div + first_half + second_half + "</div>"
    return outer_div

  def divify_old(self):
    

  def create_div(self, color):
    div = "<div class='tiny-div' "
    div += "style='background-color: "
    div += "rgb({0}, {1}, {2})'>".format(color[0], color[1], color[2])
    div += "</div>"
    return div