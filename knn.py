import math

def kunci(elem):
    return elem[2]
def hitung():
    jarak = []
    import GLCM
    for i in range(len(GLCM.pict)):
        r=0
        for data in GLCM.pict[i][1].keys():
            r += pow((importgambar.pict_test[i][1][data] - GLCM.pict[i][1][data]),2)
        r += pow(pict_test.pict[i][0] - GLCM.pict[i][0],2)
        GLCM.pict[i].append(round(math.sqrt(r),2))

    print(sorted(GLCM.pict, key=kunci))
hitung()
