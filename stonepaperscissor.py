import random
print("select 1 for stone")
print("select 2 for scissor")
print("select 3 for paper")
input1=int(input('enter a number between  1 and 3(also including 1 and 3):'))
num=random.randint(1,3)
if(num==1):
    cmove='stone'
elif(num==2):
    cmove="scissor"
else:
    cmove="paper"
if(input1==1):
    pmove='stone'
elif(input1==2):
    pmove='scissor'
elif(input1==3):
    pmove='paper'
else:
    print("invalid input")
if(pmove=='stone'):
    if(cmove=='stone'):
        print("stone cannot beat stone")
    elif(cmove=='scissor'):
        print("stone beats scissor,you WIN")
    else:
        print("stone loses to paper hence you lose")
elif(pmove=='scissor'):
    if(cmove=='stone'):
        print("scissor cannot beat stone,you LOSE")
    elif(cmove=='scissor'):
        print("scissor cannot beat scissor")
    else:
        print("scissor cuts paper,you WIN")
if(pmove=='paper'):
    if(cmove=='stone'):
        print("paper can beat stone,you WIN")
    elif(cmove=='scissor'):
        print("paper cannot beat scissor,you LOSE")
    else:
        print("paper cannot beat paper")        

                            

                    

    

 