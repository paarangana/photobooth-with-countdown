import cv2 as cv

capture=cv.VideoCapture(1)
count=1
text=True

if not capture.isOpened():
    print("Could not open webcam.")
    exit()

while True:
    isTrue, frame=capture.read()
    if not isTrue:
        print("cannot read frame")
        continue

    frame = cv.flip(frame, 1)

    if text:
        cv.putText(frame, "press 's' to take a photo", (100,100),cv.FONT_HERSHEY_PLAIN, 6, 0, 2, cv.LINE_AA)
        cv.putText(frame, "press 'w' to exit", (100,170),cv.FONT_HERSHEY_PLAIN, 6, 0, 2, cv.LINE_AA)
    cv.imshow('webcam',frame)
   


    key= cv.waitKey(1)

    if key == ord('s'):
        text=False
        print("Ready?")
        cv.waitKey(1000)
        x=0
        for i in range(3, 0 , -1):
            ret,frame=capture.read()
            frame = cv.flip(frame, 1)
            if not ret:
                break
            cv.putText(frame, str(i), (600+x,500),cv.FONT_HERSHEY_PLAIN, 10, 0, 2, cv.LINE_AA)
            cv.imshow('webcam',frame)
            cv.waitKey(1000)
            x=x+100
        ret, frame= capture.read()
        frame = cv.flip(frame, 1)
        if ret:
            img_save="photo_"+str(count)+".jpg"
            cv.imwrite(img_save, frame)
            count = count + 1

        text=True
    elif key == ord('w'):
        print("exiting the photobooth...")
        break

capture.release()
cv.destroyAllWindows()


