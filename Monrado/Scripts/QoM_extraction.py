import sys, os
import numpy as np
import cv, cv2
import matplotlib.pyplot as plt
import pandas as pd
from scipy import fftpack
import matplotlib.mlab as mlab

def QoM( buff, th=0.05, kernel=3):
    motion_image = buff[-1] * float(len(buff))
    for buffered_img in buff:
        motion_image -= buffered_img
    motion_image /= float(len(buff))
    binary = (np.abs(motion_image) > th) * np.uint8(255)
    median = cv2.medianBlur( binary, kernel) /255.0
    return median


def elab( filename, padding_x=0, padding_y=0):
    tl_buff = []
    bl_buff = []
    tr_buff = []
    br_buff = []
    buff_len = 10

    fps = 25.0
    t = 0.0

    feats = { "t": [], "PA_top": [], "PA_bottom": [], "PSY_top": [], "PSY_bottom": []}
    ts = dict(feats)

    cap = cv2.VideoCapture(filename)
    print filename
    print cap.isOpened()
    show_t = True

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret: break
		
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

        half = gray[:,gray.shape[1]/2:] /255.0
        if padding_x > 0:
            half = half[padding_x:-padding_x,:]
        if padding_y >0:
            half = half[:,:-padding_y]
            
        #half = gray[padding_x:-padding_x,gray.shape[1]/2:-padding_y] /255.0
        #half = cv2.medianBlur(half,3)/255.0

        left = half[:,:half.shape[1]/2]
        right = half[:,half.shape[1]/2:]

        top_left = left[:left.shape[0]/2,:]
        bottom_left = left[left.shape[0]/2:,:]
        top_right = right[:right.shape[0]/2,:]
        bottom_right = right[right.shape[0]/2:,:]

        tl_buff.append(top_left)
        bl_buff.append(bottom_left)
        tr_buff.append(top_right)
        br_buff.append(bottom_right)
        if len(tl_buff)>=buff_len:
            tl_buff.pop(0)
            bl_buff.pop(0)
            tr_buff.pop(0)
            br_buff.pop(0)

        s_top_left = QoM( tl_buff)
        s_bottom_left = QoM( bl_buff)
        s_top_right = QoM( tr_buff)
        s_bottom_right = QoM( br_buff)


        ts["t"].append(t)
        ts["PA_top"].append( np.sum(s_top_left)/(top_left.shape[0]*top_left.shape[1]) )
        ts["PA_bottom"].append( np.sum(s_bottom_left)/(bottom_left.shape[0]*bottom_left.shape[1]) )
        ts["PSY_top"].append( np.sum(s_top_right)/(top_right.shape[0]*top_right.shape[1]) )
        ts["PSY_bottom"].append( np.sum(s_bottom_right)/(bottom_right.shape[0]*bottom_right.shape[1]) )
        t += 1/fps

        cv2.imshow('frame',half)
        #cv2.imshow('left',left)
        #cv2.imshow('right',right)
        cv2.imshow('silhouette top left', s_top_left)
        cv2.imshow('silhouette bottom left', s_bottom_left)
        cv2.imshow('silhouette top right', s_top_right)
        cv2.imshow('silhouette bottom right', s_bottom_right)

        cv2.waitKey(1)


        if (int(t)%60 == 0):
            if (show_t):
                print int(t/60)
                show_t = False
        else:
            show_t = True

    cap.release()
    cv2.destroyAllWindows()

    if len(ts["t"]) > 0:
        df = pd.DataFrame(ts).set_index("t")
        df.name = "QoM"
        print df.describe()
        basename = os.path.basename(filename)
        df.to_csv(basename + ".QoM.csv")

        


def main():
    filename = None
    
    if len(sys.argv) < 4:
        sys.exit("Usage: " + sys.argv[0] + " <filename.mpg> <padding_x> <padding_y>")
    else:
        filename = sys.argv[1]
        padding_x = int(sys.argv[2])
        padding_y = int(sys.argv[3])
        print "Opening", filename
        print "Padding", padding_x, padding_y

        elab(filename, padding_x, padding_y)


if __name__ == '__main__':
    main()

