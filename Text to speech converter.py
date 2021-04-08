#imporing the required modules
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

#setting up the window
window=Tk()
window.title("Text to speech converter")
window.geometry("600x400")
window.config(bg="black")

#Adding a caption to the window
lbl=Label(window,text="TEXT TO SPEECH CONVERTER",font="Impact 20 bold",bg="black",fg="yellow").place(x=150,y=20)

#Declaring the variable
var=StringVar()
lbl1=Label(window,text="Enter the message:",font="Helvetica 18 bold",bg="black",fg="white").place(x=20,y=70)

#Taking input from the user
msg_entry=Entry(window,textvariable=var,width=60,font="bold")
msg_entry.grid(padx=20,pady=130,ipady=6)

#setting up the function
def play():
    Text=msg_entry.get()
    speech=gTTS(text=Text)
    speech.save('voice.mp3')
    playsound('voice.mp3')
    os.remove('voice.mp3')
def reset():
    var.set("")
def close():
    window.destroy()

#setting up the buttons
btn1=Button(window,text="PLAY",font="Helvetica 18 bold",bg="#52D017",fg="black",command=play).place(x=50,y=250)
btn2=Button(window,text="RESET",font="Helvetica 18 bold",bg="#0000A0",fg="black",command=reset).place(x=250,y=250)
btn3=Button(window,text="CLOSE",font="Helvetica 18 bold",bg="#F62217",fg="black",command=close).place(x=450,y=250)

window.mainloop()