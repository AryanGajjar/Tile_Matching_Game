from cgitb import text
from pdb import Restart
from tkinter import *
from tkinter import messagebox
import random
from tkinter import messagebox
from unittest import TestCase
root= Tk()
root.title(" MatchTiles ")
root.geometry("550x550")
#creating global vars,
global matches,winner
winner = 0
#creating list of numbers for matching
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)
#creating frame of buttons
my_frame = Frame(root)
my_frame.pack(pady=10)
#delcaring th variables to store the  counr and answers
cnt = 0
ans_list = []
ans_dict = {}
#creating win function.
def win():
    Buttons_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for button in Buttons_list:
        button.config(bg="cyan")
    my_label.config(text="Congratulations, you Win!!")

#creating the restart function,
def restart():
    global matches,winner
    winner = 0
    #reseting the values of the list,
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches)
    #reset the label,
    my_label.config(text=" ")
    #reset the tiles/buttons,
    Buttons_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for button in Buttons_list:
        button.config(text=" ",bg="SystemButtonFace",state="normal")

#creating the main function for buttons operations
def Button_click(b,num):
    global cnt,ans_list,ans_dict,winner
    if b["text"] == ' ' and cnt < 2:
        b["text"] = matches[num]
        ans_list.append(num)
        ans_dict[b] = matches[num]
        cnt += 1

    if len(ans_list) == 2:
        if matches[ans_list[0]] == matches[ans_list[1]]:
            my_label.config(text="MATCH!!")
            for key in ans_dict:
                key["state"] = "disabled"
            ans_list = []
            ans_dict = {}
            cnt = 0
            winner += 1
            if winner == 6:
                win()

        else:
            my_label.config(text="try again!!")
            ans_list=[]
            messagebox.showinfo("Incorrect!","Incorrect")
            for key in ans_dict:
                key["text"] = " "
            ans_dict = {}
            cnt = 0


#creating buttons for numbers in the list matches
b0 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b0,0),relief="groove")
b1 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b1,1),relief="groove")
b2 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b2,2),relief="groove")
b3= Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b3,3),relief="groove")
b4 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b4,4),relief="groove")
b5 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b5,5),relief="groove")
b6 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b6,6),relief="groove")
b7 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b7,7),relief="groove")
b8 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b8,8),relief="groove")
b9 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b9,9),relief="groove")
b10 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b10,10),relief="groove")
b11 = Button(my_frame,text=' ',font=("Helvetica",20),height=3,width=6,command=lambda: Button_click(b11,11),relief="groove")

#creating grid of the buttons.
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

my_label = Label(root,text=" ")
my_label.pack(pady=20)

#creating menu for restart & exit game,
my_menu = Menu(root)
root.config(menu=my_menu)
#creatinf the tabss
file_menu = Menu(my_menu,tearoff=True)
my_menu.add_cascade(label="Options",menu=file_menu)
file_menu.add_command(label="Restart",command= restart)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
root.mainloop()