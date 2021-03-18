import cv2 as cv

# Read image from your local file system
original_image = cv.imread('E:\SEM_2\VR\mini project\VR-mini-project-1\human.jpg')  
# use the appropriate paths to the human.jpg image.

# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('E:\SEM_2\VR\mini project\VR-mini-project-1\haarcascade_frontalface_alt.xml') 
# use the appropriate path to haarcascade filter.

detected_faces = face_cascade.detectMultiScale(grayscale_image)

for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )
    crop= original_image[row:row+height,column:column+width]
    cv.imwrite("face.jpg", crop)

cv.imshow('face_detected', original_image)
cv.waitKey(0)
cv.destroyAllWindows()