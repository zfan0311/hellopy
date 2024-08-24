
from hellopy import *
window.set_size(600,600)
window.set_title("碰撞测试")

player = Sprite(300,300,100,100)
player.set_scale(0.5)

player.show_outline = True
def Loop():
    window.clear()

    player.draw()
    player.src = "https://pic.imgdb.cn/item/65d01dad9f345e8d03984642.png"

run(Loop)