from hellopy import *
from random import randint
window.set_size(800,500)
ball = Circle(400,250,10,"white")
p1 = Rectangle(20,250,10,100,"white")
p2 = Rectangle(780,250,10,100,"white")
ball.state = 1 # 0:运动中，1:p1发球，2:p2发球
ball.vx = 0
ball.vy = 0
while True:
    if Key("K_w").pressed():
        p1.y -= 5
    if Key("K_s").pressed():
        p1.y += 5
    if Key("K_UP").pressed():
        p2.y -= 5
    if Key("K_DOWN").pressed():
        p2.y += 5
    if ball.state == 0:
        ball.x += ball.vx
        ball.y += ball.vy
        if ball.y < 5:
            ball.vy = -ball.vy
        if ball.y > 495:
            ball.vy = -ball.vy
        if ball.collide(p1):
            ball.vx = 5
            ball.vy += randint(-2,2)
        if ball.collide(p2):
            ball.vx = -5
            ball.vy += randint(-2,2)
    elif ball.state == 1:
        ball.x = 35
        ball.y = p1.y
        if Key("K_SPACE").pressed():
            ball.vx = 5
            ball.vy = randint(-5,5)
            ball.state = 0
    elif ball.state == 2:
        ball.x = 755
        ball.y = p2.y
        if Key("K_SPACE").pressed():
            ball.vx = -5
            ball.vy = randint(-5,5)
            ball.state = 0
    window.clear()
    ball.draw()
    p1.draw()
    p2.draw()
    window.show(20)