import cvlib as cv
import cv2
import sys
import os
import numpy as np

def detection(choice, filename, inputdir, outputdir):
    image = cv2.imread(inputdir) #python3 cv.py 860_main_beauty.png detect_face // python3 cv.py 860_main_beauty.png detect_gender
    print(image)
    if (choice=='detect_face'):
        faces, confidences = cv.detect_face(image) 
        print(faces)
        print(confidences)
        for face,conf in zip(faces,confidences):

            (startX,startY) = face[0],face[1]
            (endX,endY) = face[2],face[3]

            # draw rectangle over face
            cv2.rectangle(image, (startX,startY), (endX,endY), (0,255,0), 2)


    if (choice=='detect_gender'):
        face, conf = cv.detect_face(image)
        padding = 20
        
        for f in face:

            (startX,startY) = max(0, f[0]-padding), max(0, f[1]-padding)
            (endX,endY) = min(image.shape[1]-1, f[2]+padding), min(image.shape[0]-1, f[3]+padding)
            
            # draw rectangle over face
            cv2.rectangle(image, (startX,startY), (endX,endY), (0,255,0), 2)

            face_crop = np.copy(image[startY:endY, startX:endX])

            # apply gender detection
            (label, confidence) = cv.detect_gender(face_crop)

            print(confidence)
            print(label)

            idx = np.argmax(confidence)
            label = label[idx]

            label = "{}: {:.2f}%".format(label, confidence[idx] * 100)

            Y = startY - 10 if startY - 10 > 10 else startY + 10

            cv2.putText(image, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            
    if (choice=='video_to_frames'):
        cv.animate(frames, image)


    # save output
    cv2.imwrite(os.path.join(outputdir, filename), image)