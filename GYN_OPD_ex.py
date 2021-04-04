#Copyright:王冠權, 2021/4/4
from tkinter import Tk, StringVar, LabelFrame, Label, Entry, Checkbutton, BooleanVar, Radiobutton, Text, Button, END
from tkinter.ttk import Combobox

window = Tk()
window.title('婦產科會診')
window.geometry('1300x1000')

#=====參數========
Chief_complain = StringVar()
EDC = StringVar()
G = StringVar()
P = StringVar()
A = StringVar()
LMP = StringVar()
#GYN = StringVar()
Surgical_hx = StringVar()
#Underlying_disease = StringVar()

#Lab data
#Lab_data = StringVar()

#PV 
# =========checkbutton===================================================
# Perineum = StringVar()
# OS = StringVar()
# =============================================================================
Vagina = StringVar()
Vagina.set('nil')
Lifiting_pain = StringVar()
Lifiting_pain.set('nil')
#PE
PE = StringVar()
#Images
Images = StringVar()
#Transabdominal_sono 
Uterus_AV = StringVar()
Uterus_RV = StringVar()
Endometrium = StringVar()
Right_adnexa = StringVar()
Left_adnexa = StringVar()
Cul_de_sac = StringVar()
Cul_de_sac.set('nil')
#Transvaginal_sono
TV_Uterus_AV = StringVar()
TV_Uterus_RV = StringVar()
TV_Endometrium = StringVar()
TV_Right_adnexa = StringVar()
TV_Left_adnexa = StringVar()
TV_Cul_de_sac = StringVar()
TV_Cul_de_sac.set('nil')
#Impression
#1.Pregnancy at wks with threatened abortion
#2.Pelvic inflammatory disease, r/o TOA
#3.Ectopic pregnancy
#Impression = StringVar()
#Plan
Plan = StringVar()
Plan.set('Educated the patient if the symptoms progress, back to ER or OPD immediatly')
#Sign
Resident = StringVar()
Resident.set('R2陳姵辰')
VisitingStaff = StringVar()
#============insert_text======================================
def insert_text():
    resultTEXT.insert(1.0, f'Chief complain: {Chief_complain.get()}\n')
    resultTEXT.insert('end', f'EDC: {EDC.get()}\n')
    resultTEXT.insert('end', f'GPA: {G.get()}{P.get()}{A.get()}\n')
    GYN_hxs = checkbox_get(GYN_hx_CB,GYN_hx) 
    resultTEXT.insert('end', f'GYN hx: {GYN_hxs.result}\n')
    resultTEXT.insert('end', f'Surgical hx: {Surgical_hx.get()}\n')
    Underlying_ds = checkbox_get(Underlying_disease_CB,Underlying_disease)
    resultTEXT.insert('end', f'Underlying disease: {Underlying_ds.result}\n')
    resultTEXT.insert('end',f'Lab data: {Lab_data.get(1.0,END)}\n')
    resultTEXT.insert('end','=====PV=====\n')
    Perineum_get = checkbox_get(Perineum_CB,Perineum)
    resultTEXT.insert('end',f'Perineum: {Perineum_get.result }\n')
    OS_get = checkbox_get(OSex_CB,OSex)
    resultTEXT.insert('end',f'OS: {OS_get.result}\n')
    resultTEXT.insert('end',f'Vagina: {Vagina.get()}\n')
    resultTEXT.insert('end',f'Lifting pain: {Lifiting_pain.get()}\n')
    resultTEXT.insert('end','====={PE}=====\n')
    resultTEXT.insert('end',f'{PE.get(1.0,END)}\n')
    resultTEXT.insert('end','=====Image=====\n')
    resultTEXT.insert('end',f'Image: {Images.get(1.0,END)}\n')
    resultTEXT.insert('end','=====Transabdominal sonography=====\n')
    resultTEXT.insert('end',f'Uterus: AV/RV:{Uterus_AV.get()}/{Uterus_RV.get()}\n')
    resultTEXT.insert('end',f'Endometrium: {Endometrium.get()} cm\n')
    resultTEXT.insert('end',f'Right adnexa: {Right_adnexa.get()} cm\n')
    resultTEXT.insert('end',f'Left adnexa: {Left_adnexa.get()} cm\n')
    resultTEXT.insert('end',f'Cul_de_sac: {Cul_de_sac.get()}\n')
    resultTEXT.insert('end','=====Transvaginal sonography=====\n')
    resultTEXT.insert('end',f'Uterus: AV/RV:{TV_Uterus_AV.get()}/{TV_Uterus_RV.get()}\n')
    resultTEXT.insert('end',f'Endometrium: {TV_Endometrium.get()} cm\n')
    resultTEXT.insert('end',f'Right adnexa: {TV_Right_adnexa.get()} cm\n')
    resultTEXT.insert('end',f'Left adnexa: {TV_Left_adnexa.get()} cm\n')
    resultTEXT.insert('end',f'Cul_de_sac: {TV_Cul_de_sac.get()}\n')
    resultTEXT.insert('end',f'Impression: {Impression.get(1.0,END)}\n')
    resultTEXT.insert('end',f'Plan: {Plan.get(1.0,END)}\n')
    resultTEXT.insert('end',f'住院醫師: {Resident.get()} / ')
    resultTEXT.insert('end',f'主治醫師: {VisitingStaff.get()}')
