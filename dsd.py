import cv2
import time

class obj:
#Constructor still to be added

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
