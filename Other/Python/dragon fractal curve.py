
from turtle import *
def flip_list(lst):
    newlst = []
    for element in lst:
        if element == "right":
            newlst = ["left"] + newlst
        else:
            newlst = ["right"] + newlst
    return newlst

def drag2(depth):
    path = ["right"]
    for i in range(depth):
        path = path + ["right"] + flip_list(path[:])
    return path

def dragon(length, depth):
    reset()
    left(90)
    path = drag2(depth)
    forward(length / len(path))
    for i in path:
        if i == "right":
            right(90)
        else:
            left(90)
        forward(length / len(path))
