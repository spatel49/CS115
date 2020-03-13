'''
Created on Oct 3, 2018

@author: sypat
'''

import turtle

def square_spiral(walls):
    def square_spiral_helper(walls, distance, inital, count):
        if walls == count:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(walls, distance + inital * (count % 2), inital, count + 1)
    square_spiral_helper(walls, 20, 20, 0)

square_spiral(30)


def oct_spiral(walls):
    def oct_spiral_helper(walls, distance, inital, count):
        if walls == count:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            oct_spiral_helper(walls, distance + inital * (count % 2), inital, count + 1)
    oct_spiral_helper(walls, 20, 5, 0)

oct_spiral(30)


