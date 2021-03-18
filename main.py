import cv2
import yolo
capture= cv2.VideoCapture(0)
frame_width=capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height=capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=capture.get(cv2.CAP_PROP_FPS)

print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

if capture.isOpened() is False:
    print("Error opening camera")

ret,frame=capture.read()
if ret is True:
    detected=yolo.humanDetect(frame)
    if detected is not None:
        cv2.imshow("human detected",detected)
        cv2.imwrite("human.jpg", detected) # extra line added. This saves the image. Which will be used for face detection.
        cv2.waitKey()
    else:
        print('Human Not detected')
capture.release()
cv2.destroyAllWindows()