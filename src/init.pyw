#|=============================================================================================================
#|                                                                                                          " FILTER-A-TOR"                                                                                                                         |
#|=============================================================================================================


#|---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This program  will convert a video to looks like its hand animated.
# There are 2 filter options: 1. Cartoon-ish filter & 2. Sketch Filter. 
# It uses "OpenCV" to do the same.
# Author : Hardik Shah.
#|---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#|=============================================================================================================


# IMPORTS ---------------------------------------------
import cv2
import numpy as np
import os
from tkinter import Tk
import tkinter as tk
import shutil
from tkinter import filedialog
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import time
#----------------------------------------------------------


#PRE-REQ -----------------------------------------------------

Home_path=os.environ["HOMEPATH"]+'\Desktop'

# Tkr Window---------------------------------------------------

def browse_files():
    global video_path
    video_path.set(filedialog.askopenfilename())

def submit():
    global video_path, radio_var,filename,flt
    filename=video_path.get()
    flt=radio_var.get()
    root.destroy()
    

root = tk.Tk()
root.geometry("275x250")
root.title("Select Video")

# Video path field
video_path = tk.StringVar()
video_path_entry = tk.Entry(root, textvariable=video_path)
lbl = Label(root, text = "Video Path:  ",font = ("Arial Bold",10)).place(x=5,y=29)
video_path_entry.place(x=95,y=29)

# Browse button
photoimage =  PhotoImage(file = "IOC.png")
browse_button = tk.Button(root, text="Browse",image =photoimage ,command=browse_files)
browse_button.place(x=230, y=25)

# Radio buttons
radio_var = tk.StringVar()
lbl1 = Label(root, text = "Filter Options-  ",font = ("Arial Bold",10)).place(x=5,y=75)
option1 = tk.Radiobutton(root, text="Cartoon-ish Filter", variable=radio_var, value="1").place(x=15,y=100)
option2 = tk.Radiobutton(root, text="Sketch Filter", variable=radio_var, value="sketch").place(x=15,y=130)
# Submit button
submit_button = tk.Button(root, text="Submit",font = ("Arial Bold",10),command=submit).place(x=110,y=170)

root.mainloop()

#--------------------------------------------------------------
cap= cv2.VideoCapture(filename) #------------ VideoPath
fff=cap.get(cv2.CAP_PROP_FPS)
fps=int(fff)
#-----------------------------------------------------------------


# COLLECT FRAMES------------------------------------------------------------
def Frame():
    os.chdir(Home_path)
    os.mkdir(Home_path+'\FRAMES')
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
                break
        # Send 'frame' to filter function-
        filter_fun(frame,i)
        i+=1
    cap.release()
    cv2.destroyAllWindows()
#---------------------------------------------------------------------------------

# Apply Filter----------------------------------------------------------------------
def filter_fun(frame,y):
    if flt=="1":
        img = frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 4) 
        color = cv2.bilateralFilter(img, 1, 250, 250)
        result = cv2.bitwise_and(color, color, mask=edges)
        os.chdir(Home_path+'\FRAMES')
        cv2.imwrite(str(y)+'.jpg',result)
    else:
        img = frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(5,5),0)
        edges = cv2.Canny(gray, 10, 60)
        result = cv2.bitwise_not(edges)
        os.chdir(Home_path+'\FRAMES')
        cv2.imwrite(str(y)+'.jpg',result)
    cv2.destroyAllWindows()
#------------------------------------------------------------------------------------

#COMPILE VIDEO--------------------------------------------------------------
def Compile():
    try:
        os.remove('filter_Video.mp4')
    except:
        pass
    os.chdir(Home_path)
    l1=os.listdir(Home_path+'\FRAMES')
    img_array = []
    path2=Home_path+'\FRAMES'
    for x in range(len(l1)):
        img = cv2.imread(path2+'\\'+str(x)+".jpg")
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    out = cv2.VideoWriter('filter_Video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), int(fps), size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    cv2.destroyAllWindows()

#-------------------------------------------------------------------------------------

#=================================================
#                                            RUNNER CODE                                           |
#=================================================
Frame()
time.sleep(0.2)
Compile()
cv2.destroyAllWindows()
os.chdir(Home_path)
root = tk.Tk()
root.title("Done")
l=Label(root, text = " Video Compiled. \n Project By- Hardik Shah ",font = ("Arial Bold",12)).pack()
root.mainloop()
#-------------------------------------------------------------------------------------
