import math
import random
import turtle

raph = turtle.Turtle()
raph.speed(0)

def setupscreen(x, y):
    '''
    Creates a screen the size of x and y.  Resets coordinates to (0,0)
    at bottom left of screen
    '''
    turtle.setup(x, y)
    screen = turtle.Screen()
    screen.setworldcoordinates(0, 0, x, y)
    # sets raphs shape to circle
    raph.shape('circle')
    # goes to 0,0 without drawing there
    raph.penup()
    raph.goto(0, 0)
    # it draws a box as big as the screen
    raph.pendown()
    raph.goto(x,0)
    raph.goto(x,y)
    raph.goto(0,y)
    raph.goto(0,0)

    # place the target between 70% and 90% from the edge of the screen
    mintargetdistance=x*.7
    maxtargetdistance=x*.9
    targetdistance=random.randrange(mintargetdistance, maxtargetdistance)
    raph.penup()
    raph.goto(targetdistance,0)
    raph.stamp()

    # place the wall between 25% and 50% from the start
    # and between 10% and 30% of the height of the screen
    minwallheight=y*.1
    maxwallheight=y*.3
    minwalldistance=x*.25
    maxwalldistance=x*.50
    walldistance=random.randrange(minwalldistance, maxwalldistance)
    wallheight=random.randrange(minwallheight, maxwallheight)
    #this will draw the wall 
    raph.penup()
    raph.goto(walldistance, wallheight)
    raph.pendown()
    raph.goto(walldistance,0)
    raph.penup()
    raph.goto(0,0)
    raph.pendown()


def plot(x, y):
    '''
    moves the ball to x,y
    '''
    raph.goto(x, y)
#turtle.tracer(10, 0)

setupscreen(1500, 1000)

# #startingspeed=int(input("what is the starting speed"))
# #startingangle=int(input("what is the starting angle"))
startingspeed=150
startingangle=45
x=0
y=0

vx = startingspeed*math.cos(math.radians(startingangle))
vy = startingspeed*math.sin(math.radians(startingangle))

t=.01
timeinair=0
raph.shape("arrow")
while(y>=0):
    x=x+t*vx
    y=y+t*vy
    vy=vy-t*9.8

    # this calculates the new x value
    timeinair=timeinair+t
    plot(x,y)
turtle.update()
turtle.mainloop()
print(str (timeinair))


