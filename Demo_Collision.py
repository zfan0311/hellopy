
from hellopy import *
window.set_size(600,600)
window.set_title("鼠标点击物体测试")

player = Sprite(300,300,100,100)
player.set_scale(1)
circle = Circle(400,400,100,"red")
rc = Rectangle(100,100,60,90,"yellow")
pl = Polygon([(200,100),(200,200),(150,300)],"blue")
player.show_outline = True
def Loop():
    window.clear()
    player.draw()
    circle.draw()
    rc.draw()
    pl.draw()
    if player.on_click():
        circle.color = "green"
    if circle.on_click():
        rc.color = "pink"
    if rc.on_click():
        player.src="https://pic.imgdb.cn/item/65d01dad9f345e8d03984642.png"
    if pl.on_click():
        pl.color = circle.color
run(Loop)