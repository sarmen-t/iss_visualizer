import time, funcs
from turtle import *
from iss_shape import screen, iss, lat_lab, lon_lab

keep_running = True
while keep_running:
    funcs.move_iss_on_map(iss)
    funcs.draw_lat_lon_on_map(lat_lab, lon_lab)
    screen.update()
    time.sleep(5)
    iss.pendown()

screen.mainloop()

