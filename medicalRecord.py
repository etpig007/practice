# Louis Wang. For OPD medical record.
# Ver 1.01,add moore general NE
from tkinter import *

main = Tk()
main.geometry('900x700')
main.title('理學檢查')

GCS = StringVar()
VAS = StringVar()
Pupil = StringVar()
EOM = StringVar()
MP = StringVar()
DTR = StringVar()
VisualField = StringVar()
FingerNFinger = StringVar()
TendomGait = StringVar()

Hoffman = StringVar()
Hoffman.set('nil')
SAT = StringVar()
SAT.set('nil')
AMT = StringVar()
AMT.set('nil')
LMT = StringVar()
LMT.set('nil')

SLRT = StringVar()
SLRT.set('nil')
RSLRT = StringVar()
RSLRT.set('nil')
FABER = StringVar()
FABER.set('nil')
FAIR = StringVar()
FAIR.set('nil')
SKE = StringVar()
SKE.set('nil')
Phalen = StringVar()
Phalen.set('nil')
Tinel = StringVar()
Tinel.set('nil')


# 按確定後輸出到text
def insertTEXT():
    txt.insert(1.0, '---General NE---\n')
    txt.insert('end', 'GCS: ' + GCS.get() + '\n')
    txt.insert('end', 'VAS: ' + VAS.get() + '\n')
    txt.insert('end', 'Pupil: ' + Pupil.get() + '\n')
    txt.insert('end', 'EOM: ' + EOM.get() + '\n')
    txt.insert('end', 'Muscle power: ' + MP.get() + '\n')
    txt.insert('end', 'DTR: ' + DTR.get() + '\n')
    txt.insert('end', 'VisualField: ' + DTR.get() + '\n')
    txt.insert('end', 'FingerNFinger: ' + DTR.get() + '\n')
    txt.insert('end', 'TendomGait: ' + DTR.get() + '\n\n')
    txt.insert('end', '---Cervical---\n')
    txt.insert('end', 'Hoffman test: ' + Hoffman.get() + '\n')
    txt.insert('end', 'Shoulder abduction test: ' + SAT.get() + '\n')
    txt.insert('end', 'Axial manual traction: ' + AMT.get() + '\n')
    txt.insert('end', 'Lhermitte\'s sign: ' + AMT.get() + '\n\n')
    txt.insert('end', '---Lumbar---\n')
    txt.insert('end', 'SLRT: ' + SLRT.get() + '\n')
    txt.insert('end', 'Reverse SLRT: ' + RSLRT.get() + '\n')
    txt.insert('end', 'FABER test: ' + FABER.get() + '\n')
    txt.insert('end', 'FAIR test: ' + FAIR.get() + '\n')
    txt.insert('end', 'Sitting knee extension test: ' + SKE.get() + '\n\n')
    txt.insert('end', '---Carpal tunnel---\n')
    txt.insert('end', 'Phalen test: ' + Phalen.get() + '\n')
    txt.insert('end', 'Tineal test: ' + Tinel.get() + '\n')


def copyTEXT():
    txt.clipboard_clear()

    txt.clipboard_append(txt.get('1.0', END))


# NE
General = LabelFrame(main, text='NE', labelanchor='n',width=500)
Label(General, text='GCS: ').grid(row=0)
Entry(General, width=20, textvariable=GCS).grid(row=0, column=1,padx=10)
Label(General, text='VAS: ').grid(row=1)
Entry(General, width=20, textvariable=VAS).grid(row=1, column=1,padx=10)
Label(General, text='Pupil(L/R): ').grid(row=2)
Entry(General, width=20, textvariable=Pupil).grid(row=2, column=1,padx=10)
Label(General, text='EOM: ').grid(row=3)
Entry(General, width=20, textvariable=EOM).grid(row=3, column=1,padx=10)
Label(General, text='Muscle power: ').grid(row=4)
Entry(General, width=20, textvariable=MP).grid(row=4, column=1,padx=10)
Label(General, text='DTR: ').grid(row=5)
Entry(General, width=20, textvariable=DTR).grid(row=5, column=1,padx=10,pady=5)
Label(General, text='Visual Field: ').grid(row=6)
Entry(General, width=20, textvariable=VisualField).grid(row=6, column=1,padx=10,pady=5)
Label(General, text='FingerNFinger ').grid(row=7)
Entry(General, width=20, textvariable=FingerNFinger).grid(row=7, column=1,padx=10,pady=5)
Label(General, text='Tendom Gait ').grid(row=8)
Entry(General, width=20, textvariable=TendomGait).grid(row=8, column=1,padx=10,pady=5)
General.pack(padx=20, pady=10, anchor='w')

