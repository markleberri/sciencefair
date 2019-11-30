import math

def plot(x, y):
    print("x = " + str(x))
    print("y = " + str(y))

#startingspeed=int(input("what is the starting speed"))
#startingangle=int(input("what is the starting angle"))
startingspeed=100
startingangle=45
x=0
y=0

vx = startingspeed*math.cos(math.radians(startingangle))
vy = startingspeed*math.sin(math.radians(startingangle))

t=.0001
timeinair=0

while(y>=0):
    x=x+t*vx
    y=y+t*vy
    vy=vy-t*9.8

    # this calculates the new x value
    timeinair=timeinair+t
    plot(x,y)
print(str (timeinair))
