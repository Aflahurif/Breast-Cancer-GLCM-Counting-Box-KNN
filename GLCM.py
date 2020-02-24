import matplotlib.pyplot as plt
from skimage import io, color, filters, feature, img_as_ubyte, morphology
import os
import numpy as np
import pylab as pl
import cv2
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import entropy, pearsonr
import math

path = '.\\Data Test\\'

data = []

def ke_glcm(gambar):
        box=[]
        scales = [2,4,8,16]
        hasil = {
                "energy" : 0,
                "homogeneity" : 0,
                "contrast" : 0,
                "correlation" : 0
                }
        img_read = cv2.imread(gambar, 0)
        img_conv = img_as_ubyte(img_read)
        glcm = feature.greycomatrix(img_conv, [1], [45], symmetric=True, normed=True)
        retval, threshold = cv2.threshold(img_read, 50, 255 , cv2.THRESH_BINARY)
        tepi = cv2.Canny(threshold, 110, 200)
        for prop in hasil.keys():
                hasil[prop] = float(feature.greycoprops(glcm, prop))
        for baris in range(64):
                for kolom in range(64):
                        if tepi[baris,kolom] == 255:
                                box.append([baris,kolom])
        box = pl.array(box)
        Ns = []
        for scale in scales:
                H, edges = np.histogramdd(box, bins =(np.arange(0,64,scale), np.arange(0,64,scale)))
                Ds = np.log(np.sum(H>0))/np.log(scale)
                Ns.append(Ds)
                data.append(Ds)
        data.append(np.mean(Ns))
        data.append(hasil)

pict = []

for jenis in os.listdir(path):
        folder = path+jenis  
        for isi in os.listdir(folder):
                data=[]
                gambar = path+jenis+'\\'+isi
                ke_glcm(gambar)
                if jenis == "Benign":
                        data.append("Benign")
                elif jenis == "Malignant":
                        data.append("Malignant")
                pict.append(data)