#============copy_text======================================
def copy_text():
    resultTEXT.clipboard_clear()
    resultTEXT.clipboard_append(resultTEXT.get(1.0,END))
#============delete_text======================================
def delet_text():
    resultTEXT.delete(1.0,END)
#============GYN_hx_func======================
class checkbox_get:
    result=''
    def __init__(self,CB,CBs):      
        for l in CB:
            if CB[l].get() == True:
                self.result = self.result + CBs[l] + '.\t'

#============General==========
CC = LabelFrame(window, text='General', labelanchor='n')
CC.grid(row=0,column=0,columnspan=2, padx=5,pady=5,sticky='nesw')

Label(CC, text='Chief complain: ').grid(row=0,padx=5,pady=5)
Entry(CC, width = 50 , textvariable=Chief_complain).grid(row=0, column=1,sticky='w',columnspan=3)

Label(CC, text='EDC: ').grid(row=1,padx=5,pady=5)
Entry(CC, width = 15 , textvariable=EDC).grid(row=1, column=1,sticky='w')

Label(CC, text='GPA: ').grid(row=2,padx=5,pady=5)
Gs = [f'G{i}'for i in range(0,20)]
Ps = [f'P{i}'for i in range(0,20)]
As = [f'A{i}'for i in range(0,20)]
GCB = Combobox(CC, width=10, value=Gs, textvariable=G)
G.set(GCB)
GCB.current(0)
GCB.grid(row=2, column=1,padx=5,pady=5,sticky='w')

PCB = Combobox(CC, width=10, value=Ps, textvariable=P)
P.set(PCB)
PCB.current(0)
PCB.grid(row=2, column=2,padx=5,pady=5,sticky='w')

ACB = Combobox(CC, width=10, value=As, textvariable=A)
A.set(ACB)
ACB.current(0)
ACB.grid(row=2, column=3,padx=5,pady=5,sticky='w')
#=====GYN_hx的checkbn======
Label(CC, text='GYN hx: ').grid(row=3,padx=5,pady=5)
GYN_hx = {1:'myoma', 2:'endomeriosis', 3:'ovarian tumor', 4:'cancer', 5:'PID', 6:'STD disease', 7:'Nil'}
GYN_hx_CB = {}
for i in GYN_hx.keys():
    GYN_hx_CB[i] = BooleanVar()
    if i<4:
        GYN_checkbn = Checkbutton(CC,text=GYN_hx[i],variable=GYN_hx_CB[i])
        GYN_checkbn.grid(row=3,column=i,sticky='w')
    elif 7>i>=4:
        GYN_checkbn = Checkbutton(CC,text=GYN_hx[i],variable=GYN_hx_CB[i])
        GYN_checkbn.grid(row=4,column=i-3,sticky='w')
    else:
        GYN_checkbn = Checkbutton(CC,text=GYN_hx[i],variable=GYN_hx_CB[i])
        GYN_checkbn.grid(row=5,column=i-6,sticky='w')
#==============================
Label(CC, text='Surgical hx: ').grid(row=6,sticky='w',padx=5,pady=5)
Entry(CC, textvariable=Surgical_hx, width=15).grid(row=6,column=1,sticky='w')
#====underlying disease的checkbn========
Label(CC, text='Underlying dis: ').grid(row=7,sticky='w',padx=5,pady=5)
Underlying_disease = {1:'Hypertension', 2:'Diabetes'}
Underlying_disease_CB = {}
for j in Underlying_disease.keys():
    Underlying_disease_CB[j] = BooleanVar()
    UD_CB = Checkbutton(CC,text=Underlying_disease[j],variable=Underlying_disease_CB[j])
    UD_CB.grid(row=7,column=j,sticky='w')
