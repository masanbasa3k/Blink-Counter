import install_requirements

import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture('Video.mp4')
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640,360,[20,50])


idList = [22,23,24,26,110,157,158,159,160,161,130,243]
ratioList = []

blinkCount = 0
counterTime = 0
color = (255,0,255)

run = True
while run:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    img, faces = detector.findFaceMesh(img,draw=False)

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 5, color, cv2.FILLED)

        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]

        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img, leftUp, leftDown, (0,200,0), 3)
        cv2.line(img, leftLeft, leftRight, (0,200,0), 3)

        ratio = int((lenghtVer / lenghtHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = (sum(ratioList) / len(ratioList))

        if ratioAvg < 33 and counterTime == 0:
            blinkCount += 1
            counterTime = 1
            color = (0,255,0)
        if counterTime != 0:
            counterTime += 1
            if counterTime > 10:
                counterTime = 0
                color = (255,0,255)

        cvzone.putTextRect(img,f'Blink Count : {blinkCount}', (50,50), colorR=color)

        imgPlot = plotY.update(ratioAvg,color)
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, imgPlot], 1, 1)

    else:
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, img], 1, 1)
    
    cv2.imshow('Image',imgStack)
    cv2.waitKey(25)