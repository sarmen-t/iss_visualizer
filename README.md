# ISS Location Visualizer
## Video Demo:  https://www.youtube.com/watch?v=eiT1yZXILGA
## Description:

Basic Python Turtle graphics applet to visualize location of ISS

When launching applet, you get to choose between two functions:

The first is to draw historic ISS data onto a world map. When selecting
this option, a world map screen is drawn with a red line denoting the 
ISS location over time. The data that is used for this visual representation
comes from a sql database file within the project directory. The database is 
populated from previous runs of the live tracker program.

The second option draws the live ISS location over a world map. The function
calls onto an ISS location API and returns Latitude, longitude, and a time 
stamp for the current ISS location. The function then draws the ISS as a clip
art gif at the live location, labels and lists the latitude and longitude and
begins to draw a red line showing the ISS's movement over time.

Refresh rate of the ISS is set at once per 5 seconds, which is recommended by 
ISS API. As previously mentioned, the data from API is saved to sql database, 
which can then be accessed from the historic data function.