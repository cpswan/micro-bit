from microbit import *                  # standard Micro:Bit libraries
from array import *                     # to use an array
import random                           # generate random numbers

count = 0                               # initialise counter to 0
wait = 500                              # initialise wait to half a sec
sequence = array('B',[])                # array to hold sequence
display.show("-")                       # start out showing a dash

def squark(dir):                        # function to show arrows
    global wait
    if dir==0:                          # Right
        display.show(Image.ARROW_E)
    elif dir==1:                        # Left
        display.show(Image.ARROW_W)
    elif dir==2:                        # Down
        display.show(Image.ARROW_S)
    elif dir==3:                        # Up
        display.show(Image.ARROW_N)
    else:
        display.show("-")
    sleep(wait)
    display.show("-")
    sleep(wait)

def play_sequence():
    global count                        # use the count global variable
    global sequence                     # use the sequence global variable 
    global wait                         # use the wait global variable
    sequence.append(random.randint(0, 3))       # add a new value to sequence
    for i in range(0, count):           # loop for sequence length
      squark(sequence[i])               # display the arrow
    wait = 500 - (count * 15)           # vary delay to speed things up
    count = count+1                     # increment sequence length
    
def get_tilt():
    x = accelerometer.get_x()           # read left-right tilt
    y = accelerometer.get_y()           # read up-down tilt
    if x > 100:
        return 0                        # Right
    elif x < -100:
        return 1                        # Left
    elif y > 100:
        return 2                        # Down
    elif y < -100:
        return 3                        # Up
    else:
        return 4                        # Flat
        
def reset_game(): 
   global count
   global sequence
   count=0
   sequence=[]    

def read_sequence():
    global count
    global sequence
    display.show("*")                   # Show that we're waiting
    for i in range(0, count-1):
        while get_tilt()==4:            # Wait for a tilt
            sleep(50)
        input=get_tilt()
        if input == sequence[i]:        # If it's right then show it
            squark(input)
            if i==9:                    # We have a winner
                display.show(Image.SMILE)
                sleep(1000)
                display.show("WINNER")
                reset_game()
        else:
            display.show("X")           # Wrong tilt - game over
            sleep(1000)
            display.show("TRY AGAIN")
            reset_game()
            break
        
while True:
    play_sequence()                     # play the sequence to be remembered
    read_sequence()                     # read the sequence from the player
    sleep(1000)                         # wait a sec
