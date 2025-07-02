# Photo Booth: with countdown and mirroring using OpenCV

This is a python-based OpenCV project which captures photos when a button is pressed using your webcam. It has the following features:

- Live webcam video capturing
- Mirrored webcam for selfie-like feeling
- Capturing of photo and exiting of app with just a key press
- Automatic image saving with incremented file names (saved in same directory where the script is run)

Main functions used:

- cv.VideoCapture(): accesses webcam
- cv.flip(): used this function to mirror the webcam feed horizontally
- cv.putText(): puts text onto the live webcam feed
- cv.waitKey(): used to put a one second delay during the countdown
- cv.imwrite(): used to save the captured photo as a file
- cv.imshow(): displays the webcam feed
- cv.read(): captures webcam frames in real time