#====================================
Label(CC, text='Lab data: ').grid(row=8,sticky='w',padx=5,pady=5)
Lab_data = Text(CC,width=50,height=5)
Lab_data.grid(row=8,column=1,columnspan=3,sticky='w',pady=5)
#============PV Labelframe=============
PVLF = LabelFrame(window, text='PV', labelanchor='n')
PVLF.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky='nesw')
#===perineum checkbottun===
Label(PVLF, text='Perineum: ').grid(row=0,sticky='w',padx=5,pady=5)
Perineum = {1:'normal appearence', 2:'redness',3:'swelling'}
Perineum_CB = {}
for k in Perineum.keys():
    Perineum_CB[k] = BooleanVar()
    P_CB = Checkbutton(PVLF,text=Perineum[k],variable=Perineum_CB[k])
    P_CB.grid(row=0,column=k,sticky='w')
#=========OS checkbutton========================
Label(PVLF, text='OS: ').grid(row=1,sticky='w',padx=5,pady=5)
OSex = {1:'open', 2:'active bleeding',3:'oozing',4:'old blood clot'}
OSex_CB = {}
for k in OSex.keys():
    OSex_CB[k] = BooleanVar()
    OS_CB = Checkbutton(PVLF,text=OSex[k],variable=OSex_CB[k])
    OS_CB.grid(row=1,column=k,sticky='w')
#============VaginaRtn========================
Label(PVLF, text='Vagina: ').grid(row=2,sticky='w',padx=5,pady=5)
Vaginabtn1 = Radiobutton(PVLF,text='mucoid whitish discharge',variable=Vagina,value='mucoid whitish discharge')
Vaginabtn1.grid(row=2, column=1,sticky='w')
Vaginabtn2 = Radiobutton(PVLF,text='brownish discharge',variable=Vagina,value='brownish discharge')
Vaginabtn2.grid(row=2, column=2,sticky='w')

Label(PVLF, text='Lifting pain: ').grid(row=3,sticky='w',padx=5,pady=5)
LFPbtn1 = Radiobutton(PVLF,text='positive',variable=Lifiting_pain,value='positive')
LFPbtn1.grid(row=3, column=1,sticky='w')
LFPbtn2 = Radiobutton(PVLF,text='negative',variable=Lifiting_pain,value='negative')
LFPbtn2.grid(row=3, column=2,sticky='w')
#================PELabelFrame============================
PELF = LabelFrame(window,text='PE',labelanchor='n')
PELF.grid(row=2,column=0,padx=5,pady=5,sticky='nesw')
PE = Text(PELF,width=40,height=3)
PE.grid(row=0,column=1,padx=5,pady=5)
#=====================ImageLF==============================
IMLF = LabelFrame(window,text='Image',labelanchor='n')
IMLF.grid(row=2,column=1,padx=5,pady=5,sticky='nesw')
Images = Text(IMLF,width=40,height=3)
Images.grid(row=0,column=1,padx=5,pady=5,sticky='nesw')
#================Transabdominal sonography=================
Transabd = LabelFrame(window,text='Transabdominal sonography',labelanchor='n')
Transabd.grid(row=3,column=0,padx=5,pady=5,sticky='nesw')
Label(Transabd , text='Uterus: AV/RV:').grid(row=0,padx=5,pady=5)
Entry(Transabd, textvariable=Uterus_AV,width=5).grid(row=0,column=1)
Label(Transabd, text='cm*').grid(row=0,column=2,sticky='w')
Entry(Transabd, textvariable=Uterus_RV,width=5).grid(row=0,column=3)
Label(Transabd, text='cm').grid(row=0,column=4, sticky='w')

Label(Transabd, text='Endometrium: ').grid(row=1)
Entry(Transabd, textvariable=Endometrium,width=5).grid(row=1,column=1)
Label(Transabd, text='cm').grid(row=1,column=2,sticky='w')

Label(Transabd, text='Right adnexa ').grid(row=2)
Entry(Transabd, textvariable=Right_adnexa, width=5).grid(row=2,column=1)
Label(Transabd, text='cm').grid(row=2,column=2,sticky='w')
Label(Transabd, text='Left adnexa ').grid(row=3,column=0)
Entry(Transabd, textvariable=Left_adnexa, width=5).grid(row=3,column=1)
Label(Transabd, text='cm').grid(row=3,column=2,sticky='w')

