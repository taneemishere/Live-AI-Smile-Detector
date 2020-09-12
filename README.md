# Live-AI-Smile-Detector
An AI application that can detect the smile on the face(s) in real time i-e from a webcam or even a captured video.

## Requirements

Apart from installing [Python](https://www.python.org), you need to install the [OpenCV](https://www.docs.opencv.org) and you're good to go.

## The Classifiers

The "haarcascade_frontalface_default" is a pre-trained classifier that is used to detect faces in a frame. Also the "haarcascade_smile" is a pre-trained classifier that works the same way and is used to detect smiles on the faces.

## The Code Flow
-	Import the most important OpenCv
-	Initialized the face and the smile detection classifiers and save it in the ```face_detector```, ```smile_detector``` respectively.
-	Capture the webcam frames in the ```webcam```
-	Now loop until the webcam is stopped and this continues
	-	Read the points from the webcam
	-	If something odd occurs, break out of the loop
	-	Otherwise, convert the frame to Black and White (for opimization)
	-	Detect faces in the frame, the Black and White frame
	-	Draw the rectangle over the face(s) in the frame
	-	Slicing the frame, ```the_face = frame[y:y + h, x:x + w]```, here we're cropping the whole frame into the sub-image in which we have only the faces.
	- 	Now convert that face' frame into Black and White
	-	Detect the smiles within the faces' frame, which we converted in previous step
	-	If want to have a rectangle over the smile you can
	-	Now label "smiling" the face, if it detects the smile on the faces
	-	Show the frame titling the "Live AI Smile Detector "
	-	The ```cv2.waitkey(1)``` waits 1 milli second and then press the key to change the frame. If there is no argument you will need to press the key manually to change from frame to frame
	-	At last release everything so that the operating system will come to know to free up the spaces

-	And that's pretty much it

## License

This project is licensed under the MIT Open Source License.
