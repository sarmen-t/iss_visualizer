from turtle import *

screen = Screen()
screen.setup(1600,800)
screen.bgpic("map.gif")
setworldcoordinates(-180,-90,180,90)
screen.title("ISS Location Tracker")
screen.tracer(0)

iss_img = 'iss.gif'
screen.register_shape(iss_img)
iss = Turtle(shape=iss_img)
iss.penup()
iss.pensize(1)
iss.color("red")
iss.speed(0)

lat_lab = Turtle()
lon_lab = Turtle()