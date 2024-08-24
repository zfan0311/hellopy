from hellopy import *
import cv2, random, os, pyautogui
from onlyshow.LoongPy import draw_hand, Loong,  player, RiceBall, cap, hands, bgm, sfx
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()

def find_image_files(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 可能的图片文件扩展名

    image_files = []  # 存储图片文件路径的列表

    # 遍历指定文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名是否是图片文件扩展名
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(folder_path + "/" + file)

    return image_files

# 测试代码
folder_path = './food'  # 替换为你的文件夹路径
image_paths = find_image_files(folder_path)
for path in image_paths:
    print(path)

# 设置窗口参数
window.set_size(screen_width,screen_height)
window.fps = 10

# 设置游戏模式
player.mode = 2 # 0-鼠标，1-大拇指，2-食指，3-中指，4-无名指，5-小拇指

# 添加龙
loong = Loong(8)
# 添加食物列表
foods = []
for item in image_paths:
    foods.append(Sprite(random.randint(0,screen_width),random.randint(0,screen_height),50,50,item))
print(len(foods))

# 背景音乐
bgm.play()

def Loop():
    # 绘制背景
    window.clear()
    rectangle(window.w/2,window.h/2,window.w,window.h,"#4D32AF")

    # 控制龙头
    if player.mode != 0:
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

    for item in foods:
        if loong.head.collide(item):
            player.score += 1
            loong.body_length = 8 + player.score // 5
            sfx.play(1)
            item.x = random.randint(0,screen_width)
            item.y = random.randint(0,screen_height)
        item.draw()
    loong.draw()
    text("得分："+str(player.score),30,30,50,"white")

run(Loop)
