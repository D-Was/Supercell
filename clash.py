from tkinter import *
from tkinter.ttk import *
wind=Tk()
wind.geometry('1920x1080')
pictt=PhotoImage(file='/home/dwas/Downloads/app.png')
photoimage1 = pictt.subsample(4, 4) 
pict1=PhotoImage(file='/home/dwas/Downloads/coc.png')
phtimg2=pict1.subsample(4,4)
pict2=PhotoImage(file='/home/dwas/Downloads/bs.png')
pict2sam=pict2.subsample(4,4)

def clixk():
    txt=Entry(wind, width=30)
    txt.grid(column=15, row=30)
    btn1=Button(wind, text='go')
    btn1.grid(column=16,row=6)

def click1():
    lblx=Label(wind, text='Coming soon').grid(row=10)

def click2():
    lbly=Label(wind, text='Coming soon').grid(cloumn=5, row=5)

    
bttn=Button(wind,image=photoimage1, command=clixk).grid(column=2, row=3)
btn1=Button(wind,image=phtimg2 , command=click1).grid(column=5, row=3)
btn2=Button(wind, image=pict2sam, command=click2).grid(column=7, row=3)


wind.mainloop()

