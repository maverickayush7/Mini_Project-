from tkinter import *
from PIL import Image,ImageTk
from random import randint

#gui window suru kari
window=Tk()
window.title("Rock Paper & Scissor")
window.configure(background="cornflowerblue")

#photo insert kare
imgrockcomp=ImageTk.PhotoImage(Image.open("rockcomp.png"))
imgpapercomp=ImageTk.PhotoImage(Image.open("papercomp.png"))
imgscicomp=ImageTk.PhotoImage(Image.open("scicomp.png"))

imgrockuser=ImageTk.PhotoImage(Image.open("rockuser.png"))
imgpaperuser=ImageTk.PhotoImage(Image.open("paperuser.png"))
imgsciuser=ImageTk.PhotoImage(Image.open("sciuser.png"))

#comp and user ke niche dispaly hone wali photos initial photos 
labeluser=Label(window,image=imgsciuser)
labelcomp=Label(window,image=imgscicomp)
labelcomp.grid(row=1,column=0)
labeluser.grid(row=1,column=4)


def resetgame():
    final=int(compscore['text'])
    final=0   #score inc hota rahega
    compscore["text"]=str(final)

    final=int(userscore['text'])
    final=0   #score inc hota rahega
    userscore["text"]=str(final)

    msgupdation("")
    

#score window banaye hai 

compscore=Label(window,text=0,font=('arial',60,"bold"),fg="red",bg="cornflowerblue")
userscore=Label(window,text=0,font=('arial',60,"bold"),fg="red",bg="cornflowerblue")
compscore.grid(row=1,column=1)
userscore.grid(row=1,column=3)

#function for the updation of the message that will be coming at last
def msgupdation(a):
    result['text']=a

#fuction for updating the comp & user score 
def compupdate():
    final=int(compscore['text'])
    final+=1   #score inc hota rahega
    compscore["text"]=str(final)


def userupdate():
    final=int(userscore['text'])
    final+=1   #score inc hota rahega
    userscore["text"]=str(final)

#function for winner checking
def winner_check(u,c):
    if u == c:
        msgupdation("It's a TIE :)")
    elif u == "rock":
        if c == "paper":
            msgupdation("YOU LOSE!")
            compupdate()
        else:
            msgupdation("YOU WIN !!")
            userupdate()
    
    elif u == "paper":
        if c == "scissor":
            msgupdation("YOU LOSE!")
            compupdate()
        else:
            msgupdation("YOU WIN !!")
            userupdate()
    
    elif u == "scissor":
        if c == "rock":
            msgupdation("YOU LOSE!")
            compupdate()
        else:
            msgupdation("YOU WIN !!")
            userupdate()
    
    else:
        pass
to_select = ["rock","paper","scissor"]

def choice_update(a):
    
   

    choice_comp=to_select[randint(0,2)]
    if choice_comp == "rock":
        labelcomp.configure(image=imgrockcomp)
    elif choice_comp == "paper":
        labelcomp.configure(image=imgpapercomp)
    else:
        labelcomp.configure(image=imgscicomp)
    
    if a == "rock":
        labeluser.configure(image=imgrockuser)
    elif a == "paper":
        labeluser.configure(image=imgpaperuser)
    else:
        labeluser.configure(image=imgsciuser)
    
    winner_check(a,choice_comp)


    
#msg ki kon jeta aur kon hara
result=Label(window,font=("arial",40,"bold"),bg="red",fg="white")
result.grid(row=4,column=2)


#indicator ki ye comp ki place hai aur ye user ki place hai

user_indi=Label(window,font=("arial",40,"bold"),
                text="PLAYER",bg="orange",fg="blue")
comp_indi=Label(window,font=("arial",40,"bold"),
                text="SYSTEM",bg="orange",fg="blue")
comp_indi.grid(row=0,column=1)
user_indi.grid(row=0,column=3)





buttonrock=Button(window,width=16,height=3,text="ROCK",
                        font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:choice_update("rock")).grid(row=3,column=1)

buttonpaper=Button(window,width=16,height=3,text="PAPER",
                        font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:choice_update("paper")).grid(row=3,column=2)

buttonscissor=Button(window,width=16,height=3,text="SCISSOR",
                        font=("arial",20,"bold"),bg="yellow",fg="purple",command=lambda:choice_update("scissor")).grid(row=3,column=3)

buttonreset=Button(window,width=16,height=2,text="RESET GAME",font=("arial",16,"bold"),bg="blue",
                    fg="red",command=resetgame)
buttonreset.grid(row=5,column=2)


window.mainloop()


