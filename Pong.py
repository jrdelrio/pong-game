# Pong básico



import turtle
import os

win = turtle.Screen()
win.title('Pong by @Rai')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(10)

# Score

score_a = 0
score_b = 0

# Paddle A()
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(10)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # cuando la pelota se mueve se mueve 2 pixeles en el eje x
ball.dy = 2 # cuando la pelota se mueve se mueve 2 pixeles en el eje y

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: {}     Player B: {}'.format(score_a,score_b), align = "center", font = ('Courier', 24, 'normal'))

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,'s')
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,'Down')

# Para salir del juego
quit = False

def quit_game():
	quit = True

win.onkeypress(quit_game, 'Right')

# main loop
while quit == False:
	win.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Borders checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		os.system('afplay bounce.wav&') # en linux es 'aplay' # el & evita el delay

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		os.system('afplay bounce.wav&')

	if ball.xcor() > 390:
		ball.goto(0, 0)
		score_a += 1
		ball.dx *= -1
		pen.clear()
		pen.write('Player A: {}     Player B: {}'.format(score_a, score_b), align = "center", font = ('Courier', 24, 'normal'))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		score_b += 1
		ball.dx *= -1
		pen.clear()
		pen.write('Player A: {}     Player B: {}'.format(score_a, score_b), align = "center", font = ('Courier', 24, 'normal'))

	# Paddle and ball collisions
	if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
		os.system('afplay bounce.wav&')

	if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		os.system('afplay bounce.wav&')









