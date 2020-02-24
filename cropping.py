import cv2
def cropping(gambar):
    path="./"
    img = cv2.imread(gambar)
    tinggi = img.shape[0]
    lebar = img.shape[1]
    tengah_tinggi=int(tinggi/2)
    tengah_lebar=int(lebar/2)
    potong = img[tengah_lebar-32:tengah_lebar+32, tengah_tinggi-32:tengah_tinggi+32]
    nama = path+'test.png'
    cv2.imwrite(nama, potong)
    return nama
 