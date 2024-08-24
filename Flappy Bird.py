from hellopy import *
import random
window.set_size(600,400)
sky1 = Sprite(300,200,600,400,"https://pic.imgdb.cn/item/65af296b871b83018a84d23d.jpg")
sky2 = Sprite(300,200,600,400,"https://pic.imgdb.cn/item/65af296b871b83018a84d23d.jpg")
hills1 = Sprite(300,330,600,140,"https://pic.imgdb.cn/item/65af2392871b83018a76405b.png")
hills2 = Sprite(300,330,600,140,"https://pic.imgdb.cn/item/65af2392871b83018a76405b.png")
bird = Sprite(100,200,60,45,"https://pic.imgdb.cn/item/65af2cc1871b83018a8ce04c.png")
cactus = Sprite(400,0,60,250,"https://pic.imgdb.cn/item/65af6e20871b83018a44b13e.png")
cactus2 = Sprite(400,400,60,250,"https://pic.imgdb.cn/item/65af2f2c871b83018a927668.png")
window.score = 0
bird.speed = 0

def Loop():
    window.clear()
    sky1.draw()
    sky2.draw()
    hills1.draw()
    hills2.draw()
    bird.draw()
    cactus.draw()
    cactus2.draw()
    text("得分："+str(window.score),10,10,20,"black")
    if bird.y < 0 or bird.y > 400 or bird.collide(cactus) or bird.collide(cactus2):
        text("游戏结束，你的得分："+str(window.score),80,170,40,"black")
        if Key("K_r").pressed():
            window.score = 0
            sky1.x = 300
            sky1.y = 200
            hills1.x = 300
            hills1.y = 330
            cactus.x = 400
            cactus.y = 0
            bird.x = 100
            bird.y = 200
            bird.speed = 0
    else:
        sky1.x -= 1
        if sky1.x <= -300:
            sky1.x = 300
        sky2.x = sky1.x + 600
        hills1.x -= 1.5
        if hills1.x <= -300:
            hills1.x = 300
        hills2.x = hills1.x + 600
        cactus.x -= 8
        if cactus.x < -30:
            cactus.x = 630
            cactus.y = random.randint(-100,100)
            window.score += 1
        cactus2.x = cactus.x
        cactus2.y = cactus.y + 400
        bird.speed = bird.speed + 0.2
        bird.y = bird.y + bird.speed
        if Key("K_SPACE").pressed():
            bird.speed = -4
run(Loop)
