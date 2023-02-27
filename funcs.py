import requests
import time
from datetime import datetime
import sqlite3
from turtle import *

FONT = ('Tahoma', 12, 'normal')

data = sqlite3.connect("iss_loc.db")
cur = data.cursor()

def get_iss_loc():
    global lat, lon
    data = requests.get("http://api.open-notify.org/iss-now.json")
    loc = data.json()
    lat = float(loc["iss_position"]["latitude"])
    lon = float(loc["iss_position"]["longitude"])
    loc_time = datetime.fromtimestamp(loc["timestamp"])
    return lat, lon, loc_time
    
def move_iss_on_map(name):
    lat, lon, loc_time = get_iss_loc() 
    name.goto(lon,lat)
    name.pendown()

def draw_lat_lon_on_map(lat_label, lon_label):
    lat_label.clear()
    lon_label.clear()
    lat_label.penup()
    lon_label.penup()
    lat_label.hideturtle()
    lon_label.hideturtle()
    lat_label.goto(-175,-66)
    lon_label.goto(-175,-71)
    lat_label.write(f"The latitude is: {lat}", font=FONT)
    lon_label.write(f"The longitude is: {lon}", font=FONT)

def make_screen():
    global screen, iss, lat_lab, lon_lab
    screen, iss, lat_lab, lon_lab = screen_make()
    iss_tracker()

def screen_make():
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
    
    return screen, iss, lat_lab, lon_lab

def iss_tracker():
    keep_running = True
    while keep_running:
        move_iss_on_map(iss)
        draw_lat_lon_on_map(lat_lab, lon_lab)
        screen.update()
        time.sleep(5)
        iss.pendown()
        db_lat, db_lon, db_loc_time = get_iss_loc()
        cur.execute("INSERT into iss_loc_data VALUES(?, ?, ?)", (db_lat, db_lon, db_loc_time))
        data.commit()

def iss_hist():
    screen = Screen()
    screen.setup(1600,800)
    screen.bgpic("map.gif")
    setworldcoordinates(-180,-90,180,90)
    screen.title("Historic ISS Location Data Points")
    screen.tracer(0)
    screen.update()
    hist_data = cur.execute("SELECT * FROM iss_loc_data")
    hist_list = hist_data.fetchall()
    iss_dot = Turtle()
    iss_dot.penup()
    iss_dot.color("red")
    iss_dot.width("2")
    iss_dot.goto(-175,78)
    iss_dot.pendown()
    iss_dot.goto(-170,78)
    iss_dot.penup()
    iss_dot.goto(-168,75)
    iss_dot.write("ISS Trajectory", font=('Tahoma', 16, 'bold'))
    for x in hist_list:
        iss_dot.goto(x[1],x[0])
        iss_dot.dot(3, "red")