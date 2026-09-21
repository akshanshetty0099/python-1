import turtle

# ---------- Setup ----------
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Turtle Flower")

t = turtle.Turtle()
t.speed(0)  # fastest drawing speed

# ---------- Draw one petal ----------
def draw_petal(size, color):
    t.begin_fill()
    t.color(color)
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)
    t.end_fill()

# ---------- Draw the flower (ring of petals) ----------
def draw_flower(petal_count, size, color):
    angle = 360 / petal_count
    for _ in range(petal_count):
        draw_petal(size, color)
        t.left(angle)

# ---------- Draw stem ----------
def draw_stem(length):
    t.color("green")
    t.pensize(6)
    t.setheading(-90)  # point downward
    t.forward(length)

# ---------- Draw leaves ----------
def draw_leaf():
    t.begin_fill()
    t.color("green")
    t.circle(20, 90)
    t.left(90)
    t.circle(20, 90)
    t.end_fill()

# ---------- Main drawing ----------
t.penup()
t.goto(0, 100)
t.pendown()

# Petals
draw_flower(8, 60, "hotpink")

# Center of flower
t.penup()
t.goto(0, 100)
t.pendown()
t.begin_fill()
t.color("yellow")
t.circle(20)
t.end_fill()

# Stem
t.penup()
t.goto(0, 80)
t.pendown()
draw_stem(150)

# Leaves
t.penup()
t.goto(0, 20)
t.setheading(0)
t.pendown()
draw_leaf()

t.penup()
t.goto(0, -20)
t.setheading(180)
t.pendown()
draw_leaf()

# ---------- Finish ----------
t.hideturtle()
screen.mainloop()  # keeps the window open until you close it