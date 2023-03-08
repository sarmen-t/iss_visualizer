# ISS Location Visualizer
## Video Demo:  https://www.youtube.com/watch?v=eiT1yZXILGA
## Description:

## Basic Python Turtle graphics applet to visualize location of International Space Station

When launching applet, a TkInter window is created which asks you via
two buttons to choose between two functions: Historic Data and Live ISS 
tracking. When selecting one of the buttons, the window then closes and 
the function of the buttons is called. The functions are described below.

## Historic Data
The first is to draw historic ISS data onto a world map. We do this by creating
a turtle window which uses a world map as the backtground image with latitude
and longitude axis lines. The function then imports data from a sql database file.
The file contains latitude, longitude, and timestamps for ISS location positions. 
The file is populated by data from previous runs of the second function 
(Live ISS tracking). This data is then drawn onto the world map as a red line to 
create a visual representation of the ISS orbital path. There is also a key drawn
in the top left corner to clarify what you are looking at.

## Live ISS Tracker
When selecting the second option, similar to the first option, a turtle window is
created with a world map as the background. The function calls onto an ISS location
API and returns Latitude, longitude, and a time stamp for the current ISS location.
The function then draws the ISS as a clip art gif at the live location, labels, and 
lists the latitude and longitude and begins to draw a red line showing the ISS's 
movement over time. Refresh rate of the ISS is set at once per 5 seconds, which is 
recommended by ISS API. As previously mentioned, the data from API is saved to sql 
database, which can then be accessed from the historic data function.

My project folder contains five files, we will go over them below:

There are two image files, iss.gif and map.gif. The iss.gif file is a small clip 
art image of the ISS that is used as the "turtle" in our live tracking visualizer. 
The second image, map.gif, is a black and white world map with latitude and 
longitude axis drawn on it to help in the visualization of location.

There is a single db file which is our sql database containing previous run data
of the live ISS tracker. It contains a single table which has 3 columns: latitude,
longitude, and timestamp. As I have not run the tracker for extended periods of
time, the database file is small and does not contain many data points.

There is the funcs.py file which contains most of the functions used in our program.

The first function, get_iss_loc, is the function that calls on the ISS location API.
It retrieves the latitude, longitude, and timestamps from the API and returns those
values.

The second function, move_iss_on_map, takes the latitude and longitude numbers from 
the previous function, and moves the turtle on our turtle window to the live position
of the ISS.

The third function, draw_lat_lon_on_map, is used to draw/list the latitude and 
longitude numbers on the map as labels. This function is called every time the map
is updated, which is every five seconds.

The fourth function, make_screen, creates the screen for the live ISS tracker.
It does this by called the screen_make function, followed by the iss_tracker
function. I chose to create the screen as a function because with the user deciding
on live versus historic data, we don't want to create a screen until a decision has
been made in the first prompt.

The fifth function, screen_make, creates the turtle screen, the ISS turtle, and formats
both of them such that the ISS turtle uses the clip art gif as the pointer, and the 
screen uses the world map as the background. The label turtles are also created in this 
function, which are used to later list the latitude and longitude values on the map as
the ISS moves.

The sixth and final function, iss_hist, creates the historic ISS map. It creates a screen,
formats it to have the world map as the background, then imports the data from the sql
database file. The function loops through the database data and takes every latitude
longitude pair and draws dots on the map to show the historic location of the ISS.


