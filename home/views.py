from django.shortcuts import render

# Create your views here.
# Source: https://opensource.com/life/15/2/resize-images-python
import os
from PIL import Image
import time
start_time = time.time()

# scale by setting a height

# baseheight = 300
# for file in os.listdir("images/"):
#     img = Image.open(f"images/{file}")
#     hpercent = (baseheight / float(img.size[1]))
#     wsize = int((float(img.size[0]) * float(hpercent)))
#     img = img.resize((wsize, baseheight), Image.ANTIALIAS)
#     name = file.split(".")
#     img.save(f'resized_images/{name[0]}_mobile.jpg')

def hd_photos():
    basewidth = 1920
    for file in os.listdir("images/"):
        img = Image.open(f"images/{file}")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        name = file.split(".")
        img.save(f'static/resized_images/hd/{name[0]}_mobile.jpg')



def mobile_photos():
    basewidth = 300
    for file in os.listdir("images/"):
        img = Image.open(f"images/{file}")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        name = file.split(".")
        img.save(f'static/resized_images/mobile/{name[0]}_mobile.jpg')


def tablet_photos():
    basewidth = 768
    for file in os.listdir("images/"):
        img = Image.open(f"images/{file}")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        name = file.split(".")
        img.save(f'static/resized_images/tablet/{name[0]}_mobile.jpg')

def image_conversion(request):
    mobile_photos()
    hd_photos()
    tablet_photos()
    template = 'home/result.html'
    context = {}
    return render(request, template, context)
