#madem sys improt ettim argümanı neden sys ile almıyorum değil mi :D
#opens dataset
#checks each image in dataset
#automatically build class dirs for object detection
#assigns each classs image with keyboard
#deletes each assigned image on base dataset

#how to use?

import argparse
import cv2
import os
import sys
from tkinter import *
from PIL import Image, ImageTk


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--classnum", type=int, default=2)
parser.add_argument("-b", "--basedir", type=str, default=os.path.join(os.curdir,"dataset"))

args = vars(parser.parse_args())
print(type(args))

imgnums = [0] + [0]*args["classnum"]

for classnum in range(1,args["classnum"]+1):
    classdir = os.path.join(os.curdir, str(classnum))
    if not os.path.isdir(classdir):
        os.mkdir(classdir)
    imgnums[classnum] = len(os.listdir(classdir))
print("imgnums", imgnums)

def processing(img_file_name,taken_image,name_in_class):
    class_path = os.path.join(os.curdir,str(name_in_class))
    taken_image.save(os.path.join(class_path,img_file_name))
    imgnums[name_in_class] += 1
    os.remove(os.path.join(args["basedir"],img_file_name))
    window.destroy()

global window #bunu global koymamızın özel bir sebebi var mı?

for img_file_name in os.listdir(args["basedir"]):
    #build window
    window = Tk()
    window.geometry("1000x1500")
    img_path = os.path.join(args["basedir"],img_file_name)
    image = Image.open(img_path).resize((1000,800)) #ımageyi doğru yüklüyor
    photoimage = ImageTk.PhotoImage(image)
    lbl  = Label(window,image = photoimage)
    lbl.place(x=0,y=0)
    x_coordinate = 75
    y_coordinate = 750
    rel_x = 0.1
    rel_y = 0.05
    rel_height = 0.05
    rel_width = 0.1

    #place buttons on window
    for button_number in range(1,args["classnum"]+1):

        button = Button(window, text=button_number, command=lambda button_number=button_number:
        (processing(img_file_name, image, button_number)))
        button.place(x=x_coordinate, y=y_coordinate, relx=rel_x, rely=rel_y,
                     relheight=rel_height, relwidth=rel_width)


        if button_number % 5 != 0:
            x_coordinate += 150
        else:
            x_coordinate = 75
            y_coordinate += 75


    window.mainloop()

print("Done!")
for classnum in range(1,args["classnum"]+1):
    print("[INFO] Class {} have {} images".format(classnum, imgnums[classnum]))




