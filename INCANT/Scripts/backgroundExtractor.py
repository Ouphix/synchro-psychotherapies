# This script make an exraction of the background with Open CV.
# It could help to improve the relevant fetures of motio history

import numpy as np
import cv2
cap = cv2.VideoCapture('/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/INCANT/Scripts/convertingVideos/avimovies/F1007A1.VOB.avi')


fgbg = cv2.BackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
#    ball=fgmask[1:500,1:500]
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
#    cv2.imshow('frame2',ball)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
