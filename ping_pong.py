import turtle

wn=turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#Score
score_a=0
score_b=0

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
#ball.shapesize(stretch_wid=5,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.5 #d= delta which mean change in x coordinate
ball.dy=0.5

#Pen
pen=turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.clear()
pen.write("Player A: 0 Player B: 0  Win by 5 Points! ",align="center",font=("Courier",24))

#Winner board
win=turtle.Turtle()
win.speed()
win.color("Green")
win.penup()
win.hideturtle()
win.goto(0,0)
win.clear()



#functions

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)



#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")






#main
while True:
    wn.update()
    
    #move ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Border checking

    #   top border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    #   bottom border
        
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1

    #   right border
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24))

    #   left border
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24))

    # Declaring Winners
    if(score_a==5):
        win.write("Player A Wins by {}".format(score_a),align="center",font=("Courier",24))
        
        score_a=0
        score_b=0
        break
        

    if(score_b==5):
        win.write("Player B Wins by {}".format(score_b),align="center",font=("Courier",24))
       
        score_a=0
        score_b=0
        break
        
        
    # Paddle collides

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1





        