# Cervical PE
Cervical = LabelFrame(main, text='C spine', labelanchor='n')
Label(Cervical, text='Hoffman test: ').grid(row=0)
Radiobutton(Cervical, text='positive', variable=Hoffman, value='positive').grid(row=0, column=1)
Radiobutton(Cervical, text='negative', variable=Hoffman, value='negative').grid(row=0, column=2)
Label(Cervical, text='Shoulder abduction test: ').grid(row=1)
Radiobutton(Cervical, text='positive', variable=SAT, value='positive').grid(row=1, column=1)
Radiobutton(Cervical, text='negative', variable=SAT, value='negative').grid(row=1, column=2)
Label(Cervical, text='Axial manual traction: ').grid(row=2)
Radiobutton(Cervical, text='positive', variable=AMT, value='positive').grid(row=2, column=1)
Radiobutton(Cervical, text='negative', variable=AMT, value='negative').grid(row=2, column=2)
Label(Cervical, text='lhermitte sign: ').grid(row=3)
Radiobutton(Cervical, text='positive', variable=LMT, value='positive').grid(row=3, column=1)
Radiobutton(Cervical, text='negative', variable=LMT, value='negative').grid(row=3, column=2)
Cervical.pack(padx=20, pady=10, anchor='w')

# Lumbar PE
Lumbar = LabelFrame(main, text='Lumbar', labelanchor='n')
Label(Lumbar, text='SLRT').grid(row=0, column=0)
Radiobutton(Lumbar, text='positive', variable=SLRT, value='positive').grid(row=0, column=1)
Radiobutton(Lumbar, text='negative', variable=SLRT, value='negative').grid(row=0, column=2)

Label(Lumbar, text='Reverse SLRT').grid(row=1, column=0)
Radiobutton(Lumbar, text='positive', variable=RSLRT, value='positive').grid(row=1, column=1)
Radiobutton(Lumbar, text='negative', variable=RSLRT, value='negative').grid(row=1, column=2)

Label(Lumbar, text='FABER').grid(row=2, column=0)
Radiobutton(Lumbar, text='positive', variable=FABER, value='positive').grid(row=2, column=1)
Radiobutton(Lumbar, text='negative', variable=FABER, value='negative').grid(row=2, column=2)

Label(Lumbar, text='FAIR').grid(row=3, column=0)
Radiobutton(Lumbar, text='positive', variable=FAIR, value='positive').grid(row=3, column=1)
Radiobutton(Lumbar, text='negative', variable=FAIR, value='negative').grid(row=3, column=2)

Label(Lumbar, text='Sitting knee extension').grid(row=4, column=0)
Radiobutton(Lumbar, text='positive', variable=SKE, value='positive').grid(row=4, column=1)
Radiobutton(Lumbar, text='negative', variable=SKE, value='negative').grid(row=4, column=2)
Lumbar.pack(padx=20, pady=10, anchor='w')

# Carpal tunnel
Carpal = LabelFrame(main, text='Capal tunnel examiniations', labelanchor='n')
Label(Carpal, text='Phalen test').grid(row=0, column=0)
Radiobutton(Carpal, text='positive', variable=Phalen, value='positive').grid(row=0, column=1)
Radiobutton(Carpal, text='negative', variable=Phalen, value='negative').grid(row=0, column=2)

Label(Carpal, text='Tinel test').grid(row=1, column=0)
Radiobutton(Carpal, text='positive', variable=Tinel, value='positive').grid(row=1, column=1)
Radiobutton(Carpal, text='negative', variable=Tinel, value='negative').grid(row=1, column=2)
Carpal.pack(padx=20, pady=10, anchor='w')

# check button
txt = Text(main, width=70, height=45)
txt.place(x=350, y=10)

btn1 = Button(main, text='確定', command=insertTEXT)
btn1.place(x=20, y=650)
btn2 = Button(main, text='複製文字', command=copyTEXT)
btn2.place(x=150, y=650)

main.mainloop()
