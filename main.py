import cv2
import yolo
import Detect
capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
	print("Error opening camera")
ret,frame=capture.read()
if ret is True:
	detected=yolo.humanDetect(frame)

	if detected is not None:
    	
		#cv2.imshow("human detected",detected)
		#cv2.waitKey()
		print("Human Detected")
		face = Detect.detect_face(detected)
		if face is not None:
			cv2.imshow("face", face)
			mask = Detect.detect_mask(face)
			print(mask)
		else:
			print('face not detected')

	else:
		print('Human Not detected')

capture.release()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
