from hellopy import *
import random

# 只需要执行一次的代码
window.set_size(480,700)
window.set_title("飞机大战")
bg = Sprite(window.w/2,window.h/2,480,700,'https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/background.png')
plane = Sprite(200,500,100,120,'https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/me1.png')
enemy = Sprite(200,100,57,43,'https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/enemy1.png')
bullet = Sprite(plane.x, plane.y, 5,11,'https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/bullet1.png')
enemy.speed = 5
bgm = Sound('https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/sound/bgm.mp3')
bgm.play()
bullet_sound = Sound('https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/sound/fireEffect.mp3')
hit_sound = Sound('https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/sound/explodeEffect.mp3')
score_text = Text("分数:", 20,20,40,"red")
plane.score = 0
# 需要重复执行的代码
def GameLoop():
    # 修改得分文字
    score_text.text = "分数: " + str(plane.score)
    # 敌机移动
    enemy.y += enemy.speed
    if enemy.y > 760:
        enemy.y = -enemy.h/2
        enemy.x = random.randint(0, 480)
        plane.speed = random.random() * 0.5
    bullet.y -= 30
    # 主角移动
    if Key("K_RIGHT").pressed():
        plane.x += 2
    if Key("K_LEFT").pressed():
        plane.x -= 2
    if Key("K_UP").pressed():
        plane.y -= 2
    if Key("K_DOWN").pressed():
        plane.y += 2
    # 子弹移动
    if bullet.y < -bullet.h:
        bullet_sound.play(1)
        bullet.x = plane.x
        bullet.y = plane.y
    # 击中效果
    if bullet.collide(enemy):
        hit_sound.play(1)
        enemy.y = -enemy.h/2
        enemy.x = random.randint(0, 480)
        bullet.x = plane.x
        bullet.y = plane.y
        enemy.speed = random.random() * 5
        plane.score = plane.score + 10
    # 绘制游戏元素
    bg.draw()
    bullet.draw()
    plane.draw()
    enemy.draw()
    score_text.draw()
    
run(GameLoop) # 准备就绪，开始运行
