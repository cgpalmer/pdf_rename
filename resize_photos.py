# Source: https://opensource.com/life/15/2/resize-images-python
import os
from PIL import Image

# scale by setting a height

# baseheight = 300
# for file in os.listdir("images/"):
#     img = Image.open(f"images/{file}")
#     hpercent = (baseheight / float(img.size[1]))
#     wsize = int((float(img.size[0]) * float(hpercent)))
#     img = img.resize((wsize, baseheight), Image.ANTIALIAS)
#     name = file.split(".")
#     img.save(f'resized_images/{name[0]}_mobile.jpg')

basewidth = 1920
for file in os.listdir("images/"):
    img = Image.open(f"images/{file}")
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    name = file.split(".")
    img.save(f'resized_images/{name[0]}_mobile.jpg')