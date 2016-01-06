import ipdb
import numpy as np
import cv2

cap = cv2.VideoCapture(-1)

# darker_green = np.uint8([[[65, 83, 62]]])
# lighter_green = np.uint8([[78, 92, 67]])

while(True):

    # Might want to check cap.isOpened()

    # Capture frame-by-frame
    success, frame = cap.read()

    # Our operations on the frame come here
    # hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv_frame = frame

    # Display the resulting frame
    cv2.imshow('iRoboCop - Your computer is infected!!', hsv_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# If you want to save the image
# cv2.imwrite('first_image.png', frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

