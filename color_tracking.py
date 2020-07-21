import cv2
import numpy as np 

#define font style
font = cv2.FONT_HERSHEY_SIMPLEX

#capture video
video = cv2.VideoCapture("pacman.webm")

while True:
    #capture a frame
    video_return, frame = video.read()

    #verify video status
    if not video_return:
        exit()

    #lower and upper limits of the desired color (yellow)
    lower_range = np.array([0,220,220], dtype=np.uint8)
    upper_range = np.array([50,255,255], dtype=np.uint8)

    #create a mask using ranges
    mask = cv2.inRange(frame, lower_range, upper_range)
    
    #find mask contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        #create a rectangle with the contours limits
        (x,y,w,h) = cv2.boundingRect(contour)
        if w > 25 and h > 25:
            #print rectangle in the frame
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4, cv2.LINE_AA)
            #print the text with the coordinates
            image = cv2.putText(frame, "x: " + str(x) + " - y: " + str(y), (x+5, y-5), font, .8, [255,255,255], 1, cv2.LINE_AA)
            #segment the detected area in a small image
            cv2.imshow("Sliced Image", frame[y:y+h, x:x+w])
    
    #show the frame tracking the pacman
    cv2.imshow("frame", frame)

    #wait until a key is pressed
    c = cv2.waitKey(15)

    if c == ord("q"):
        break

cv2.destroyAllWindows