#madem sys improt ettim argümanı neden sys ile almıyorum değil mi :D
#opens dataset
#checks each image in dataset
#automatically build class dirs for object detection
#assigns each classs image with keyboard
#deletes each assigned image on base dataset

import argparse
import cv2
import os
import sys
from tkinter import *
from PIL import Image, ImageTk


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--classnum", type=int, default=8)
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

def processing(taken_img,taken_imge,name_in_class):
    class_path = os.path.join(os.curdir,str(name_in_class))
    taken_imge.save(os.path.join(class_path,str(imgnums[classnum])+".jpg"))
    imgnums[name_in_class] += 1
    os.remove(os.path.join(args["basedir"],taken_img))
    window.destroy()

global window

for img in os.listdir(args["basedir"]):
    window = Tk()
    window.geometry("1000x1500")
    imge = (Image.open(os.path.join(args["basedir"],img))).resize((1000,800))
    image = ImageTk.PhotoImage(imge)
    lbl  = Label(window,image = image)
    lbl.place(x=0,y=0)
    x_coordinate = 75
    y_coordinate = 750
    rel_x = 0.1
    rel_y = 0.05
    rel_height = 0.05
    rel_width = 0.1
    for button_number in range(1,args["classnum"]+1):
        if button_number % 5 != 0 :
            button = Button(window, text = button_number ,command = lambda button_number=button_number:
                         (processing(img,imge,button_number)))
            button.place(x = x_coordinate, y = y_coordinate,relx = rel_x,rely = rel_y,
                         relheight = rel_height,relwidth = rel_width)


            x_coordinate += 150
        else :
            button = Button(window, text = button_number ,command = lambda button_number=button_number:
                         (processing(img,imge,button_number)))
            button.place(x = x_coordinate, y = y_coordinate,relx = rel_x,rely = rel_y,
                         relheight = rel_height,relwidth = rel_width)

            x_coordinate = 75
            y_coordinate += 75


    window.mainloop()

print("Done!")
for classnum in range(1,args["classnum"]+1):
    print("[INFO] Class {} have {} images".format(classnum, imgnums[classnum]))


