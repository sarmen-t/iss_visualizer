from funcs import make_screen, iss_hist
import tkinter as tk

def live():
    window.destroy()
    make_screen()
    
def hist():
    window.destroy()
    iss_hist()
    
window = tk.Tk()
label = tk.Label(text="Would you like to view historic data or live ISS tracker?").pack()
hist = tk.Button(text="Historic Data", command=hist).pack()
live = tk.Button(text="Live ISS tracker", command=live).pack()

window.mainloop()


