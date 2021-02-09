# Source: https://opensource.com/life/15/2/resize-images-python
import os
from PIL import Image
import time
start_time = time.time()

# scale by setting a height

# baseheight = 300
# for file in os.listdir("submission_upload/"):
#     img = Image.open(f"submission_upload/{file}")
#     hpercent = (baseheight / float(img.size[1]))
#     wsize = int((float(img.size[0]) * float(hpercent)))
#     img = img.resize((wsize, baseheight), Image.ANTIALIAS)
#     img.save(f'submission_upload/{file}')



# from PIL import Image

basewidth = 480
for file in os.listdir("submission_upload/"):
    img = Image.open(f"submission_upload/{file}")
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'submission_upload/{file}')

print("My program took", time.time() - start_time, "to run")