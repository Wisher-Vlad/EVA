import math
from turtle import *

name = input("введите свое имя: ").strip().lower()
if name == "eva":

    def heart_a(n):
        return 15 * math.sin(n) ** 3
    
    def heart_b(n):
        return 12 * math.cos(n)-5 *\
            math.cos(2*n) - 2 *\
            math.cos(3*n) - \
            math.cos(4*n)
            
    speed(10)
    bgcolor("white")
    color("red")
    
    penup()
    
    for i in range(335):
        x = heart_a(i) * 15
        y = heart_b(i) * 15
        goto(x, y)
        pendown()
    hideturtle()    
    done()
else:
    print("Сердце доступно только для Евы")
