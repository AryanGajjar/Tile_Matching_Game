from tkinter import *

root = Tk()
root.geometry("400x400")
#creating a label widget
myLabel = Label(root,text="Hello World!!")
myLabel2 = Label(root,text="The name's gajjar, Aryan Gajjar ")
#inserting the label through pack
myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()

