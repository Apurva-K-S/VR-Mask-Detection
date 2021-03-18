import cv2 as cv

def faceDetect(image):
    # Convert color image to grayscale for Viola-Jones
    grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Load the classifier and create a cascade object for face detection
    face_cascade = cv.CascadeClassifier('E:\SEM_2\VR\mini project\VR-mini-project-1\haarcascade_frontalface_alt.xml') 
    # use the appropriate path to haarcascade filter.

    detected_faces = face_cascade.detectMultiScale(grayscale_image)

    if(len(detected_faces)!=0):
        for (column, row, width, height) in detected_faces:
            cv.rectangle(
                image,
                (column, row),
                (column + width, row + height),
                (0, 255, 0),
                2
            )
            face_detected = image[row:row+height,column:column+width]

        return face_detected
    else:
        return None