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

Basically a divide and conquer algorithm. ☺

---------------------------------------------------------------------------------------------------

## NOTE-
◙ Make Sure All The File Are On Your Desktop Before Executing The Program.
<br>
◙ Try with smaller videos (less than 10 seconds long), Longer and larger video files 
  will take forever and may crash the interpreter.

---------------------------------------------------------------------------------------------------
<br>

## GUI Window-

<br>

![GUI](https://user-images.githubusercontent.com/89474886/217238584-a2762d90-8cdb-4481-8989-04491f570fb7.png)


<br>

## Example Input Video-

<br>

https://user-images.githubusercontent.com/89474886/217241857-91603541-95cc-4296-8a98-b512a5002732.mp4

<br>

## Example output-


<br>


https://user-images.githubusercontent.com/89474886/217243376-b10dc64d-c275-4086-a51b-cb2f6b282630.mp4



THANK YOU :)
