#resize all images into given ratio
#as specified by user
from PIL import Image
import os,sys

width = int(sys.argv[1])
height = int(sys.argv[2])

dir = "../" + "image" + str(width) + "by" + str(height) + "/"

if not os.path.exists(dir):
  os.makedirs(dir)

for file in os.listdir(".."):
  if file.endswith(".png"):
    im = Image.open("../" + file)
    im.copy()
    im = im.resize((width,height),Image.ANTIALIAS)
    im.save(dir+file)


