import numpy as np
import matplotlib.pyplot as plt
import unittest
import PIL

class Drapeau():
    def __init__(self):
        self.val = np.zeros((360,600,3))
        
    def set_pixel(self,x,y,r,g,b):
        assert 0<=x<600,"x doit etre entre 0 et 599 inclus"
        assert 0<=y<360,"y doit etre entre 0 et 359 inclus"
        assert 0<=r<=255 and 0<=g<=255 and 0<=b<=255,"La valeur d'un canal coloré doit être entre 0 et 255 inclus"
        self.val[y,x,:]=[r/255,g/255,b/255]
        
    def show(self):
        
        im = plt.imshow(self.val,interpolation='none')
        #im.set_cmap('gray')
        #plt.axis("off")
        plt.xticks([],[])
        plt.yticks([],[])
        plt.show()