import cv2
import numpy as np

# Function to calculate the angle between three points
def calculate_angle(start, end, far):
   
    a = np.array(start)
    b = np.array(end)
    c = np.array(far)

    ab = b - a
    bc = c - b

    dot_product = np.dot(ab, bc)
    
    magnitude_ab = np.linalg.norm(ab)
    magnitude_bc = np.linalg.norm(bc)

    angle = np.arccos(dot_product / (magnitude_ab * magnitude_bc))

    angle = np.degrees(angle)

    return angle

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(15,15),0)

    _, thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse=True)

    if contours:
        hand_contour = contours[0]
        hull = cv2.convexHull(hand_contour)
        
        hull_defects = cv2.convexityDefects(hand_contour,cv2.convexHull(hand_contour,returnPoints=False))
        if hull_defects is not None:
            count_fingers = 0
            for i in range(hull_defects.shape[0]):
                s,e,f,d = hull_defects[i,0]
                start = tuple(hand_contour[s][0])
                end = tuple(hand_contour[e][0])
                far = tuple(hand_contour[f][0])

                angle =calculate_angle(start,end,far)
                if angle <= 90 and d>1000:
                    count_fingers +=1
            print("Fingers detected: ",count_fingers)

        cv2.drawContours(frame, [hull], 0,(0,255,0),0)

    cv2.imshow("Hand Gesture Recognotion",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

capture.release()
cv2.destroyAllWindows()