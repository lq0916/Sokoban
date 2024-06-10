import pygame
from button import Button

class Game_init:
    pygame.init()
    try:
        # 设置游戏图标
        gameicon = pygame.image.load('image/BoxIcon.png')
        # 展示游戏图标
        pygame.display.set_icon(gameicon)
        # 设置背景音乐
        bgm = ["music.mp3", "music.mp3", "music.mp3"]
        # 设置背景音乐音量为50%
        pygame.mixer.music.set_volume(0.5)
        # 设置过关时的音乐
        chapterpasssound = pygame.mixer.Sound('Chapter Pass Sound.wav')

        # 设置界面大小
        screen = pygame.display.set_mode((400, 400))
        # “开始游戏”按钮
        button1 = Button('image/GameStartUp.png', 'image/GameStartDown.png', (200, 300))
        # “游戏说明”按钮
        button2 = Button('image/GameTipsUp.png', 'image/GameTipsDown.png', (200, 350))
        # “第一关”按钮
        buttonc1 = Button('image/Chapter1Up.png', 'image/Chapter1Down.png', (200, 175))
        # “第二关”按钮
        buttonc2 = Button('image/Chapter2Up.png', 'image/Chapter2Down.png', (200, 225))
        # “第三关”按钮
        buttonc3 = Button('image/Chapter3Up.png', 'image/Chapter3Down.png', (200, 275))
        # “返回主界面”按钮
        buttonmain = Button('image/ReturnInterfaceUp.png', 'image/ReturnInterfaceDown.png', (200, 350))
        # “下一关”按钮
        buttonnext = Button('image/NextChapterUp.png', 'image/NextChapterDown.png', (100, 350))
        # “返回选关”按钮（样式1）
        buttonret1 = Button('image/Return2ChooseUp.png', 'image/Return2ChooseDown.png', (300, 350))
        # “返回选关”按钮（样式2）
        buttonret2 = Button('image/Return2ChooseUp.png', 'image/Return2ChooseDown.png', (200, 350))
        # 主界面背景图片
        interface = pygame.image.load("image/Interface.png")
        # 游戏说明界面图片
        gametips = pygame.image.load("image/GameTips.png")
        # 选择关卡界面图片
        choosechapter = pygame.image.load("image/ChooseChapter.png")
        # 通关提示界面图片
        chapterpass = pygame.image.load("image/ChapterPass.png")
        # 加载游戏界面图片资源
        skin = pygame.image.load("image/borgar.png")
        skin = skin.convert()

    # 显示错误输出
    except pygame.error as msg:
        raise (SystemExit(msg))
    # 设置标题
    pygame.display.set_caption('弱智推箱子_lq01')
