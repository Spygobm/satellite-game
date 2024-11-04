import pgzrun 
import random 

HEIGHT = 600
WIDTH = 800

satellites = []
number_of_satellites = 10
next_satellite = 0

def creating_satellites():
    global satellites
    for i in range (number_of_satellites):
        satellite = Actor("satillite")
        satellite.pos = (random.randint(20,WIDTH - 20),random.randint(20,HEIGHT - 20))
        satellites.append(satellite)



def draw():
    screen.clear()
    screen.blit("backround",(0,0))
    for item in satellites:
        item.draw()

creating_satellites()

pgzrun.go()