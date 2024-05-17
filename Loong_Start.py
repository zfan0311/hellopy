from hellopy import *
from random import randint
window.set_size(800, 600)
# 引入：编程 - Python - 游戏制作
# 任务分析：一个游戏要包含哪些要素 - 角色 + 交互 + 机制
# 制作：1. 添加角色；2. 交互的实现； 3.机制的实现。
lichen = Loong()
longzhu = Ball()

def Loop():
    window.bg_color("lightblue")

    lichen.head_to(mouse)

    if lichen.collide(longzhu):
        # 复杂
        longzhu.x = randint(0, 800)
        longzhu.y = randint(0, 600)
        # 简单
        # longzhu.reset()
        lichen.length += 1

    lichen.draw()
    longzhu.draw()
    

run(Loop)
