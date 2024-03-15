from turtle import *
from random import *
from time import *

tracer(100)
speed(1000)
bgcolor('black')
width(5)

coords = [[0, 0]]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
size = 400

class turtle:
    def __init__(self):
        self.coords = [[randrange(size * -1, size, 10), randrange(size * -1, size, 10)]]
        self.color = colors[randint(0, len(colors)-1)]
        self.counter = 0

    def move(self):
        up()
        setpos(self.coords[-1])
        down()
        color(self.color)
        i = randint(0, 3)
        if i == 0 and not([self.coords[-1][0] + 10, self.coords[-1][1]] in self.coords):
            self.coords.append([self.coords[-1][0] + 10, self.coords[-1][1]])
            setpos(self.coords[-1])
        elif i == 1 and not([self.coords[-1][0] - 10, self.coords[-1][1]] in self.coords):
            self.coords.append([self.coords[-1][0] - 10, self.coords[-1][1]])
            setpos(self.coords[-1])
        elif i == 2 and not([self.coords[-1][0] , self.coords[-1][1] + 10] in self.coords):
            self.coords.append([self.coords[-1][0], self.coords[-1][1] + 10])
            setpos(self.coords[-1])
        elif i == 3 and not([self.coords[-1][0], self.coords[-1][1] - 10] in self.coords):
            self.coords.append([self.coords[-1][0], self.coords[-1][1] - 10])
            setpos(self.coords[-1])
        elif [self.coords[-1][0] + 10, self.coords[-1][1]] in self.coords and [self.coords[-1][0] - 10, self.coords[-1][1]] in self.coords and [self.coords[-1][0], self.coords[-1][1] + 10] in self.coords and [self.coords[-1][0] , self.coords[-1][1] - 10] in self.coords or abs(xcor()) > size or abs(ycor()) > size:
            self.color = (colors[randint(0, len(colors)-1)])
            up()
            self.coords = [[randrange(size * -1, size, 10), randrange(size * -1, size, 10)]]
            setpos(self.coords[-1])
            down()

k = int(input())
sp = [turtle() for _ in range(k)]

while True:
    for i in sp:
        i.move()

##while True:
##    sleep(0.25)
##    i = randint(0, 3)
##    if i == 0 and not([coords[-1][0] + 10, coords[-1][1]] in coords):
##        coords.append([coords[-1][0] + 10, coords[-1][1]])
##        setpos(coords[-1])
##    elif i == 1 and not([coords[-1][0] - 10, coords[-1][1]] in coords):
##        coords.append([coords[-1][0] - 10, coords[-1][1]])
##        setpos(coords[-1])
##    elif i == 2 and not([coords[-1][0] , coords[-1][1] + 10] in coords):
##        coords.append([coords[-1][0], coords[-1][1] + 10])
##        setpos(coords[-1])
##    elif i == 3 and not([coords[-1][0], coords[-1][1] - 10] in coords):
##        coords.append([coords[-1][0], coords[-1][1] - 10])
##        setpos(coords[-1])
##    elif [coords[-1][0] + 10, coords[-1][1]] in coords and [coords[-1][0] - 10, coords[-1][1]] in coords and [coords[-1][0], coords[-1][1] + 10] in coords and [coords[-1][0] , coords[-1][1] - 10] in coords or abs(xcor()) > 200 or abs(ycor()) > 200:
##        up()
##        coords = [[randrange(-200, 200, 10), randrange(-200, 200, 10)]]
##        setpos(coords[-1])
##        down()
