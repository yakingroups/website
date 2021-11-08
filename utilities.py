#import for s3 object storage
from PIL import Image
import os

for file in os.listdir("res/images/personnels"):
  #if file is a directory ignore.
  if os.path.isdir("res/images/personnels/" + file):
    continue
  im = Image.open("res/images/personnels/" + file)
  im.resize((507, 678)).save("res/images/personnels/" + file, "JPEG")