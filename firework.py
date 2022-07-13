#import modules
import turtle
import random
import time
#set screen size
win = turtle.Screen()
win.screensize (600,600)

#set turtle for firework
start = turtle.Turtle()
#set turtles for burst
burst1 = turtle.Turtle()
burst2 = turtle.Turtle()
build = turtle.Turtle()

burst1.ht()
colors = ["#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000","#800080","#008080","#000080"]

#background color


#start firework (base)(clear after each step?)

def building():
    build.ht()
    build.pencolor("white")
    build.speed(20)
    build.up()
    build.goto(-350,-300)
    build.down()
    build.setheading(0)
    build.forward(10)
    for x in range(10):
        build.setheading(90)
        build1 = random.randint(10,50)
        build.forward(build1)
        build.setheading(0)
        build.forward(random.randint(10,20))
        build.setheading(270)
        build.forward(build1)
        build.setheading(0)
        build.forward(random.randint(1,20))
    build.pencolor("black")
    build.forward(25)
    build.pencolor("white")
    build.forward(10)
    for x in range(10):
        build.setheading(90)
        build1 = random.randint(10,50)
        build.forward(build1)
        build.setheading(0)
        build.forward(random.randint(10,20))
        build.setheading(270)
        build.forward(build1)
        build.setheading(0)
        build.forward(random.randint(1,20))
    


def base():
    for x in range(1):
        start.ht()
        start.pencolor("White")
        start.pensize(1)
        start.speed(0)
        start.up()
        start.goto(random.randint(-300,300),-300)
        start.down()
        start.setheading(90)
        for x in range(random.randint(5, 45)):
               start.forward(5)
               start.up()
               start.forward(5)
               start.down()
               start.clear()

#burst
def burst():
    head = 15
    burst1.speed(0)
    burst1.pensize(2)
    for x in range(25):
        turtle.tracer(10,0)
        burst1.ht()
        burst1.up()
        burst1.goto(start.xcor(),start.ycor())
        burst1.down()
        burst1.setheading(head)
        for x in range(5):
            burst1.color(random.choice(colors))
            burst1.forward(random.randint(3, 15))
            burst1.up()
            burst1.forward(random.randint(3, 15))
            burst1.down()
            head = head + 15
            turtle.update()
            
def burstcool():
    head = 15
    burst1.speed(0)
    burst1.pensize(3)
    for x in range(25):
        turtle.tracer(0,0)
        burst1.ht()
        burst1.up()
        burst1.goto(start.xcor(),start.ycor())
        burst1.down()
        burst1.setheading(head)
        for x in range(5):
            burst1.color(random.choice(colors))
            burst1.forward(random.randint(3, 15))
            burst1.up()
            burst1.forward(random.randint(3, 15))
            burst1.down()
            head = head + 15
            turtle.update()
            

def small_burst():
    head = 15
    burst2.speed(0)
    burst2.pensize(1)
    for x in range(25):
        turtle.tracer(10,0)
        burst2.ht()
        burst2.up()
        burst2.goto(start.xcor(),start.ycor())
        burst2.down()
        burst2.setheading(head)
        for x in range(5):
            burst2.color(random.choice(colors))
            burst2.forward(random.randint(2, 5))
            burst2.up()
            burst2.forward(random.randint(2, 10))
            burst2.down()
            head = head + 15
            turtle.update()
        

#reset
while True:
    win.bgcolor("black")
    building()
    l = [small_burst, burst, burstcool]
    
    for i in range(5):
        base()
        random.choice(l)()
        
    turtle.clearscreen()