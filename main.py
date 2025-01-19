import pgzrun
from random import randint
from time import time


WIDTH = 800
HEIGHT = 600
TITLE="Satellite Connect"

start_time=0
total_time=0
num_satellites=10
current_satellite=0

satellites=[]
lines=[]

def create_satellites():
    global start_time
    for i in range(num_satellites):
        satellite=Actor("satellite")
        satellite.pos = randint(50,750),randint(50,550)
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
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if current_satellite<num_satellites:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=40)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=40)

def update():
    pass

def on_mouse_down(pos):
    global current_satellite, lines
    if current_satellite<num_satellites:
        if satellites[current_satellite].collidepoint(pos):
            if current_satellite:
                lines.append(
                    (
                        satellites[current_satellite-1].pos,
                        satellites[current_satellite].pos
                    )
                )
            current_satellite = current_satellite + 1
        else:
            lines = []
            current_satellite=0

create_satellites()

pgzrun.go()





