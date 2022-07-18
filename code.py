from tkinter import *
from setuptools import Command
from textblob import TextBlob
import textblob 
def correcttheword():
    inputword=word1.get()
    obj=TextBlob(inputword)
    correctedword=str(obj.correct())
    word2.delete(0,END)
    word2.insert(10,correctedword)
def clearall():
    word1.delete(0,END)
    word2.delete(0,END)    
if(__name__=='__main__'):
    root=Tk()
    root.configure(background='lightblue')
    root.title('Error Saver')
    root.geometry('500x250')
    header=Label(root,text='Welcome To The Error Saver App',fg='black',bg='lightblue')
    header.grid(row=0,column=1)
    label1=Label(root,text='Input word',fg='black',bg='lightblue')
    label1.grid(row=1,column=0)
    label2=Label(root,text='Corrected word',fg='black',bg='lightblue')
    label2.grid(row=3,column=0)
    word1=Entry()
    word2=Entry()
    word1.grid(row=1,column=1)
    word2.grid(row=3,column=1)
    button1=Button(root,text='Correction',fg='black',bg='red',command=correcttheword)

    button1.grid(row=2,column=1,pady=10)
    button2=Button(root,text='Clear all',fg='black',bg='red',command=clearall)
    button2.grid(row=4,column=1,pady=10)
    root.mainloop()