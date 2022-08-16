
import string,tkinter,pyperclip
import random


#from cgitb import text


def generate(n):
    alphabets=string.ascii_letters
    digits=string.digits
    specialchar=string.punctuation
    charsets=[alphabets,digits,specialchar]
    password=""
    while(len(password)!=n):
        selectedset=random.choice(charsets)
        index=random.randint(0,len(selectedset)-1)
        password=password+selectedset[index]
    p2=list(password)
    random.shuffle(p2)
    pass2="".join(p2)
    return(pass2)





from cProfile import label
from tkinter import Frame

def clickedsubmit():
    n=txt.get()
    s=generate(int(n))
    label2.configure(text=s)
    copybtn.pack(side=tkinter.LEFT)

def copyfn():
    tocopy=label2.cget("text")
    pyperclip.copy(tocopy)

window=tkinter.Tk()
window.title("Password Generator")
window.geometry("500x500")

title=tkinter.Label(window,text="Password Generator",font=("Arial Bold",30))
title.pack(pady=30)
frame1=Frame(window)
frame2=Frame(window)
frame1.pack(pady=15,side=tkinter.TOP,anchor="w")
frame2.pack(pady=15,side=tkinter.TOP,anchor="w")

label1=tkinter.Label(frame1,text="Enter length of password:",font=("Arial",15))
label1.pack(padx=15,side=tkinter.LEFT)
txt=tkinter.Entry(frame1,width=10)
txt.pack(padx=10,side=tkinter.LEFT)
submitbtn=tkinter.Button(frame1,text="Enter",command=clickedsubmit)
submitbtn.pack(side=tkinter.LEFT)
label1=tkinter.Label(frame2,text="Password Generated is:",font=("Arial",15))
label1.pack(padx=15,side=tkinter.LEFT)
label2=tkinter.Label(frame2,text="",font=("Arial",15))
label2.pack(padx=10,side=tkinter.LEFT)
copybtn=tkinter.Button(frame2,text="Click to Copy",command=copyfn)


window.mainloop()


