import tkinter as tk
from tkinter import ttk
from tkinter import Menu
win = tk.Tk()
win.title("first gui")


thislabel = ttk.Label(win,text="---------Program to minimise debt accounting---------")
thislabel.grid(column=0,row=0)


# this_button
def clickme():
    thisbutton.configure(text="The result is:")

    a1 = int(tl1.get())
    a2 = int(tl2.get())
    b1 = int(tl3.get())
    b2 = int(tl4.get())
    c1 = int(tl5.get())
    c2 = int(tl6.get())

    if a1 > b1 and b2 > c2:
        diff = a1-b1
        print("user1 owes user2:" + str(diff) + "\nuser2 owes user1: 0")
        ans1 = ttk.Label(win,text="Amount user1 owes user2: " + str(diff) + "\nAmount user2 owes user1: 0")
        ans1.grid(column=0,row=9)

        diff1 = b2-c2

        ans2 = ttk.Label(win,text="Amount user2 owes user3: " + str(diff1) + "\nAmount user3 owes user2: 0")
        ans2.grid(column=0,row=10)

        if diff > diff1:
            diff2 = diff - diff1 # new a1- new b2
            ans3 = ttk.Label(win,text="Amount user1 owes user2: " + str(diff2) + "\nAmount user1 owes user3: " + str(diff1))
            ans3.grid(column=0,row=11)
        else:
            diff2 = diff1 - diff
            ans3 = ttk.Label(win,text="Amount user1 owes user2: " + str(diff1) + "\nAmount user1 owes user3: " + str(diff2))
            ans3.grid(column=0,row=11)

    elif a1 < b1 and b2 < c2:
        diff = b1 - a1
        print("user1 owes user2:" + str(diff) + "\nuser2 owes user1: 0")
        ans1 = ttk.Label(win,text="Amount user2 owes user1: " + str(diff) + "\nAmount user1 owes user2: 0")
        ans1.grid(column=0,row=9)

        diff1 = c2-b2

        ans2 = ttk.Label(win,text="Amount user3 owes user2: " + str(diff1) + "\nAmount user2 owes user3: 0")
        ans2.grid(column=0,row=10)

        if diff > diff1:
            diff2 = diff - diff1 # new a1- new b2
            ans3 = ttk.Label(win,text="Amount user3 owes user2: " + str(diff2) + "\nAmount user3 owes user1: " + str(diff1))
            ans3.grid(column=0,row=11)
        else:
            diff2 = diff1 - diff
            ans3 = ttk.Label(win,text="Amount user3 owes user2: " + str(diff2) + "\nAmount user3 owes user1: " + str(diff))
            ans3.grid(column=0,row=11)

    elif a1 < b1 and b2 > c2:
        diff = b1-a1
        print("user2 owes user1:" + str(diff) + "\nuser1 owes user2: 0")
        ans1 = ttk.Label(win,text="Amount user1 owes user2: " + str(diff) + "\nAmount user2 owes user1: 0")
        ans1.grid(column=0,row=9)

        diff1 = b2-c2

        ans2 = ttk.Label(win,text="Amount user2 owes user3: " + str(diff1) + "\nAmount user3 owes user2: 0")
        ans2.grid(column=0,row=10)


    elif a1 > b1 and b2 < c2:
        diff = a1-b1
        print("user2 owes user1:" + str(diff) + "\nuser1 owes user2: 0")
        ans1 = ttk.Label(win,text="Amount user1 owes user2: " + str(diff) + "\nAmount user2 owes user1: 0")
        ans1.grid(column=0,row=9)

        diff1 = c2-b2

        ans2 = ttk.Label(win,text="Amount user2 owes user3: " + str(diff1) + "\nAmount user2 owes user3: 0")
        ans2.grid(column=0,row=10)


tl1 = tk.StringVar()
tl2 = tk.StringVar()
tl3 = tk.StringVar()
tl4 = tk.StringVar()
tl5 = tk.StringVar()
tl6 = tk.StringVar()

#button
thislabel1 = ttk.Label(win,text="Amount user1 owes user2")
thislabel1.grid(column=0,row=1)
thistext1 = ttk.Entry(win,width=6, textvariable=tl1)
thistext1.grid(column=1,row=1)

thislabel2 = ttk.Label(win,text="Amount user1 owes user3")
thislabel2.grid(column=0,row=2)
thistext2 = ttk.Entry(win,width=6, textvariable=tl2)
thistext2.grid(column=1,row=2)

thislabel3 = ttk.Label(win,text="Amount user2 owes user1")
thislabel3.grid(column=0,row=3)
thistext3 = ttk.Entry(win,width=6, textvariable=tl3)
thistext3.grid(column=1,row=3)

thislabel4 = ttk.Label(win,text="Amount user2 owes user3")
thislabel4.grid(column=0,row=4)
thistext4 = ttk.Entry(win,width=6, textvariable=tl4)
thistext4.grid(column=1,row=4)

thislabel5 = ttk.Label(win,text="Amount user3 owes user1")
thislabel5.grid(column=0,row=5)
thistext5 = ttk.Entry(win,width=6, textvariable=tl5)
thistext5.grid(column=1,row=5)

thislabel6 = ttk.Label(win,text="Amount user3 owes user2")
thislabel6.grid(column=0,row=6)
thistext6 = ttk.Entry(win,width=6, textvariable=tl6)
thistext6.grid(column=1,row=6)

thisbutton = ttk.Button(win, text="submit", command=clickme)
thisbutton.grid(column=1,row=8)

win.mainloop()
