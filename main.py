import cv2


# Face and Smile Classifiers
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

# Catching the webcam feed, the argument is default for webcam,
# we can provide a video as well
webcam = cv2.VideoCapture(0)

while True:
    # Reading the current frame from web-cam
    # The successful_frame_read is boolean and frame is an array
    successful_frame_read, frame = webcam.read()

    # if there is an error break out of the loop
    if not successful_frame_read:
        break

    # Change to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting the faces, This returns the array of points
    faces = face_detector.detectMultiScale(frame_grayscale)

    # print(faces)

    # Looping for face in the frame
    for (x, y, w, h) in faces:
        # Draw rectangle around the faces        color of rectangle and 4px thickness
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 200, 50), 4)

        # This is our face' frame
        # The sub frame using the numpy n-dimensional array slicing
        the_face = frame[y:y + h, x:x + w]

        # Converting the face to bNw
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        # Detecting the smiles within face, this returns the array of points
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        # for (x_, y_, w_, h_) in smiles:
        #    Draw rectangle around the smiles
        #    cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (50, 50, 200), 4)

        # Label the face as smiling
        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=2,
                        fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

    cv2.imshow("Live AI Smile Detector", frame)

    # Display
    cv2.waitKey(1)

# Releasing!
webcam.release()
cv2.destroyAllWindows()

print("End Of program")
