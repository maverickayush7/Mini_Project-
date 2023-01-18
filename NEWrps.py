from tkinter import *
from PIL import Image,ImageTk
from random import randint
window1=Tk()
window1.geometry("1275x1275")
window1.title("Rock Paper & Scissor")

c=Canvas(window1,bg="gray16",height=2000,width=2000)
filename=ImageTk.PhotoImage(Image.open("rps_wallpaper.jpg"))
background_label=Label(window1,image=filename)
background_label.place(x=12,y=12,relwidth=1,relheight=1)
c.place(x=10,y=20)



def open_game_window():
    
    
    # import tkinter as Tk
    # from PIL import Image,ImageTk
    # from random import randint

#GUI window started   
    window = Toplevel(window1)
    # window=Tk()
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
                            font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:user_choice("rock"))
    rock_button.grid(row=3,column=1)


    paper_button=Button(window,width=16,height=3,text="PAPER",
                            font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:user_choice("paper"))
    paper_button.grid(row=3,column=2)
    
    scissor_button=Button(window,width=16,height=3,text="SCISSOR",
                            font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:user_choice("scissor"))
    scissor_button.grid(row=3,column=3)

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
    def winner_check(u,c):                  #u for user_choice & c for comp_choice
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
    window.mainloop()   
   

# The end of the Program for Rock , Paper & Scissor Game .
btn = Button(window1,text ="START GAME",fg='blue',bg='red',height='2',width='20', command = open_game_window)
btn.place(x=800,y=130)

# window1.mainloop()



def open_help_window():
	
	newWindow = Toplevel(window1)
	newWindow.title("HELP")
	newWindow.geometry("1275x1275")
	Label(newWindow,text ="How To Play",font=('Agency FB bold', 30),fg='blue').pack()
	label2=Label(newWindow,text=''' describe here ''',font=('aharoni',15))
	label2.place(x=5,y=100)
btn = Button(window1,text ="HELP",fg='yellow',bg='black',height='1',width='20',command = open_help_window)
btn.place(x=1100,y=600)



def open_credits_window():
	
	newWindow = Toplevel(window1)
	newWindow.title("CREDITS")
	newWindow.geometry("1275x1275")
	Label(newWindow,text ="TEAM MEMBERS",font=('Agency FB bold', 30),fg='blue').pack()
	label2=Label(newWindow,text='''
AYUSH KUMAR
ATHRAV GANESH
ANJANI
LOHITH
''',font=('aharoni',35))
	label2.place(x=400,y=100)
btn = Button(window1,text ="CREDITS",fg='yellow',bg='black',height='1',width='20',command = open_credits_window)
btn.place(x=25,y=600)


# mainloop()
window1.mainloop()