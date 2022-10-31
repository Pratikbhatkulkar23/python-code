from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet speed test")
sp.geometry("500x500")
sp.config(bg="Blue")
lab = Label(sp,text="Internet speed test",font=("Time new Roman",20,"bold"),bg="white")
lab.place(x=55,y=40,height=50,width=380)

lab = Label(sp,text="Download speed test",font=("Time new Roman",20,"bold"),bg="Blue")
lab.place(x=55,y=130,height=50,width=380)

lab = Label(sp,text="00",font=("Time new Roman",20,"bold"),bg="Blue")
lab.place(x=55,y=200,height=50,width=38)

lab = Label(sp,text="Upload  speed test",font=("Time new Roman",20,"bold"),bg="Blue")
lab.place(x=55,y=290,height=50,width=380)

lab = Label(sp,text="00",font=("Time new Roman",20,"bold"),bg="Blue")
lab.place(x=55,y=360,height=50,width=380)

button = Button(sp,text="chekc speed",30,"bold"),relief=RAISED)
sp.mainloop()
