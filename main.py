import pgzrun
from random import randint
from time import time


WIDTH = 600
HEIGHT = 400
TITLE="Satellite Connect"

start_time=0
total_time=0
num_satellites=10
next_satellite=0

satellites=[]
lines=[]

def create_satellites():
    global start_time
    for i in range(num_satellites):
        satellite=Actor("satellite")
        satellite.pos = randint(50,550),randint(50,350)
        satellites.append(satellite)
    start_time=time()

def draw():
    global total_time
    screen.blit("background",(0,0))
    num = 1
    for satellite in satellites:
        screen.draw.text(str(num),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        num=num+1

create_satellites()

pgzrun.go()





