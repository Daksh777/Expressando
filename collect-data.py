import cv2
import os

if not os.path.exists("data"): #True
    os.makedirs("data")
    os.makedirs("data/train") 
    os.makedirs("data/test")
    os.makedirs("data/train/rock") 
    os.makedirs("data/train/paper")
    os.makedirs("data/train/scissor")
    os.makedirs("data/train/none")
    os.makedirs("data/test/rock")
    os.makedirs("data/test/paper")
    os.makedirs("data/test/scissor")
    os.makedirs("data/test/none")
    
 
mode = 'TRAIN' 
directory = 'data/'+mode+'/' #data/train/

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    cv2.putText(frame, "Expressando - TDOC 2021", (175, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)

    count = {'rock': len(os.listdir(directory+"/rock")), 
             'paper': len(os.listdir(directory+"/paper")),
             'scissor': len(os.listdir(directory+"/scissor")),
             'none': len(os.listdir(directory+"/none"))} 
    
    cv2.putText(frame, "MODE : "+ mode, (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT:", (10, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (225,255,255), 1)
    cv2.putText(frame, "ROCK : "+str(count['rock']), (10, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "PAPER : "+str(count['paper']), (10, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "SCISSORS : "+str(count['scissor']), (10, 160), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    cv2.putText(frame, "NONE : "+str(count['none']), (10, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
    
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,3)
    roi = frame[y1:y2, x1:x2] 
    roi = cv2.resize(roi, (200, 200)) 
    cv2.putText(frame, "R.O.I", (440, 350), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,225,0), 2)
    cv2.imshow("Frame", frame)

    
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 1)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10) 
    if interrupt & 0xFF == 27:
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'rock/'+str(count['rock'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'paper/'+str(count['paper'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'scissor/'+str(count['scissor'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'none/'+str(count['none'])+'.jpg', roi)
    
cap.release()
cv2.destroyAllWindows()