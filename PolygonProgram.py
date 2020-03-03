# Casandra Villagran
# 03/2/2020

#Use a polygon and convert it to a function.

import turtle
Villagran = turtle.Turtle()

length = int(input ("What is the length for the sides?"))
sides = int(input ("Number of sides in the polygon?"))

Villagran= turtle.Turtle()

#Villagran.color(str(lcolor))
#Villagran.pencolor(str(lcolor))

def drawPolygon(t,sides,length):
    
    for i in range(sides):
    #Villagran.pencolor = (str(lcolor))
    #Villagran.fillcolor = (str(fcolor))
        Villagran.forward(length)
        Villagran.left(360 / sides)

wn = turtle.Screen()
Villagran= turtle.Turtle()
Villagran.speed(5)
wn.bgcolor("lightgreen")
Villagran.pencolor("blue")

mv = -10

for s in range(length, 10*length,40):
   
  drawPolygon(Villagran,sides,s)

  Villagran.penup()
  Villagran.goto(mv,mv)
  Villagran.pendown()
  mv = mv -10
