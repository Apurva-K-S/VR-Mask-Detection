import cv2
import yolo
import face_detection

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
        #cv2.imshow("human detected",detected)
        face_detected = face_detection.faceDetect(detected)
        if face_detected is not None:
            cv2.imshow("face detected",face_detected)
        else:
            print('face not detected')
    else:
        print('Human Not detected')

capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()