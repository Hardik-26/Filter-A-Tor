#|=================================================================================================================================================================================|
#|                                                                               " AI ANIMATOR "                                                                                                  |
#|=================================================================================================================================================================================|

#|---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This program  will convert a video to looks like its hand animated.
# It uses "OpenCV" AI to do the same.
# Time taken to complete this project- 14 Hrs.
#|---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#|=================================================================================================================================================================================|


# IMPORTS ---------------------------------------------
import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time
import moviepy.editor as moviepy
#----------------------------------------------------------


# PRE-REQ -----------------------------------------------------
Home_path=os.environ["HOMEPATH"]+'\Desktop'
print(' SELECT VIDEO FILE ')
print()
Tk().withdraw()
filename = askopenfilename()
cap= cv2.VideoCapture(filename) #------------ VideoPath
fff=cap.get(cv2.CAP_PROP_FPS)
fps=int(fff)
#-----------------------------------------------------------------


# COLLECT FRAMES------------------------------------------------------------
def Frame():
    print('PROGRESS: 0%')
    os.chdir(Home_path)
    os.mkdir('FRAMES')
    os.chdir(Home_path+'\FRAMES')
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
                break
        cv2.imwrite(str(i)+'.jpg',frame)
        i+=1
    cap.release()
    cv2.destroyAllWindows()
    print()
    print('PROGRESS: 25%')
#---------------------------------------------------------------------------------

# CARTOONIZE----------------------------------------------------------------
def cartoon():
    os.mkdir(Home_path+'\CARTOON FRAMES')
    os.chdir(Home_path+'\FRAMES')
    no=0
    FL=[]
    l2=os.listdir(Home_path+'\FRAMES')
    for ll in range(len(l2)):
        FL.append(str(ll)+'.jpg')
    for y in FL:
        os.chdir(Home_path+'\FRAMES')
        path=Home_path+'\FRAMES'
        img = cv2.imread(path+'\\'+str(y))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 999999,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4) 
        color = cv2.bilateralFilter(img, 1, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        os.chdir(Home_path+'\CARTOON FRAMES')
        cv2.imwrite(str(no)+'.jpg',cartoon)
        no=no+1
    cv2.destroyAllWindows()
    print()
    print('PROGRESS: 50%')
#---------------------------------------------------------------------------------

#COMPILE VIDEO--------------------------------------------------------------
def Compile():
    os.chdir(Home_path)
    l1=os.listdir(Home_path+'\CARTOON FRAMES')
    fileL=[]
    img_array = []
    for l in range(len(l1)):
        fileL.append(str(l)+'.jpg')
    l1=None
    path2=Home_path+'\CARTOON FRAMES'
    for x in fileL:
        img = cv2.imread(path2+'\\'+x)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    out = cv2.VideoWriter('VID.mp4',cv2.VideoWriter_fourcc(*'DIVX'), int(fps), size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    cv2.destroyAllWindows()
    print()
    print('PROGRESS: 75%')
#-------------------------------------------------------------------------------------

#=================================================
#                  RUNNER CODE                   |
#=================================================

print('PLEASE WAIT TILL THE PROCEES IS OVER.')
print()
Vfile=moviepy.VideoFileClip(filename) #-----------------EXTRACTING AUDIO
audioclip=Vfile.audio.copy() #---------------------------↗
Frame()
time.sleep(1)
cartoon()
time.sleep(1)
Compile()
cv2.destroyAllWindows()
os.chdir(Home_path)
videoclip = moviepy.VideoFileClip(Home_path+'\\'+'VID.mp4')
clip = videoclip.set_audio(audioclip)
clip.write_videofile(Home_path+'\\'+'Cartoon.mp4')
print()
print('PROGRESS: 99%')
print()
time.sleep(3)
os.system('del.pyc')
#-------------------------------------------------------------------------------------


#|=================================================================================================================================================================================|
#|                                                                                  CODE END                                                                                                        |
#|=================================================================================================================================================================================|
