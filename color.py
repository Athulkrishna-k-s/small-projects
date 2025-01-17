import random 
from sty import fg 

def rgb():
    red = random.randint(0,250)
    blue = random.randint(0,250)
    green  = random.randint(0,250)
    return red,blue,green 
red,blue,green =rgb()

def colour_generator(red,blue,green):
    return fg(red,blue,green )

colour=colour_generator(red,blue,green )


print(colour,'i close my eyes i can see the world is waiting uo for me that i call my home ......')

# creating a fuction to print the commandprompt in different colors 
    