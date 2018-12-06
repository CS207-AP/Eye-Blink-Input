import cv2
import time
import numpy as np
import os
import socket

def espeak(st):
    os.system("espeak "+st)

class obj:
    def __init__(self, obj_name, possible_states, ROIs, primary_cascade, secondary_cascade):
        self.obj_name = obj_name
        self.possible_states = possible_states
        self.rois = ROIs
        self.prim = cv2.CascadeClassifier(primary_cascade)
        self.sec = cv2.CascadeClassifier(secondary_cascade)
        self.base_img = []
        self.means_array=[]
        
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



    def find_feature(self, img_color):
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        faces = self.prim.detectMultiScale(img_gray, 1.3, 5)
        if(len(faces)>0):
            fx,fy,fw,fh = faces[0]
            face_color = img_color[fy:fy+fw, fx:fx+fh]
            face_gray = img_gray[fy:fy+fw, fx:fx+fh]
            eyes = self.sec.detectMultiScale(face_gray)
            if(len(eyes)>0):
                ex,ey,ew,eh = eyes[0]
                return face_color[ey:ey+ew, ex:ex+eh]
            else:
                return None
        else:
            return None
   
