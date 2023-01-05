from tkinter import *
from PIL import Image,ImageTk
from random import randint

#GUI window started 
window=Tk()
window.title("Rock Paper & Scissor")
window.configure(background="cornflowerblue")

#Photo assigned for futher usage
comp_rock_img=ImageTk.PhotoImage(Image.open("rockcomp.png"))
comp_paper_img=ImageTk.PhotoImage(Image.open("papercomp.png"))
comp_sci_img=ImageTk.PhotoImage(Image.open("scicomp.png"))

user_rock_img=ImageTk.PhotoImage(Image.open("rockuser.png"))
user_paper_img=ImageTk.PhotoImage(Image.open("paperuser.png"))
user_sci_img=ImageTk.PhotoImage(Image.open("sciuser.png"))


#labels to indicate the side of players 
user_indi=Label(window,font=("arial",40,"bold"),
                text="PLAYER",bg="orange",fg="blue")
comp_indi=Label(window,font=("arial",40,"bold"),
                text="SYSTEM",bg="orange",fg="blue")
comp_indi.grid(row=0,column=1)
user_indi.grid(row=0,column=3)


#Computer and user , initial photos 
label_user=Label(window,image=user_sci_img)
label_comp=Label(window,image=comp_sci_img)
label_comp.grid(row=1,column=0)
label_user.grid(row=1,column=4)

#initial score window 
comp_score=Label(window,text=0,font=('arial',60,"bold"),fg="red",bg="cornflowerblue")
user_score=Label(window,text=0,font=('arial',60,"bold"),fg="red",bg="cornflowerblue")
comp_score.grid(row=1,column=1)
user_score.grid(row=1,column=3)


#reset button function
def resetgame():                 
    final=int(comp_score['text'])
    final=0   
    comp_score["text"]=str(final)

    final=int(user_score['text'])
    final=0   
    user_score["text"]=str(final)

    label_user=Label(window,image=user_sci_img)
    label_comp=Label(window,image=comp_sci_img)
    label_comp.grid(row=1,column=0)
    label_user.grid(row=1,column=4)

    msg_updation("")
    

#function for the updation of the message that will be coming at last
def msg_updation(a):
    result['text']=a

result=Label(window,text='',font=("arial",40,"bold"),bg="red",fg="white") #text   #message-showing result
result.grid(row=4,column=2)


#Function for updating the computer & user score 
def comp_update():
    final=int(comp_score['text'])
    final+=1                     #increase's computer score
    comp_score["text"]=str(final)

def user_update():
    final=int(user_score['text'])
    final+=1                     #increase's user score 
    user_score["text"]=str(final)


#buttons for user choice input
rock_button=Button(window,width=16,height=3,text="ROCK",
                        font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:user_choice("rock")).grid(row=3,column=1)

paper_button=Button(window,width=16,height=3,text="PAPER",
                        font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:user_choice("paper")).grid(row=3,column=2)

scissor_button=Button(window,width=16,height=3,text="SCISSOR",
                        font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:user_choice("scissor")).grid(row=3,column=3)


#buttons to rest the game to initial state
reset_button=Button(window,width=16,height=2,text="RESET GAME",font=("arial",16,"bold"),bg="blue",
                    fg="red",command=resetgame)
reset_button.grid(row=5,column=2)


# function to update image on the basis of choice made
to_select = ["rock","scissor","paper"]
def user_choice(a):
    
    comp_choice=to_select[randint(0,2)]            # computer choice update
    if comp_choice == "rock":
        label_comp.configure(image=comp_rock_img)
    elif comp_choice == "paper":
        label_comp.configure(image=comp_paper_img)
    else:
        label_comp.configure(image=comp_sci_img)
    
    if a == "rock":
        label_user.configure(image=user_rock_img)
    elif a == "paper":
        label_user.configure(image=user_paper_img)
    else:
        label_user.configure(image=user_sci_img)
    
    winner_check(a,comp_choice)


#function for winner checking , msg-updation and score-updation
def winner_check(u,c):
    if u == c:
        msg_updation("It's a TIE :)")
    
    elif u == "rock":
        if c == "paper":
            msg_updation("YOU LOSE!")
            comp_update()
        else:
            msg_updation("YOU WIN !!")
            user_update()
    
    elif u == "paper":
        if c == "scissor":
            msg_updation("YOU LOSE!")
            comp_update()
        else:
            msg_updation("YOU WIN !!")
            user_update()
    
    elif u == "scissor":
        if c == "rock":
            msg_updation("YOU LOSE!")
            comp_update()
        else:
            msg_updation("YOU WIN !!")
            user_update()
    
    else:
        pass


# function to open a new window
def openNewWindow():
	
	# Toplevel object which will be treated as a new window
	newWindow = Toplevel(window)

	# sets the title of the Toplevel widget
	newWindow.title("Game Result")

	# sets the geometry of toplevel
	newWindow.geometry("500x500")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="This is the new window ").pack()


label = Label(window,
			text ="This is the main window")


# result window open karne ka button
btn = Button(window,width=16,height=3,
			text ="RESULT",
			command = openNewWindow,bg="blue",
                    fg="red")
btn.grid(row=7,column=2)


# The end of the Program for Rock , Paper & Scissor Game .
window.mainloop()




























