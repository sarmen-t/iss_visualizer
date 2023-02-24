import requests, time
from turtle import *

FONT = ('Tahome', 12, 'normal')

screen = Screen()
screen.setup(1600,800)
screen.bgpic("map.gif")
setworldcoordinates(-180,-90,180,90)
screen.title("ISS Location Tracker")
screen.tracer(0)

iss = Turtle()
iss.penup()
iss.shape("circle")
iss.shapesize(0.3,0.3)
iss.pensize(3)
iss.color("red")
iss.speed(0)

lat_lab = Turtle()
lon_lab = Turtle()

def get_iss_loc():
    global lat, lon
    data = requests.get("http://api.open-notify.org/iss-now.json")
    loc = data.json()
    lat = float(loc["iss_position"]["latitude"])
    lon = float(loc["iss_position"]["longitude"])
    return lat,lon
    
def move_iss_on_map():
    lat,lon = get_iss_loc() 
    iss.goto(lon,lat)
    iss.pendown()

def draw_lat_lon_on_map():
    lat_lab.clear()
    lon_lab.clear()
    lat_lab.penup()
    lon_lab.penup()
    lat_lab.hideturtle()
    lon_lab.hideturtle()
    lat_lab.goto(-175,-66)
    lon_lab.goto(-175,-71)
    lat_lab.write(f"The latitude is: {lat}", font=FONT)
    lon_lab.write(f"The longitude is: {lon}", font=FONT)

keep_running = True
while keep_running:
    move_iss_on_map()
    draw_lat_lon_on_map()
    screen.update()
    time.sleep(5)

screen.mainloop()

