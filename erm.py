import tkinter as tk
from PIL import Image, ImageTk
import winsound as wn
import time
import webbrowser as wb
import random as rnd

root = tk.Tk()

#images used for the random goat button.
goatrndr1 = Image.open("goat1.jpg")
goatrnd1 = ImageTk.PhotoImage(goatrndr1)
goatrndr2 = Image.open("goat2.jpeg")
goatrnd2 = ImageTk.PhotoImage(goatrndr2)
goatrndr3 = Image.open("goat3.jpg")
goatrnd3 = ImageTk.PhotoImage(goatrndr3)

#function that chooses a random image from a list of the various images
def randomimg():
    global randomGoat
    randomGoat = randomGoat = rnd.choice([goatrnd1, goatrnd2, goatrnd3])
#function that makes a new window that chooses a new image of the goats
def goatrandom():
    global randomWindow
    global lrando
    randomimg()
    randomWindow = tk.Toplevel()
    lrando = tk.Label(randomWindow, image=randomGoat)
    lrando.pack()
    randomWindow.configure(bg = "gray6")

#functions for buttons, opens a wiki and plays sound
def goatsnd():
    wn.PlaySound('goat.wav', wn.SND_ASYNC)
    time.sleep(1)

def goatwiki():
    wb.open("https://en.wikipedia.org/wiki/Goat")


#version for goatware, used for title and window title
version = "goatware V1.3.1"



#image of goat used in home screen
imager = Image.open("goated.jpeg")
resized_im = imager.resize((round(imager.size[0]*0.1), round(imager.size[1]*0.1)))
test = ImageTk.PhotoImage(resized_im)
label1 = tk.Label(image=test)

#images use for goat sound button
gtbttn = Image.open("buttonreal.png")
gtbttnr = gtbttn.resize((round(gtbttn.size[0]*0.3), round(gtbttn.size[1]*0.3)))
gbtn = ImageTk.PhotoImage(gtbttnr)


#configures main window
root.title(version)
root.configure(width = 1000, height = 1000)
root.configure(bg = "gray6")

l = tk.Label(root, text = version, fg = "white", bg = "gray6")
l.config(font =("Courier", 14))


#various labels used in the window and places them
l5 = tk.Label(root, text = "Goat Facts", bg = "gray6", fg = "white", font = ("courier", 25))
l2 = tk.Label(root, text = "Goatware, the most sophisticated goat client", fg = "white", bg = "gray6", font = "courier")
l3 = tk.Label(root, text = "A goat is a two, hollowed horned animal from Eastern Europe", fg = "white", bg = "gray6", font = "courier")
l4 = tk.Label(root, text = "and Soutwestern Asia", fg = "white", bg = "gray6", font = "courier")
l6 = tk.Label(root, text = "Goats produce milk and are used for various dairy products", fg = "white", bg = "gray6", font = "courier")


l.place(x=1, y=1)
l5.place(x=1, y= 240)
l4.place(x=1, y= 320)
l3.place(x=1, y= 300)
l2.place(x=1, y= 30)
l6.place(x=1, y=360)


#various buttons and places them
b1 = tk.Button(root, image = gbtn, command = goatsnd, bg = "gray6")
b2 = tk.Button(root, text="Goat Wiki!!!", command = goatwiki)
b3 = tk.Button(root, text="random goat image", command = goatrandom)


b3.place(x= 300, y= 250)
b2.place(x=220, y=250)
b1.place(x=685, y=400)
label1.place(x=600, y=25)
root.mainloop()