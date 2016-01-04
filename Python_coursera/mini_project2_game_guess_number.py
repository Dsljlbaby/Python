#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simplegui
import math
import random


# initialize global variables used in your code here
num_range = 100
secret_num = 0
guesses_left = 0


# helper function to start and restart the game
# add code to the function:new_game()
def new_game():
    global num_range
    global secret_num
    global guesses_left
    
    secret_num = random.randrange(0, num_range)
    
    if num_range == 100 : 	
        guesses_left = 7
    elif num_range == 1000 :
        guesses_left = 10  
        
    print "New game. The range is from 0 to", num_range, ". Good luck!"
    print "Number of remaining guesses is ", guesses_left, "\n"

    
# define event handlers for control panel
# add code to the function:range100()
 # button that changes the range to [0,100) and starts a new game     
def range100():
    global num_range
    num_range = 100 
    new_game() 

    
# add code to the function:range1000()
# button that changes the range to [0,1000) and starts a new game
def range1000(): 
    global num_range
    num_range = 1000 
    new_game()
    
    
# main game logic goes here		    
def input_guess(guess):
    global guesses_left
    global secret_num
    
    won = False
    
    print "You guessed: ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
           
    if won:
        print "That is correct! Congratulations!\n"
        new_game()
        return
    elif guesses_left == 0:
        print "Game over. You didn't guess the number in time!"   
        new_game()
        return
    else:
        print result
        
        
# create frame
frame = simplegui.create_frame("Game: Guess the number!", 200, 200)
frame.set_canvas_background('Block')


# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 100)
frame.add_button("Range is [0, 1000)", range1000, 100)	
frame.add_input("Enter your guess", input_guess, 100)


# call new_game 
new_game()
frame.start()