Label(Transabd, text='Cu-de-sac: ').grid(row=4,sticky='w',padx=5,pady=5)
Cubtn1 = Radiobutton(Transabd,text='positive',variable=Cul_de_sac,value='positive')
Cubtn2 = Radiobutton(Transabd,text='negative',variable=Cul_de_sac,value='negative')
Cubtn1.grid(row=4,column=1)
Cubtn2.grid(row=4,column=2)

#=============TVSLF=============
TVSLF = LabelFrame(window,text='Transvaginal sonography', labelanchor='n')
TVSLF.grid(row=3,column=1,padx=5,pady=5,sticky='nesw')
Label(TVSLF, text='Uterus: AV/RV:').grid(row=0,padx=5,pady=5)
Entry(TVSLF, textvariable=TV_Uterus_AV,width=5).grid(row=0,column=1)
Label(TVSLF, text='cm*').grid(row=0,column=2,sticky='w')
Entry(TVSLF, textvariable=TV_Uterus_RV,width=5).grid(row=0,column=3)
Label(TVSLF, text='cm').grid(row=0,column=4, sticky='w')

Label(TVSLF, text='Endometrium: ').grid(row=1)
Entry(TVSLF, textvariable=TV_Endometrium,width=5).grid(row=1,column=1)
Label(TVSLF, text='cm').grid(row=1,column=2,sticky='w')

Label(TVSLF, text='Right adnexa ').grid(row=2)
Entry(TVSLF, textvariable=TV_Right_adnexa, width=5).grid(row=2,column=1)
Label(TVSLF, text='cm').grid(row=2,column=2,sticky='w')
Label(TVSLF, text='Left adnexa ').grid(row=3,column=0)
Entry(TVSLF, textvariable=TV_Left_adnexa, width=5).grid(row=3,column=1)
Label(TVSLF, text='cm').grid(row=3,column=2,sticky='w')

Label(TVSLF, text='Cu-de-sac: ').grid(row=4,sticky='w',padx=5,pady=5)
Cubtn1 = Radiobutton(TVSLF,text='positive',variable=TV_Cul_de_sac,value='positive')
Cubtn2 = Radiobutton(TVSLF,text='negative',variable=TV_Cul_de_sac,value='negative')
Cubtn1.grid(row=4,column=1)
Cubtn2.grid(row=4,column=2)

#=========impressionLF==========
impressionLF = LabelFrame(window,text='Impression', labelanchor='n')
impressionLF.grid(row=4,padx=5,pady=5,sticky='nesw')
Impression = Text(impressionLF,width=45, height=5)
Impression.grid(row=0,column=0,padx=5,pady=5)

#================PlanLF=============
planLF = LabelFrame(window,text='Plan', labelanchor='n')
planLF.grid(row=4,column=1,padx=5,pady=5,sticky='nesw')
Plan = Text(planLF,width=45, height=5)
Plan.grid(row=0,column=0,padx=5,pady=5)

#========DoctorsLF==============
DocLF = LabelFrame(window,text='Doctors', labelanchor='n')
DocLF.grid(row=5,sticky='nesw',padx=5,pady=5)
Label(DocLF,text='住院醫師: ').grid(row=0)
Residents = ['R2陳姵辰']
ResidentCB = Combobox(DocLF, width=10, value=Residents, textvariable=Resident)
Resident.set(ResidentCB)
ResidentCB.current(0)
ResidentCB.grid(row=0, column=1,padx=5,pady=5)
VisitingStaffs = ['VS魏佑吉','VS陳萱','VS高聖博','VS丁大清','VS黃琦']
VSCB = Combobox(DocLF, width=10, value=VisitingStaffs, textvariable=VisitingStaff)
VisitingStaff.set(VSCB)
VSCB.current(0)
VSCB.grid(row=0, column=2,padx=5,pady=5)

#============show main text===========
resultTEXT = Text(window, width=80,height=70)
resultTEXT.place(x=700, y=10)
#==================checkbtn==================
checkbtn = Button(window, text='確定',command=insert_text)
copybtn = Button(window, text ='複製',command=copy_text)
clearbtn = Button(window, text='清除',command=delet_text)
checkbtn.place(x=50,y=900)
copybtn.place(x=150,y=900)
clearbtn.place(x=250,y=900)


window.mainloop()