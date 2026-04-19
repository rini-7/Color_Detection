import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)


#NOISE REMOVAL:
#Think of it as a sponge that cleans up the noise, (5x5 matrix, defines neighbourhood of morphological operations

kernel = np.ones((5,5),np.uint8)

while True:
    ret, frame = capture.read()

    hsvImage = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

#to get a mask from all pixels that belong to the color we wanna detect

    lower_blue = np.array([95, 60, 60])
    upper_blue = np.array([130, 255, 255])
    mask_blue = cv.inRange(hsvImage, lower_blue, upper_blue)

    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])
    mask_green = cv.inRange(hsvImage, lower_green,upper_green)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red = cv.inRange(hsvImage, lower_red1, upper_red1) + \
    cv.inRange(hsvImage, lower_red2, upper_red2)

    def clean(mask):
        #Removes noise (white dots) but keeps the image
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        #Fills in the holes (black spaces after the white dots are removed)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel) 
        return mask
    
    mask_blue = clean(mask_blue)
    mask_green = clean(mask_green)
    mask_red = clean(mask_red)

#BOUNDING BOX:
#cv.RETR_EXTERNAL -> retrieves outer corners of the white mask
#cv.CHAIN_APPROX_SIMPLE -> retains shape's structure but compresses contour data, keeps diagonals, straight lines.
    def detect_label(mask, color_name, box_color):
        contours,_=cv.findContours(mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv.contourArea(cnt)>1500: #threshold 
                x,y,w,h=cv.boundingRect(cnt)
                cv.rectangle(frame,(x,y),(x+w,y+h),box_color,3) #3 -> thickness
                cv.putText(frame,color_name,(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.7,box_color,3)
    detect_label(mask_blue,"BLUE",(255,0,0))
    detect_label(mask_green,"GREEN",(0,255,0))
    detect_label(mask_red,"RED",(0,0,255))
    
    combined_mask = mask_blue+mask_green+mask_red
    result = cv.bitwise_and(frame,frame,mask=combined_mask)

    cv.imshow("Frame ",frame)
    cv.imshow("Mask",combined_mask)
    cv.imshow("Result",result)
    if ret:
        cv.imshow('Webcam',frame)
    if cv.waitKey(1)==ord('q'):
        break

capture.release()
cv.destroyAllWindows()

print(np.sum(combined_mask))


