import tkinter as tk
from PIL import Image, ImageTk
import winsound as wn
import time

def goatsnd():
    wn.PlaySound('goat.wav', wn.SND_ASYNC)
    time.sleep(1)

version = "goatware V1.1"
root = tk.Tk()
imager = Image.open("goated.jpeg")
resized_im = imager.resize((round(imager.size[0]*0.1), round(imager.size[1]*0.1)))


root.title(version)
root.configure(width = 1000, height = 1000)
root.configure(bg = "gray6")
test = ImageTk.PhotoImage(resized_im)
label1 = tk.Label(image=test)

l = tk.Label(root, text = version, fg = "white", bg = "gray6")
l2 = tk.Label(root, text = "The goat is a two, hollowed horned animal from Southwestern", fg = "white", bg = "gray6", font = "courier")
l3 = tk.Label(root, text = "Asia and Eastern Europe.", fg = "white", bg = "gray6", font = "courier")
l.config(font =("Courier", 14))
l.place(x=1, y=1)

l3.place(x=1, y=50)
l2.place(x=1, y= 30)
b1 = tk.Button(root, text = "What a goat sounds like", command = goatsnd)
b1.place(x=600, y=400)
label1.place(x=600, y=25)
root.mainloop()