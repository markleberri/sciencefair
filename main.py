import math
import turtle

raph = turtle.Turtle()
raph.speed(0)
def setupscreen(x, y):
    '''
    Creates a screen the size of x and y
    '''
    turtle.setup(x, y)
    screen = turtle.Screen()
    screen.setworldcoordinates(0, 0, x, y)
    raph.shape('circle')
    raph.penup()
    raph.goto(0, 0)
    raph.pendown()
    raph.goto(x,0)
    raph.goto(x,y)
    raph.goto(0,y)
    raph.goto(0,0)

def plot(x, y):
    raph.goto(x,y)

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

while(y>=0):
    x=x+t*vx
    y=y+t*vy
    vy=vy-t*9.8

    # this calculates the new x value
    timeinair=timeinair+t
    plot(x,y)
print(str (timeinair))

