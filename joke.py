from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo("","I knew it XD")
    quit()

def motinMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

def disable_close_button():
    pass

root = Tk()
root.protocol("WM_DELETE_WINDOW", disable_close_button)
root.geometry("600x600")
root.title("Survey")
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Are you gay?', font='Arial 20 bold', bg="white").pack()
btnYes = Button(root,text='No', font="Arial 20 bold")
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motinMouse)
btnNo = Button(root, text='Yes',font='Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()