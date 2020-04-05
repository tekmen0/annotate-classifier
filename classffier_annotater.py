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

for img in os.listdir(args["basedir"]):
    cv2.namedWindow("image", flags=cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 1000, 1000)
    image = cv2.imread(os.path.join(args["basedir"], img))
    cv2.imshow("image", image) #yakınlaştırıp uzaklaştırabilen ekra)

    keyboard = cv2.waitKey()
    if keyboard == 27: sys.exit()

    for classnum in range(1, args["classnum"]+1):
        if keyboard == ord(str(classnum)):
            class_path = os.path.join(os.curdir, str(classnum))
            cv2.imwrite(os.path.join(class_path,str(imgnums[classnum])+".jpg"), image)
            imgnums[classnum] += 1
            #delete image on basedir
            os.remove(os.path.join(args["basedir"], img))
            cv2.destroyAllWindows()

cv2.destroyAllWindows()

print("Done!")
for classnum in range(1,args["classnum"]+1):
    print("[INFO] Class {} have {} images".format(classnum, imgnums[classnum]))





