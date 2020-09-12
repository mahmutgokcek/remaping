from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
def haritaguncelle(ind, haerita_x, harita_y):
    if ind == 0:
        for i in range(harita_x.shape[0]):
            for j in range(harita_x.shape[1]):
                if j > harita_x.shape[1]*0.25 and j < harita_x.shape[1]*0.75 and i > harita_x.shape[0]*0.25 and i < harita_x.shape[0]*0.75:
                    harita_x[i,j] = 2 * (j-harita_x.shape[1]*0.25) + 0.5
                    harita_y[i,j] = 2 * (i-harita_y.shape[0]*0.25) + 0.5
                else:
                    harita_x[i,j] = 0
                    harita_y[i,j] = 0
    elif ind == 1:
        for i in range(harita_x.shape[0]):
            harita_x[i,:] = [x for x in range(harita_x.shape[1])]
        for j in range(harita_y.shape[1]):
            harita_y[:,j] = [harita_y.shape[0]-y for y in range(harita_y.shape[0])]
    elif ind == 2:
        for i in range(harita_x.shape[0]):
            harita_x[i,:] = [harita_x.shape[1]-x for x in range(harita_x.shape[1])]
        for j in range(harita_y.shape[1]):
            harita_y[:,j] = [y for y in range(harita_y.shape[0])]
    elif ind == 3:
        for i in range(harita_x.shape[0]):
            harita_x[i,:] = [harita_x.shape[1]-x for x in range(harita_x.shape[1])]
        for j in range(harita_y.shape[1]):
            harita_y[:,j] = [harita_y.shape[0]-y for y in range(harita_y.shape[0])]
parser = argparse.ArgumentParser(description='Haritalandirma Kodu.')
parser.add_argument('--giris', help='Giris Resmi', default='istnabul2.jp')
args = parser.parse_args()
resim = cv.imread("istanbul2.jpg")
if resim is None:
    print('Resim Bulunamadı: ', args.input)
    exit(0)
harita_x = np.zeros((resim.shape[0], resim.shape[1]), dtype=np.float32)
harita_y = np.zeros((resim.shape[0], resim.shape[1]), dtype=np.float32)
pencereadi = 'HARITALANDIRMA'
cv.namedWindow(pencereadi)

ind = 0
while True:
    haritaguncelle(ind, harita_x, harita_y)
    ind = (ind + 1) % 4
    dst = cv.remap(resim, harita_x, harita_y, cv.INTER_LINEAR)
    cv.imshow(pencereadi, dst)
    c = cv.waitKey(1000)
    if c == 27:
        break