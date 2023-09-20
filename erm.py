import tkinter as tk
from PIL import Image, ImageTk
import winsound as wn
import time
import webbrowser as wb

def goatsnd():
    wn.PlaySound('goat.wav', wn.SND_ASYNC)
    time.sleep(1)
def goatwiki():
    wb.open("https://en.wikipedia.org/wiki/Goat")

version = "goatware V1.2"
root = tk.Tk()
imager = Image.open("goated.jpeg")
resized_im = imager.resize((round(imager.size[0]*0.1), round(imager.size[1]*0.1)))
gtbttn = Image.open("buttonreal.png")
gtbttnr = gtbttn.resize((round(gtbttn.size[0]*0.3), round(gtbttn.size[1]*0.3)))
gbtn = ImageTk.PhotoImage(gtbttnr)
root.title(version)
root.configure(width = 1000, height = 1000)
root.configure(bg = "gray6")
test = ImageTk.PhotoImage(resized_im)
label1 = tk.Label(image=test)

l5 = tk.Label(root, text = "Goat Facts", bg = "gray6", fg = "white", font = ("courier", 25))
l = tk.Label(root, text = version, fg = "white", bg = "gray6")
l2 = tk.Label(root, text = "Goatware, the most sophisticated goat client", fg = "white", bg = "gray6", font = "courier")
l3 = tk.Label(root, text = "A goat is a two, hollowed horned animal from Eastern Europe", fg = "white", bg = "gray6", font = "courier")
l4 = tk.Label(root, text = "and Soutwestern Asia", fg = "white", bg = "gray6", font = "courier")
l6 = tk.Label(root, text = "Goats produce milk and are used for various dairy products", fg = "white", bg = "gray6", font = "courier")
l.config(font =("Courier", 14))
l.place(x=1, y=1)
l5.place(x=1, y= 240)
l4.place(x=1, y= 320)
l3.place(x=1, y= 300)
l2.place(x=1, y= 30)
l6.place(x=1, y=360)
b1 = tk.Button(root, image = gbtn, command = goatsnd, bg = "gray6")
b2 = tk.Button(root, text="Goat Wiki!!!", command = goatwiki)
b2.place(x=220, y=250)
b1.place(x=685, y=400)
label1.place(x=600, y=25)
root.mainloop()