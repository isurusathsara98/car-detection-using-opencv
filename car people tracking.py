import cv2
img_file='Car Image.jpg'
#edit the video name that you have in your folder
video = cv2.VideoCapture('Tesla Dashcam Accident.mp4')

classifier_file='car_detector.xml'
car_tracker = cv2.CascadeClassifier(classifier_file)
while True:
    (read_successful, frame) = video.read()

    if read_successful:
       grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    else:
        break
    
    cars = car_tracker.detectMultiScale(grayscaled_frame)

    for(x, y, w, h) in cars:
        cv2.rectangle(frame,(x,y),(x+w, y+h),(0, 0, 255), 2)
        
    cv2.imshow('car detector', frame)
    
    cv2.waitKey(1)

    #below commented code helps you to process a photo instead of a video
"""
img=cv2.imread(img_file)

car_tracker = cv2.CascadeClassifier(classifier_file)

black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_tracker.detectMultiScale(black_n_white )

for(x, y, w, h) in cars:
    cv2.rectangle(img,(x,y),(x+w, y+h),(0, 0, 255), 2)

cv2.imshow('car detector', img)

cv2.waitKey()
"""

print("code completed")