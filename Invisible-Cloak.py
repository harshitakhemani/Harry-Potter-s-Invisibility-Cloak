import cv2
# THIS IS MY WEBCAM
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()   # READING FROM MY WEBCAM
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()