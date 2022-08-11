import turtle
import time
import random
turtle.bgcolor('black')
turtle.title('Turtle race')

# Finish line
meta = turtle.Turtle()
meta.color('white')
meta.penup()
meta.goto(-50,220)
meta.write("Finish line", font=("Arial", 15, "bold"))

meta.penup()
meta.goto(-400,200)
meta.pendown()
meta.goto(400,200)
meta.hideturtle()

# Players
green = turtle.Turtle()
green.shape('turtle')
green.color('green')
green.pensize(2)
green.penup()
green.goto(-300,-200)
green.left(90)
green.pendown()

blue = turtle.Turtle()
blue.shape('turtle')
blue.color('blue')
blue.pensize(2)
blue.penup()
blue.goto(-200,-200)
blue.left(90)
blue.pendown()

yellow = turtle.Turtle()
yellow.shape('turtle')
yellow.color('yellow')
yellow.pensize(2)
yellow.penup()
yellow.goto(-100,-200)
yellow.left(90)
yellow.pendown()

red = turtle.Turtle()
red.shape('turtle')
red.color('red')
red.pensize(2)
red.penup()
red.goto(0,-200)
red.left(90)
red.pendown()

orange = turtle.Turtle()
orange.shape('turtle')
orange.color('orange')
orange.pensize(2)
orange.penup()
orange.goto(100,-200)
orange.left(90)
orange.pendown()

pink = turtle.Turtle()
pink.shape('turtle')
pink.color('pink')
pink.pensize(2)
pink.penup()
pink.goto(200,-200)
pink.left(90)
pink.pendown()

white = turtle.Turtle()
white.shape('turtle')
white.color('white')
white.pensize(2)
white.penup()
white.goto(300,-200)
white.left(90)
white.pendown()

# Counting down

odliczanie = turtle.Turtle()
odliczanie.color('white')
odliczanie.penup()
odliczanie.goto(-300,270)
odliczanie.hideturtle()

for x in range(3):
    odliczanie.write(3-x, font=("Arial", 40, 'bold'))
    time.sleep(1)
    odliczanie.clear()

# Which turtle win

def sprawdz():

    if green.position()[1] >= 200:
        odliczanie.clear()
        odliczanie.color('green')
        odliczanie.write('Green turtle won !!', font=("Arial", 20, 'bold'))
        return True

    if blue.position()[1] >= 200:
        odliczanie.clear()
        odliczanie.color('blue')
        odliczanie.write('Blue turtle won !!', font=("Arial", 20, 'bold'))
        return True

    if yellow.position()[1] >= 200:
        odliczanie.clear()
        odliczanie.color('yellow')
        odliczanie.write('Yellow turtle won !!', font=("Arial", 20, 'bold'))
        return True

    if red.position()[1] >= 200:
        odliczanie.clear()
        odliczanie.color('red')
        odliczanie.write('Red turtle won !!', font=("Arial", 20, 'bold'))
        return True

    if orange.position()[1] >= 200:
        odliczanie.clear()
        odliczanie.color('orange')
        odliczanie.write('Orange turtle won !!', font=("Arial", 20, 'bold'))
        return True

    if pink.position()[1] >= 200:
        odliczanie.clear()
        odliczanie.color('pink')
        odliczanie.write('Pink turtle won !!', font=("Arial", 20, 'bold'))
        return True

    if white.position()[1] >= 200:
        odliczanie.clear()
        odliczanie.color('white')
        odliczanie.write('White turtle won !!', font=("Arial", 20, 'bold'))
        return True

    return False

# Main loop

first = random.choice(['green','blue','yellow','red','orange','pink'])

while True:

    if first == 'green':
        green.forward(random.randint(0,40))
        if sprawdz(): break
        blue.forward(random.randint(0,70))
        if sprawdz(): break
        yellow.forward(random.randint(0, 70))
        if sprawdz(): break
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        pink.forward(random.randint(0, 70))
        if sprawdz(): break
        orange.forward(random.randint(0, 70))
        if sprawdz(): break
        white.forward(random.randint(0, 70))
        if sprawdz(): break

    if first == 'blue':
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
        green.forward(random.randint(0, 70))
        if sprawdz(): break
        yellow.forward(random.randint(0, 70))
        if sprawdz(): break
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        pink.forward(random.randint(0, 70))
        if sprawdz(): break
        orange.forward(random.randint(0, 70))
        if sprawdz(): break
        white.forward(random.randint(0, 70))
        if sprawdz(): break

    if first == 'yellow':
        yellow.forward(random.randint(0, 70))
        if sprawdz(): break
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
        green.forward(random.randint(0, 70))
        if sprawdz(): break
        pink.forward(random.randint(0, 70))
        if sprawdz(): break
        orange.forward(random.randint(0, 70))
        if sprawdz(): break
        white.forward(random.randint(0, 70))
        if sprawdz(): break

    if first == 'red':
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        yellow.forward(random.randint(0, 70))
        if sprawdz(): break
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
        green.forward(random.randint(0, 70))
        if sprawdz(): break
        pink.forward(random.randint(0, 70))
        if sprawdz(): break
        orange.forward(random.randint(0, 70))
        if sprawdz(): break
        white.forward(random.randint(0, 70))
        if sprawdz(): break

    if first == 'orange':
        orange.forward(random.randint(0, 70))
        if sprawdz(): break
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        yellow.forward(random.randint(0, 70))
        if sprawdz(): break
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
        green.forward(random.randint(0, 70))
        if sprawdz(): break
        pink.forward(random.randint(0, 70))
        if sprawdz(): break
        white.forward(random.randint(0, 70))
        if sprawdz(): break


    if first == 'pink':
        pink.forward(random.randint(0, 70))
        if sprawdz(): break
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        yellow.forward(random.randint(0, 70))
        if sprawdz(): break
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
        green.forward(random.randint(0, 70))
        if sprawdz(): break
        orange.forward(random.randint(0, 70))
        if sprawdz(): break
        white.forward(random.randint(0, 70))
        if sprawdz(): break

    if first == 'white':
        white.forward(random.randint(0, 70))
        if sprawdz(): break
        pink.forward(random.randint(0, 70))
        if sprawdz(): break
        red.forward(random.randint(0, 70))
        if sprawdz(): break
        yellow.forward(random.randint(0, 70))
        if sprawdz(): break
        blue.forward(random.randint(0, 70))
        if sprawdz(): break
        green.forward(random.randint(0, 70))
        if sprawdz(): break
        orange.forward(random.randint(0, 70))
        if sprawdz(): break



    time.sleep(0.3)



turtle.exitonclick()



