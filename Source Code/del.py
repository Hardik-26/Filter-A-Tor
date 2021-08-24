import os
import time
Home_path=os.environ["HOMEPATH"]+'\Desktop'
time.sleep(1)
for i in os.listdir(Home_path+'\CARTOON FRAMES'):
    os.remove(Home_path+'\CARTOON FRAMES'+'\\'+str(i))
time.sleep(1)
for ii in os.listdir(Home_path+'\FRAMES'):
    os.remove(Home_path+'\FRAMES'+'\\'+str(ii))
time.sleep(1)
os.rmdir(Home_path+'\FRAMES')
os.rmdir(Home_path+'\CARTOON FRAMES')
os.remove(Home_path+'\VID.mp4')
time.sleep(1)
print( ' !! DONE !! ')
time.sleep(100)
