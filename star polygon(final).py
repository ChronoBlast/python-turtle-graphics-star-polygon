import turtle
import math

#this function creates a button and returns its bottom-left and top-right angle coordinates
def make_button(x, y, name):
  screen.tracer(0, 0)
  name = str(name)
  turtle_1 = turtle.Turtle()
  turtle_1.ht()
  turtle_1.penup()
  turtle_1.goto(x, y)
  turtle_1.pendown()
  turtle_1.color("yellow")
  turtle_1.fillcolor("cyan")
  turtle_1.pensize(5)
  turtle_1.begin_fill()

  for i in range(2):
    turtle_1.forward(200)
    turtle_1.left(90)
    turtle_1.forward(100)
    turtle_1.left(90)
  turtle_1.end_fill()
  turtle_1.penup()
  turtle_1.goto(x + 100, y + 40)
  turtle_1.write(name, align="center", font=("Arial", 15, "normal"))
  screen.tracer(1, 10)

  return ((x, y), (x + 200, y + 100))

#makes smaller button
def make_up_button(x, y, name):
  screen.tracer(0, 0)
  name = str(name)
  turtle_2 = turtle.Turtle()
  turtle_2.ht()
  turtle_2.penup()
  turtle_2.goto(x, y)
  turtle_2.pendown()
  turtle_2.color("yellow")
  turtle_2.fillcolor("cyan")
  turtle_2.pensize(5)
  turtle_2.begin_fill()

  for i in range(2):
    turtle_2.forward(100)
    turtle_2.left(90)
    turtle_2.forward(40)
    turtle_2.left(90)
  turtle_2.end_fill()
  turtle_2.penup()
  turtle_2.goto(x + 50, y + 10)
  turtle_2.write(name, align="center", font=("Arial", 15, "normal"))
  screen.tracer(1, 10)

  return ((x, y), (x + 100, y + 40))


#this function checks if click coordinates are within button coordinates
def check_button(x, y, button_coord):
  return (x > button_coord[0][0] and x < button_coord[1][0]) and (y > button_coord[0][1] and y < button_coord[1][1])
  

#this function is called on mouse click, determines whether a button was clicked and what action to take
def action(x, y):
  global polygon_size
  global n
  global step
  global turtle_3
  global show
  screen.tracer(0, 0)
  turtle_3.reset()
  turtle_3.penup()
  turtle_3.ht()
  turtle_3.goto(-260, -400)
  turtle_3.write(f"star density: {step}", font=("Arial", 15, "normal"))
  turtle_3.goto(-260, -360)
  turtle_3.write(f"number of sides: {n}", font=("Arial", 15, "normal"))
  turtle_3.goto(-260, -320)
  turtle_3.write(f"polygon size: {polygon_size}", font=("Arial", 15, "normal"))
  screen.tracer(1, 10)
  if check_button(x, y, button_dict["polygon_size"]):
    polygon_size = int(turtle.numinput("polygon size", "can't be negative", default = 200, minval = 10, maxval = 400))
  elif check_button(x, y, button_dict["number_of_sides"]):
    n = int(turtle.numinput("number of sides", "at least 3", default = 5, minval = 3, maxval = 100))
  elif check_button(x, y, button_dict["density"]):
    step = int(turtle.numinput("star density", "greater than zero and less than number of sides", default = 3, minval = 1, maxval = n))    #LIMIT BY THE NUMBER OF SIDES
  elif check_button(x, y, button_dict["draw"]):
    print(polygon_size, n, step)
    draw_star_polygon()
  elif check_button(x, y, button_dict["show"]):
    if show == 0:
      show = 1
    else:
      show = 0


    
def pol_center(number_of_sides, pol_size, x, y):
  radians = math.radians(180 / number_of_sides)    #convert (180 / n) degrees to radians
  inradius = pol_size * math.cos(radians)    #radius of incircle
  side_len = inradius * 2 * math.tan(radians)    #side length
  x -= side_len / 2
  y -= inradius 
  return [inradius, side_len, x, y]

def draw_star_polygon():
  global polygon_size
  global n
  global step
  global show
  
  #turn angle
  turn = 360 / n

  global dude
  dude.reset()
  dude.ht()


  f = pol_center(n, polygon_size, 0, 0)

  #inscribed circle radius
  inradius = f[0]    

  #side length
  side_length = f[1]

  #starting point
  x = f[2]
  y = f[3]

  #move the turtle to starting point
  dude.penup()
  dude.goto(x, y)
  dude.pendown()
  screen.tracer(1, 0)

  if show == 0:
    dude.penup()
  #draw a polygon and record coordinates of the list_of_vertices
  list_of_vertices = []
  for i in range(n):
    list_of_vertices.append(dude.pos())
    dude.forward(side_length)
    dude.left(turn)

  dude.pendown()
  #draw a star polygon
  starting_index = step
  while True:
    dude.goto(list_of_vertices[starting_index])
    starting_index += step
    if starting_index >= len(list_of_vertices):
        starting_index -= n
          
          
          
    if ((x - dude.pos()[0])**2 + (y - dude.pos()[1])**2)**0.5 < 1:
        break




screen = turtle.Screen()

#create buttons and write their positions
button_dict = {}
button_dict["polygon_size"] = make_button(-470, 300, "polygon size")

button_dict["number_of_sides"] = make_button(-100, 300, "number of sides")

button_dict["density"] = make_button(270, 300, "density")

button_dict["button_4"] = make_up_button(-260, 360, "more")

button_dict["button_5"] = make_up_button(-260, 300, "less")

button_dict["button_6"] = make_up_button(110, 360, "more")

button_dict["button_7"] = make_up_button(110, 300, "less")

button_dict["button_8"] = make_up_button(480, 360, "more")

button_dict["button_9"] = make_up_button(480, 300, "less")

button_dict["draw"] = make_button(-470, -400, "draw")

button_dict["show"] = make_button(270, -400, "show/hide polygon")

make_up_button(110, -400, "upd values")

#TODO make an option to show or hide the polygon (only show the star)

#polygon size, number of sides and star density
polygon_size = 200
n = 5
step = 3
show = 0

dude = turtle.Turtle()
dude.ht()

turtle_3 = turtle.Turtle()
turtle_3.ht()
screen.onclick(action)





screen.mainloop()
