import tkinter as tk
from tkinter import ttk
from tkinter import Menu
win = tk.Tk()
win.title("first gui")


thislabel = ttk.Label(win,text="what is your name?")
thislabel.grid(column=0,row=0)



def clickme():
    thisbutton.configure(text="dear" + name.get())

#button
thisbutton = ttk.Button(win, text="enter", command=clickme )
thisbutton.grid(column=1,row=1)

#textarea
name = tk.StringVar()
thistext = ttk.Entry(win,width=12, textvariable=name)
thistext.grid(column=0,row=1)
thistext.focus()

#combobox
ttk.Label(win,text="this is a combobox").grid(column=0,row=3)
num =tk.StringVar()
numbers = ttk.Combobox(win, width=5, textvariable=num, state='readonly')
numbers.grid(column=1,row=3)
numbers['values']=(1,2,3,4,5)
numbers.current(0)

#menu
menuBar = Menu(win)
win.config(menu=menuBar)

filebar = Menu(menuBar, tearoff=0)
filebar.add_cascade(label="file", menu=menuBar)
filebar.add_command(label="about")
filebar.add_separator()

filebar.add_command(label="exit")



win.mainloop()
