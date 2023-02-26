import requests
from iss_shape import screen, iss, lat_lab, lon_lab
import time
from datetime import datetime
import sqlite3

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
        