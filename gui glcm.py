from tkinter import filedialog
from tkinter import *
from shutil import copy2
from PIL import ImageTk, Image
import math
import operator
import GLCM
import numpy as np
pict_test = []
class coba:
    
    def __init__(self, ini):
        data = "3.png"
        text1 = "0"
        text2 = "0"
        text3 = "0"
        text4 = "0"
        text5 = "0"
        text1F = "0"
        text2F = "0"
        text3F = "0"
        text4F = "0"

        gambar = ""
        
        self.ini = ini
        self.initUI()
        var = StringVar()

        self.lbllist = Label(ini, text="HASIL PERHITUNGAN KNN").grid(row=7, column=0, columnspan=3)
        
        self.table()
        self.tombol(NORMAL,DISABLED)
        self.gmr(data)
        self.kualifikasi(text1,text2,text3,text4,text5,text1F,text2F,text3F,text4F)

    def tombol(self, statusU, statusP):
        self.buttonUpload = Button(text="UPLOAD", width=6, command=self.upload, state=statusU)
        self.buttonUpload.grid(row=6, column=0, columnspan=2)

        self.buttonProses = Button(text="PROSES", width=6, command=self.hitung, state=statusP).grid(row=6, column=3, columnspan=2)

    def kualifikasi(self,text1,text2,text3,text4,text5,text1F,text2F,text3F,text4F):
        self.lFJ = Label( text="FRAKTAL BOX COUNTING").grid(row=0, column=2, columnspan = 4)
        self.lF1 = Label( text="1").grid(row=1, column=2, columnspan = 2)
        self.lF11 = Label( width=10, bg="white", text=text1F ).grid(row=1, column=4, columnspan = 2)
        
        self.lF2 = Label( text="2").grid(row=2, column=2, columnspan = 2)
        self.lF12 = Label( width=10, bg="white", text=text2F ).grid(row=2, column=4, columnspan = 2)
        
        self.lF3 = Label( text="3").grid(row=3, column=2, columnspan = 2)
        self.lF13 = Label( width=10, bg="white", text=text3F ).grid(row=3, column=4, columnspan = 2)
        
        self.lF4 = Label( text="4").grid(row=4, column=2, columnspan = 2)
        self.lF14 = Label( width=10, bg="white", text=text4F ).grid(row=4, column=4, columnspan = 2)

        
        self.lJ = Label( text="GLCM").grid(row=0, column=6, columnspan = 4)
        self.l1 = Label( text="Rerata Dimensi Fraktal").grid(row=5, column=2, stick=W, columnspan = 2)
        self.l11 = Label( width=10, bg="white", text=text1 ).grid(row=5, column=4, columnspan = 2)

        self.l2 = Label( text="energy").grid(row=1, column=6, stick=W, columnspan = 2)
        self.l12 = Label( width=10, bg="white", text=text2 ).grid(row=1, column=8, columnspan = 2)
        
        self.l3 = Label( text="homogeneity").grid(row=2, column=6, stick=W, columnspan = 2)
        self.l13 = Label( width=10, bg="white", text=text3 ).grid(row=2, column=8, columnspan = 2)
        
        self.l4 = Label( text="contrast").grid(row=3, column=6, stick=W, columnspan = 2)
        self.l14 = Label( width=10, bg="white", text=text4 ).grid(row=3, column=8, columnspan = 2)
        
        self.l5 = Label( text="correlation").grid(row=4, column=6, columnspan = 2, stick=W)
        self.l15 = Label( width=10, bg="white", text=text5 ).grid(row=4, column=8, columnspan = 2)

    def gmr(self, data):
        img=Image.open(data)
        self.tkimage = ImageTk.PhotoImage(img)
        self.lblimage = Label(image=self.tkimage, width=70, height=70).grid(row=0, column=0, rowspan=5, columnspan =2)
    
    def initUI(self):
        self.ini.title("PERTHITUNGAN FRAKTAL DAN GLCM")
        self.ini.geometry("850x300")
   
    def upload(self):
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("gambar files","*.png"),("all files","*.*")))
        gambar = str(filename)
        self.gmr(gambar)
        import cropping
        gambar = cropping.cropping(gambar)
        self.gmr(gambar)
        GLCM.ke_glcm(gambar)
        pict_test.append(GLCM.data)
        text1F = round(GLCM.data[0],4)
        text2F = round(GLCM.data[1],4)
        text3F = round(GLCM.data[2],4)
        text4F = round(GLCM.data[3],4)
        text1 = round(GLCM.data[4],4)
        text2 = round(GLCM.data[5]["energy"],4)
        text3 = round(GLCM.data[5]["homogeneity"],4)
        text4 = round(GLCM.data[5]["contrast"],4)
        text5 = round(GLCM.data[5]["correlation"],4)
        self.kualifikasi(text1,text2,text3,text4,text5,text1F,text2F,text3F,text4F)
        self.tombol(DISABLED,NORMAL)
    
    def hitung(self):
        jarak = 0
        import GLCM
        for i in range(len(GLCM.pict)):
            r=0
            for D in range(4,5):
                r+=pow(float(pict_test[0][D] - GLCM.pict[i][D]),2)
            for data in GLCM.pict[i][5].keys():
                r += pow(float(pict_test[0][5][data] - GLCM.pict[i][5][data]),2)
            jarak = round(math.sqrt(r),2)
            GLCM.pict[i].append(jarak)
        print(GLCM.pict[0])
        list.sort(GLCM.pict, key=lambda x:float(x[7]))
        print(GLCM.pict[0])
        print(GLCM.pict[1])
        self.tombol(NORMAL,DISABLED)
        baris=9
        lebar = 10
        for data in range(3):
            kolom = 0
            for D in range(8):
                if D is not 6:
                    if D is 5:
                        for prop in GLCM.pict[i][5].keys():
                            a = round(GLCM.pict[data][5][prop],6)
                            b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                            kolom+=1
                    else:
                        a = round(GLCM.pict[data][D],6)
                        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                else:
                    kolom-=1
                    a = GLCM.pict[data][D]
                    b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                kolom+=1
            baris+=1

    def table(self):
        baris = 9

        lebar = 10
        
        a = "D(2)"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 0)
        
        a = "D(4)"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 1)
        
        a = "D(8)"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 2)
        
        a = "D(16)"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 3)
        
        a = "Mean D"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 4)
        
        a = "Energy"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 5)
        
        a = "Homogeneity"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 6)
        
        a = "Contrast"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 7)
        
        a = "Correlation"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 8)
        
        a = "Jenis"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 9)
        
        a = "Jarak"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 10)

        for data in range(3):
            kolom = 0
            for D in range(11):
                a = "-"
                b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                kolom+=1
            baris+=1

root = Tk()
app = coba(root)
root.mainloop()