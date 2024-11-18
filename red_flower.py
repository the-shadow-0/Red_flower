from turtle import *
colors = ['red']
speed(0)

def flower():
    for i in range(190):
        pencolor(colors[i % len(colors)])
        circle(190 - i, extent=90)
        left(90)
        circle(190 - i, extent=90)
        left(18)

flower()
done()
