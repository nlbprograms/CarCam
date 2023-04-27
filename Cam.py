# inports
import numpy as np
import cv2

# Varibles
cap = cv2.VideoCapture(0)
cap.set(3,850)
cap.set(4,400)
w = 200

# code
while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame',frame)

        cv2.waitKey(w)

        if cv2.waitKey(20) & 0xFF == ord('q'):
                 break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
