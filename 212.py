from tkinter import *

r = Tk()
r.geometry("500x500")
r.title("My Title")
r.configure(bg="yellow")

# Labels
rn = Label(r, text="Roll No.")
rn.place(x=20, y=20)

fn = Label(r, text="First Name")
fn.place(x=20, y=60)

ln = Label(r, text="Last Name")
ln.place(x=20, y=100)

em = Label(r, text="Email")
em.place(x=20, y=140)

ern=Entry()
ern.place(x=100,y=20)
efn=Entry()
efn.place(x=100,y=60)
eln=Entry()
eln.place(x=100,y=100)
eem=Entry()
eem.place(x=100,y=140)


button1=Button(r,text="Button1",bg="White")
button1.place(x=20,y=200)
button2=Button(r,text="Button2",bg="White")
button2.place(x=80,y=200)
button3=Button(r,text="Button3",bg="White")
button3.place(x=140,y=200)
button4=Button(r,text="Button4",bg="White")
button4.place(x=200,y=200)

r.mainloop()
