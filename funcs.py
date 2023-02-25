import requests

FONT = ('Tahoma', 12, 'normal')

def get_iss_loc():
    global lat, lon
    data = requests.get("http://api.open-notify.org/iss-now.json")
    loc = data.json()
    lat = float(loc["iss_position"]["latitude"])
    lon = float(loc["iss_position"]["longitude"])
    return lat,lon
    
def move_iss_on_map(name):
    lat,lon = get_iss_loc() 
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

