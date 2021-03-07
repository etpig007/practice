import os
import pikepdf
from tkinter import *
from tkinter import filedialog
import tkinter as tk


window = Tk()
window.geometry('500x200')
window.title('解密pdf')

PASSWORD = StringVar()
FileName = StringVar()
Destination = StringVar()
def pathCallBack():
    filepath = filedialog.askopenfilename()
    if(filepath != ''):
        FileName.set(filepath)
def dirCallback():
    dirpath = filedialog.askdirectory()
    if(dirpath  != ''):
        Destination.set(dirpath)

def decode():
    try:
        pdf = pikepdf.open(FileName.get(),password=PASSWORD.get())
    except pikepdf._qpdf.PasswordError: 
        messagebox.showwarning('密碼錯誤','密碼錯誤')
    else:
        messagebox.showinfo('解碼成功','解碼成功')
        fileName = FileName.get().split('/')[-1].rstrip('.pdf')
        pdf.save(Destination.get()+'/decoded_{}.pdf'.format(fileName))
    
btnpath = tk.Button(window,text='選擇',width=10,command=pathCallBack)
btndestination = tk.Button(window,text='選擇',width=10,command=dirCallback)
btnok = tk.Button(window, text='解密',width=10,command=decode)

Label(window,text='選擇檔案: ').grid(row=0,column=0)
Entry(window,width=45,textvariable=FileName).grid(row=0,column=1)
Label(window,text='密碼: ').grid(row=1,column=0)
Entry(window,width=45,textvariable=PASSWORD, show='*').grid(row=1,column=1)
Label(window,text='目標資料夾 ').grid(row=2,column=0)
Entry(window,width=45,textvariable=Destination).grid(row=2,column=1)

btnpath.grid(row=0,column=2)
btndestination.grid(row=2,column=2)
btnok.grid(row=3,column=1)



window.mainloop()