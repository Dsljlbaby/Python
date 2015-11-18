from random import randint
num=randint(1,100)
times=0 
name=raw_input('Please enter your name:') #input player's name 

#define function
def guess_num(answer,num):
    if answer<num:
        print 'Too Small,Please try again!'
        return False
    elif answer>num:
        print 'Too Big,Please try again!'
        return False
    else:
        print 'Good Luck!'
        return True
    
#read the file    
game=file('game.txt')
lines=game.readlines()
game.close()

scores={} #create empty dictionary
for data in lines:
    s=data.split()
    scores[s[0]]=s[1:]
score=scores.get(name) # find the current player data
if score is None: 
    score=[0,0,0] #initialize the data    
game_time=int(score[0])
min_time=int(score[1])
total_time=int(score[2])
if game_time>0:
    avg_time=float((total_time) / (game_time))
else:
    avg_time=0
#output performance information
print 'Hi,%s!you had played %d wheel game' %(name,game_time)
print 'The mininum wheel is %d' %min_time
print 'The average wheel is %.2f' %avg_time

bingo=False
print'Guess what I think!'
while bingo==False:
    times+=1
    answer=input()
    if answer<0:
        print 'Game Over!'
        break #exit the game
    bingo=guess_num(answer,num)
    
   
if game_time==0 or times < min_time:
    min_time=times
total_time+=times
game_time+=1

scores[name]=[str(game_time),str(min_time),str(total_time)] #updata the data in the player
result='' #initialize the empty string,stored data
for num1 in scores:
    line=num1+' '+' '.join(scores[num1])+'\n'
    result+=line
    
game=open('game.txt','w')
game.write(result)
game.close()

        
    

