import turtle
from pygame import mixer
import time

mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("MusicTest.mp3")
mixer.music.play()

count = 5

while count > 0:
    screen = turtle.Screen()

    screen.bgcolor('#000')
    screen.title("Happy new year 2024")
    screen.screensize(800,800)

   # mixer.music.play()


    firework = turtle.Turtle()
    firework.pensize(3)
    firework.shape('turtle')
    size = 20
    firework.stamp
    firework.speed(11)
    firework.left(90)

    firework.color("#EA2027")
    for step in range(40):
        firework.forward(100)
        firework.left(180)
        firework.forward(100)
        firework.left(9)

    firework.color('#EE5A2A')
    for step in range(36):
        firework.forward(130)
        firework.left(180)
        firework.forward(130)
        firework.left(10)

    firework.color('#F79F1F')
    for step in range(20):
        firework.forward(150)
        firework.left(180)
        firework.forward(150)
        firework.left(18)

    firework.color('#3ae374')
    for stamps in range(12):
        firework.penup()
        firework.forward(170)
        firework.pendown()
        firework.forward(10)
        firework.penup()
        firework.forward(10)
        firework.stamp()
        firework.right(30)
        firework.penup()
        firework.setpos(0,0)


    text = turtle.Turtle()
    text.color("#fff")
    text.penup()
    text.setpos(0,-240)
    text.write("Happy New Year 2024 Mi Amor", True, align="center", font=("Monsterrat", 20, "normal"))
    text.setpos(0,-260)

   # screen.mainloop()

    count -= 1
    time.sleep(1.4)
    screen.clear()


# Code modified by Phil
# Inspired from:
# [Python Program To Wish Happy New Year](https://pythondex.com/python-program-to-wish-happy-new-year)
# Musique : Count on me - Bruno Mars

# [The best way to install pygame is with the pip tool](https://www.pygame.org/wiki/GettingStarted)