import cv2
import time
import numpy as np
import os
import socket

def espeak(st):
    os.system("espeak "+st)

class obj:
#Constructor still to be made
    def initialize_means_roi(self):
        for state_imgs in self.base_img:
            roi_means = []
            fin_means = []
            for state_img in state_imgs:
                width = len(state_img)
                height = len(state_img[0])
                roi_mean_array =[]
                for roi in self.rois:
                    x1 = int(width*roi[0])
                    x2 = int(width*roi[1])
                    y1 = int(height*roi[2])
                    y2 = int(height*roi[3])
                    roi_mean_array.extend([state_img[:,:,0][x1:x2,y1:y2].mean()])#, state_img[:,:,1][x1:x2,y1:y2].mean(), state_img[:,:,2][x1:x2,y1:y2].mean()])
                roi_means.append(roi_mean_array)
            tp = [list(x) for x in zip(*roi_means)]
            for arr in tp:
                fin_means.append(sum(arr)/len(arr))
            self.means_array.append(fin_means)
        self.means_array_transposed = [list(x) for x in zip(*self.means_array)]

    def initialize(self, comm_method):
        cap = cv2.VideoCapture(0)
        for state in self.possible_states:
            not_init = 0
            comm_method("Please keep "+self.obj_name+" in "+state+" state for next 5 seconds.")
            time.sleep(2)
            bas_imgs = []
            while(not_init<100):
                ret, img = cap.read()
                fet = self.find_feature(img)
                if(type(fet)!=type(None)):
                    bas_imgs.append(fet)
                    not_init=not_init+1
            self.base_img.append(bas_imgs)
            comm_method(state+" initizalized.")
            time.sleep(2)
        return cap
