from hellopy import *
from random import randint
window.set_size(800, 600)
# 引入：编程 - Python - 游戏制作
# 任务分析：一个游戏要包含哪些要素 - 角色 + 交互 + 机制
# 制作：1. 添加角色；2. 交互的实现； 3.机制的实现。
a = Loong()
ball = Ball()

def Loop():
    window.bg_color("lightblue")
    if a.collide(ball):
        # 简单版：直接调用reset方法
        ball.reset()
        # 进阶版：使用随机数
##        ball.x = randint(0, 800)
##        ball.y = randint(0, 600)
        a.length += 1
        a.score += 1
    a.head_to(mouse)
    ball.draw()
    a.draw()

run(Loop)
