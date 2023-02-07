# Filter-A-Tor

--------------------------------------------------------------------------------------------------------
Filter-A-Tor is a Python project that will add a filter to any video. 
This program uses Open-CV to essentially change the video to apply a filter to each frame of the video.
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------

◙ REQUIREMENTS-

tkinter 

time 

Open-cv2 (pip install opencv-python)

numpy (pip install numpy)

moviepy.editor (pip install moviepy)

---------------------------------------------------------------------------------------------------

◙ Basic Program Process-

First the program breaks down the video into frame (A 5 second video with 30fps will have around 150 frames),
each frame(jpeg data) is then passed to a function that applies the chosen filter to the image and saves
the image file in a directory. 
After all frames have passed through the function, all the filtered-frames are read and compiled back into a video.

---------------------------------------------------------------------------------------------------
 
◙ NOTE- Make sure all the file are on your desktop Before executing the program.

---------------------------------------------------------------------------------------------------
<br>

## Example Input Video-

<br>

https://user-images.githubusercontent.com/89474886/164997998-28037e64-62e6-41e6-b4f9-fba8588c5df9.mp4

<br>

## Example output-

<br>

https://user-images.githubusercontent.com/89474886/164998212-e98dabc9-1b42-464c-8fd7-525c5c4a6006.mp4

THANK YOU :)
