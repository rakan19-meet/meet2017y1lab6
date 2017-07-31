
def up ():
    global direction
    direction=UP
    print ('you moved up')


def left ():
    global direction
    direction=LEFT
    print ('you moved left')
    
def right ():
    global direction
    direction=RIGHT
    print ('you moved right')


def down ():
    global direction
    direction=DOWN
    print ('you moved down')

#################################################
import turtle

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"


UP=0
LEFT=1
RIGHT=2
DOWN=3


direction=UP

    
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()



turtle.mainloop()

def up():
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos())
