print("""Game of Rock Paper and Scissor 
Possible Choice:
(1) Rock enter --> R (2) Paper enter --> P (3) Scissor enter --> S""")
num=int(input("Enter the the number of times you want to play : "))
user_s=0
comp_s=0    
for i in range(1,num+1):
    import random
    a=input("enter choice : ")
    b=a.upper()
    if b=="R":
        user=0
        u="ROCK"
    elif b=="P":
        user=1
        u="PAPER"    
    elif b=="S":
        user=2
        u="SCISSOR"
    else:
        print("Invalid input")   
    c=random.randint(0, 2) 
    if c==0:
        print("Computer choice : ROCK",end=" ")
    elif c==1:
        print("Computer choice : PAPER",end=" ")    
    elif c==2:
        print("Computer choice : SCISSOR",end=" ")
    print("User Choice : ",u)  
    if user==c:
        print("TIE!")
    elif (user==0 and c==1) or (user==1 and c==2) or (user==2 and c==0):
        print("USER LOST!")
        comp_s+=1
    elif (user==1 and c==0) or (user==2 and c==1) or (user==0 and c==2):    
        print("USER WINS!")
        user_s+=1
print("---------------------------------------------------------------------------------------------------")
print("USER SCORE : ",user_s)
print("COMPUTER SCORE : ",comp_s)
if user_s > comp_s :
    print("USER WINS THE GAME!")
elif user_s < comp_s :
    print("COMPUTER WINS THE GAME!")
elif user_s == comp_s :                  
    print("GAME IS TIED!")
print("---------------------------------------------------------------------------------------------------")