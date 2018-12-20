#made_by_sameer_kaushik
from tkinter import *
from math import cos, sin ,pi
import time
import pyglet
from pygame import mixer
root=Tk()
root.title(">   C L O C K  <")
root.resizable(0,0)
root.wm_attributes("-topmost",1)

c=Canvas(width=400, height=400, bg="black")
c.pack()

c.create_oval(10,10,390,390, fill="white",outline="#00C957",width=5)
c.create_oval(195,195,205,205, fill="black")


angle=(2*pi) + (pi/6)
for i in range(1,13):
    c.create_text(200+(sin(angle)*180), 200-(cos(angle)*180),text=int(str(i)), fill="black")
    angle=angle+(pi/6)

p=0
q=0
r=0
for i in range(15,10000,3):
    c.delete(p)
    c.delete(q)
    c.delete(r)

    t=time.localtime()

    sec=(2*pi)+((pi/30)*t[5])

    mint=(2*pi) +((pi/30)*t[4])

    h=(t[4]/60)
    hr=(2*pi)+ ((pi/6)*(h+t[3]))
    c.create_line(200+(sin(sec)*5),200-(cos(sec)*5),200+(sin(sec)*150), 200-(cos(sec)*150), fill="red")   # sec
    c.create_line(200+(sin(mint)*5), 200-(cos(mint)*5),200+(sin(mint)*120), 200-(cos(mint)*120), fill="#006400")   # minute
    c.create_line(200+(sin(hr)*5), 200-(cos(hr)*5),200+(sin(hr)*90), 200-(cos(hr)*90), fill="blue")     # hour
    time.sleep(1)
    mixer.init()
    mixer.music.load("./tik.wav")
    mixer.music.play()
    p=i
    q=i+1
    r=i+2
    root.update()
