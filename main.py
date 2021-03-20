import cv2
import YOLO
import Detect
capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
	print("Error opening camera")
ret,frame=capture.read()
if ret is True:
	detected=YOLO.humanDetect(frame)

	if detected is not None:
    	
		#cv2.imshow("human detected",detected)
		#cv2.waitKey()
		print("Human Detected")
		face = Detect.detect_face(detected)
		cv2.imshow("face", face)
		mask = Detect.detect_mask(face)
		print(mask)

	else:
		print('Human Not detected')

capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
