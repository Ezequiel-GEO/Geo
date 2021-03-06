from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Q (Barton, 1974)")
root.geometry("400x400+200+200")

#Introducción al programa
label = Label(root, text="Clasificar del macizo rocoso según la clasificación Q:", font=("", "12"))
label.place(x=10,y=0)


#Parámetros
rqd = Label(root, text="RQD (%)", font=("","11")) 
rqd.place(x=5, y=50)
rqd_ = Entry(root, width=5)
rqd_.place(x=75, y=50)

def Jn():
    jn1=Toplevel()
    jn1.title("Jn")
    jn1.geometry("725x325+750+50")
    jn2= Image.open("jn.jpg")     
    jn3 = jn2.resize((700, 300), Image.ANTIALIAS)
    jn4 = ImageTk.PhotoImage(jn3)
    jn5 = Label(jn1, image=jn4)
    jn5.pack()
    jn1.mainloop()
    return

def Ja():
    ja1=Toplevel()
    ja1.title("Ja")
    ja1.geometry("750x600+550+50")
    ja2= Image.open("ja.jpg")     
    ja3 = ja2.resize((725, 575), Image.ANTIALIAS)
    ja4 = ImageTk.PhotoImage(ja3)
    ja5 = Label(ja1, image=ja4)
    ja5.pack()
    ja1.mainloop()
    return

def Jr():
    jr1=Toplevel()
    jr1.title("Jr")
    jr1.geometry("725x475+650+50")
    jr2= Image.open("jr.jpg")     
    jr3 = jr2.resize((700, 450), Image.ANTIALIAS)
    jr4 = ImageTk.PhotoImage(jr3)
    jr5 = Label(jr1, image=jr4)
    jr5.pack()
    jr1.mainloop()
    return

def Jw():
    jw1=Toplevel()
    jw1.title("Jw")
    jw1.geometry("725x325+750+50")
    jw2= Image.open("jw.jpg")     
    jw3 = jw2.resize((700, 300), Image.ANTIALIAS)
    jw4 = ImageTk.PhotoImage(jw3)
    jw5 = Label(jw1, image=jw4)
    jw5.pack()
    jw1.mainloop()
    return

def SRF():
    srf1=Toplevel()
    srf1.title("SRF")
    srf1.geometry("750x725+600+50")
    srf2= Image.open("srf.jpg")     
    srf3 = srf2.resize((725, 700), Image.ANTIALIAS)
    srf4 = ImageTk.PhotoImage(srf3)
    srf5 = Label(srf1, image=srf4)
    srf5.pack()
    srf1.mainloop()
    return

jn = Label(root, text="Jn", font=("","11")) 
jn.place(x=15, y=90)
jn_ = Entry(root, width=5)
jn_.place(x=75, y=90)
jn__ = Button(root, text="!", width=5, command=Jn)
jn__.place(x=120, y=87)

ja = Label(root, text="Ja", font=("","11")) 
ja.place(x=15, y=130)
ja_ = Entry(root, width=5)
ja_.place(x=75, y=130)
ja__ = Button(root, text="!", width=5, command=Ja)
ja__.place(x=120, y=127)

jr = Label(root, text="Jr", font=("","11")) 
jr.place(x=15, y=170)
jr_ = Entry(root, width=5)
jr_.place(x=75, y=170)
jr__ = Button(root, text="!", width=5, command=Jr)
jr__.place(x=120, y=167)

jw = Label(root, text="Jw", font=("","11")) 
jw.place(x=15, y=210)
jw_ = Entry(root, width=5)
jw_.place(x=75, y=210)
jw__ = Button(root, text="!", width=5, command=Jw)
jw__.place(x=120, y=207)

srf = Label(root, text="SRF", font=("","11")) 
srf.place(x=15, y=250)
srf_ = Entry(root, width=5)
srf_.place(x=75, y=250)
srf__ = Button(root, text="!", width=5, command=SRF)
srf__.place(x=120, y=247)

def Q():
    a = float(rqd_.get())
    b = float(jn_.get())
    c = float(ja_.get())
    d = float(jr_.get())
    e = float(jw_.get())
    f = float(srf_.get())
    g=(a/b)*(d/c)*(e/f)
    h=round(g,2)
    global q
    q = Entry(root, width=10)
    q.place(x=120, y=300)
    q.insert(0, h)
    global clase
    clase = Entry(root, width=30)
    clase.place(x=200, y=300)
    if h>=400:
        clase.insert(0, "roca excepcionalmente buena")
    elif h<400 and h>=100:
        clase.insert(0,"roca extrenadamente buena")
    elif h<100 and h>=40:
        clase.insert(0,"roca muy buena")
    elif h<40 and h>=10:
        clase.insert(0,"roca buena")
    elif h<10 and h>=4:
        clase.insert(0,"roca media")
    elif h<4 and h>=1:
        clase.insert(0,"roca mala")
    elif h<1 and h>=0.1:
        clase.insert(0,"roca muy mala")
    elif h<0.1 and h>=0.01:
        clase.insert(0,"roca extremadamente mala")
    elif h<0.01 and h>=0.001:
        clase.insert(0,"roca excepcionalmente mala")
    return

q_= Button(root, text="Calcular Q", width=10, command=Q)
q_.place(x=30, y=295)

def borrar():
    q.delete(0,END)
    clase.delete(0, END)

borrar = Button(root, text="Borrar", padx=5, pady=5, command= borrar)
borrar.place(x=30, y=330)

root.mainloop() 
