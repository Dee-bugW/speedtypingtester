import sys
import time
import random
import tkinter
from tkinter import *
from tkinter import messagebox

#using one piece quotes for fun
Sentences=["It doesn't matter if you're a king, or even if you're a god. It doesn't matter if you're someone who's great, or if you're someone who's not so great.",
           "They're not all strong like me, but either way, they're my friends and I wanna keep em","I don't want to rule anything. Being King of the Pirates is about being more free than anyone.",
           "As long as I'm still alive, I have infinite chances.","Scars on the back are a swordsman's shame.","Everyone has things that they can do and things that they cant."]

class Main:
    def __init__(self,root):
        self.root=root
        self.root.title("Typing Speed Tester")
        self.root.config(bg="black",padx=50,pady=50)

        self.sentence=""
        self.start_time=None

        self.label_sentence=tkinter.Label(root,text="",font=("Courier",24,"bold"),wraplength=600,bg="black",fg="white")
        self.label_sentence.grid(row=0,column=0,columnspan=2,pady=10)

        self.entry=tkinter.Entry(root,width=60,font=("Courier",24,"bold"))
        self.entry.grid(row=1,column=0,pady=10)
        self.entry.bind("<Return>",self.result)

        self.start=tkinter.Button(root,text="Start",command=self.start_typing,font=("Courier",24,"bold"))
        self.start.grid(row=2,column=0,pady=10)

        self.submit=tkinter.Button(root,text="Submit",command=self.result,font=("Courier",24,"bold"))
        self.submit.grid(row=2,column=1,pady=10)

        self.label_result=tkinter.Label(root,text="",font=("Courier",24,"bold"),bg="black",fg="red")
        self.label_result.grid(row=3,column=0,columnspan=2,pady=10)

    def start_typing(self): #keep these def functions inside the class
        self.sentence=random.choice(Sentences)
        self.label_sentence.config(text=self.sentence)
        self.entry.delete(0,tkinter.END)
        self.label_result.config(text="")
        self.start_time=time.time()

    def result(self,event=None):
        end=time.time()
        total=round(end-self.start_time,2)
        typed_text=self.entry.get()

        correct=sum(1 for a,b in zip(typed_text,self.sentence) if a==b)
        accuracy=round((correct/len(self.sentence))*100,2)
        words=len(typed_text.split())
        wpm=round((words/total)*60,2) if total>0 else 0

        self.label_result.config(text=f"Time: {total}s , WPM: {wpm} , Accuracy: {accuracy}%")
        self.start_time=None

if __name__=="__main__":
    root=tkinter.Tk()
    app=Main(root)
    root.mainloop()

