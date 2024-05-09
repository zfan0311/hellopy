from hellopy import *
import cv2, math
from onlyshow.LoongPy import draw_hand, Loong,  player, RiceBall, cap, hands, bgm, sfx

# 设置窗口参数
window.set_size(1200,800)
window.fps = 10

# 设置游戏模式
player.mode = 2 # 0-鼠标，1-大拇指，2-食指，3-中指，4-无名指，5-小拇指，6-自动模式

# 添加龙
loong = Loong(3)
# 添加汤圆
rb1 = RiceBall()
rb2 = RiceBall()
rb3 = RiceBall()

# 背景音乐
bgm.play()
def get_dis(a,b):
    return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)


def Loop():
    # 绘制背景
    window.clear()
    rectangle(window.w/2,window.h/2,window.w,window.h,"firebrick4")
    if player.mode == 6:
        min_dis = rb1
        for item in [rb2, rb3]:
            if get_dis(loong.head, item) < get_dis(loong.head, min_dis):
                min_dis = item
        player.controller = min_dis
    # 控制龙头
    elif player.mode != 0:
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # 水平翻转图像
                frame_flipped = cv2.flip(frame, 1)
                # 将图像转换为RGB格式并传递给MediaPipe模型进行处理
                frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)
                results = hands.process(frame_rgb)
                # 检查是否检测到手部关键点
                if results.multi_hand_landmarks:
                    player.main_hand = results.multi_hand_landmarks[0]
                    draw_hand(player.main_hand)
                    player.controller = player.finger_nodes[player.mode*4]
            else:
                player.controller = mouse
    loong.head_to(player.controller)

    # 吃元宵的逻辑
    if loong.head.collide(rb1):
        rb1.reset()
        player.score += 1
        loong.body_length += 1
        sfx.play(1)
    if loong.head.collide(rb2):
        rb2.reset()
        player.score += 1
        loong.body_length += 1
        sfx.play(1)
    if loong.head.collide(rb3):
        rb3.reset()
        player.score += 1
        loong.body_length += 1
        sfx.play(1)
    # 绘制游戏图像
    rb1.draw()
    rb2.draw()
    rb3.draw()
    loong.draw()
    text("得分："+str(player.score),30,30,50,"white")

run(Loop)
