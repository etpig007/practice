from tkinter import *
from tkinter import messagebox
import os , glob
from PIL import Image

imagefiles=glob.glob('*.jpg') + glob.glob('*.tiff')

def myMessage(a,b,c):
    for i in imagefiles:
        im = Image.open(i)
        short_pixel = int(im.height*(a/im.width))
        im = im.resize((a, short_pixel))
        im.save('{}_{}.{}'.format('new',i,c),dpi=(b,b))
    messagebox.showinfo('轉換完畢','目標像素:{} 目標dpi:{} 圖片型態:{} '.format(a,b,c))
   

window = Tk()
window.title('投稿圖形格式轉換')
window.geometry('500x200')
label = Label(window, text='把此程式跟圖片資料夾放在一起',
              font='20').grid(row=0,column=1)
n1=IntVar()
n2=IntVar()
n3=StringVar()

targetpixel_lab = Label(window, text='目標像素(寬): ').grid(row=1)
targetdpi_lab = Label(window, text='目標dpi: ').grid(row=2)
targetformat_lab = Label(window, text='輸出檔案格式(jpg,tiff)').grid(row=3)


targetpixel = Entry(window,textvariable=n1).grid(row=1, column=1)
targetdpi = Entry(window,textvariable=n2).grid(row=2, column=1)
targetformat = Entry(window,textvariable=n3).grid(row=3, column=1)


btn1 = Button(window,text="轉換",command=lambda: myMessage(n1.get(),n2.get(),n3.get()))
btn1.grid(row=4,column=0)
btn2 = Button(window,text='離開',command=window.destroy)
btn2.grid(row=4,column=1)

window.mainloop()