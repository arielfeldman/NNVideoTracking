import numpy as np
#saving frames of video as jpgs
import cv2
import imageio
import scipy.misc

# Open the data file
npzfile = np.load("/home/kemerelab/Ariel/NNTrackingVids/12-22-2016-1.npz")
npzfile.files

# Break the points of the bounding boxes into two numpy arrays
topleft = npzfile['tl']
bottomright = npzfile['br']

# topleft.shape,bottomright.shape
# topleft[:,1]

# Checking the format of the filenames
# for i in range(12):
#     print("moo{:06d}".format(i))

# Checking that two coordinates are stored in the position for each frame
# print(topleft[415])

#xml formatting
for i in range(0,topleft.shape[0]):
    f = open("LongEvansdevkit/LongEvans/Annotations/{:06d}.xml".format(i+1),"w+")
    f.write("<annotation>\n")
    f.write("\t<folder>LongEvans</folder>\n")
    f.write("\t<filename>{:06d}.jpg</filename>\n".format(i+1))
    f.write("\t<size>\n")
    f.write("\t\t<width>1280</width>\n")
    f.write("\t\t<height>720</height>\n")
    f.write("\t\t<depth>3</depth>\n")
    f.write("\t</size>\n")
    f.write("\t<object>\n")
    f.write("\t\t<name>rat</name>\n")
    f.write("\t\t<bndbox>\n")
    f.write("\t\t\t<xmin>{:d}</xmin>\n".format(topleft[i,0]))
    f.write("\t\t\t<ymin>{:d}</ymin>\n".format(topleft[i,1]))
    f.write("\t\t\t<xmax>{:d}</xmax>\n".format(bottomright[i,0]))
    f.write("\t\t\t<ymax>{:d}</ymax>\n".format(bottomright[i,1]))
    f.write("\t\t</bndbox>\n")
    f.write("\t</object>\n")
    f.write("</annotation>")
    f.close()

reader = imageio.get_reader("/home/kemerelab/Ariel/NNTrackingVids/12-22-2016-1.mkv")
cnt=0
for i, im in enumerate(reader):
    cnt+=1
    im =  cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    scipy.misc.imsave("LongEvansdevkit/LongEvans/JPEGImages/{:06d}.jpg".format(cnt), im)

# #just checking real quick!
# from PIL import Image, ImageDraw
# im = Image.open("LongEvansdevkit/LongEvans/JPEGImages/000001.jpg")
# draw = ImageDraw.Draw(im)
# draw.rectangle([(597,385),(654,551)])
# im.show()