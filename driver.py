#Creating tkinter GUI
import os
import tkinter
import tkinter as tk
from tkinter import *
from data_engine import Engine 
from sound_engine import text2speech  
from PIL import ImageTk, Image
from gtts import gTTS
from speech2txt import speech2txt 

E = Engine() 

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "You: " + msg + '\n\n')
        ChatBox.config(foreground="#446665", font=("Verdana", 12 ))

        res  = E.get_data(msg)
        res1  = res.split(',')
        res1 = "\n\t".join(res1) 

        ChatBox.insert(END, "CoBot: " + res1 + '\n\n')

 
        ChatBox.config(state=DISABLED)
        ChatBox.yview(END)
        text2speech(res, E.count)




if __name__ == "__main__":

   #Welcome()
   root = Tk()
   root.title("Covid-19 Information System developed by Jayanti Prasad")
   root.geometry("600x400")
   root.resizable(width=FALSE, height=FALSE)
   root.config(background="darkblue")
   img = ImageTk.PhotoImage(Image.open("app.png"))
   imglabel = Label(root, image=img).grid(row=1, column=1) 


   #Create Chat window
   ChatBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)

   ChatBox.config(state=DISABLED)

   #Bind scrollbar to Chat window
   scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
   ChatBox['yscrollcommand'] = scrollbar.set

   #Create Button to send message
   SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= send )

   #Create Button to send message
   AudioButton = Button(root, font=("Verdana",12,'bold'), text="Audio", width="12", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= text2speech)


   #Create the box to enter message
   EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")


   #Place all components on the screen
   scrollbar.place(x=560,y=6, height=400)
   ChatBox.place(x=6,y=16, height=250, width=520)
   EntryBox.place(x=6, y=300, height=90, width=390)
   SendButton.place(x=400, y=300, height=87)
   #AudioButton.place(x=6, y=180, height=90)

   root.mainloop()
