# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle
    global food
    global cume
    size(800, 600)
    cume = 0
    velocity = PVector(0, 0)
    velocity2 =  PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(random(width),random(height), velocity2)
    food.update(random(width),random(height))   

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    vehicle.seek(food.position)
    vehicle.update()
    vehicle.display()
    food.display()
    nearby = vehicle.bucho_update(food.position)  
    if nearby == 1:
        food.update(random(width),random(height))
