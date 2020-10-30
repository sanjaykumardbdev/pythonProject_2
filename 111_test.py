from tkinter import *
import datetime

root = Tk()

date = str(datetime.datetime.now().date())
print(date)


# need two frames: topFrame  bottomFrame
topFrame = Frame(root, height=150, bg='white')
topFrame.pack(fill=X)

bottomFrame = Frame(root, height=350, bg='#7fe3a7')
bottomFrame.pack(fill=X)


heading = Label(topFrame, text='TEST****', bg='white', fg='blue', font='arial 15 bold')
heading.place(x=200, y=50)

date_lbl = Label(topFrame, text="Today's Date:" + date, font='arial 12 bold', fg='#7fe3a7', bg='white')
date_lbl.place(x=300, y=110)

scroll = Scrollbar(bottomFrame, orient=VERTICAL)

listbox = Listbox(bottomFrame, width=40, height=27)
listbox.grid(row=0, column=0)
listbox.config(yscrollcommand=scroll.set)

scroll.config(command=listbox.yview())
scroll.grid(row=0, column=1,sticky=N+S)

for i in range(200):
    listbox.insert(END,'listitem: ' + str(i))


root.geometry('500x500+150+100')
root.title('My People')
root.resizable(False, False)

root.mainloop()