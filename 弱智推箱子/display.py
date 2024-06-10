import pygame, sys
from pygame.locals import *

# 显示游戏主界面
def showGameInterface(screen, interface, startGame, gameTips):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # 点击开始游戏
            if startGame.inButtonRange():
                return 1
            # 点击游戏说明
            elif gameTips.inButtonRange():
                return 2
    # 绘制背景
    screen.blit(interface, (0,0))
    # 显示开始游戏
    startGame.show(screen)
    # 游戏说明
    gameTips.show(screen)
    return 0

# 显示关卡选择界面的函数
def showChapterInterface(screen, interface, chapter1, chapter2, chapter3, prevInterface):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # 如果点击的是“第一关”
            if chapter1.inButtonRange():
                return 1
            # 如果点击的是“第二关”
            elif chapter2.inButtonRange():
                return 2
            # 如果点击的是“第三关”
            elif chapter3.inButtonRange():
                return 3
            # 如果点击的是“返回主界面”
            elif prevInterface.inButtonRange():
                return 4
    # 绘制背景图片
    screen.blit(interface, (0,0))
    # 显示“第一关”按钮
    chapter1.show(screen)
    # 显示“第二关”按钮
    chapter2.show(screen)
    # 显示“第三关”按钮
    chapter3.show(screen)
    # 显示“返回主界面”按钮
    prevInterface.show(screen)
    return 0

# 显示过关界面的函数
def showWinInterface(screen, interface, nextChapter, returnToChoose, flag):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # 如果点击的是“下一关”
            if nextChapter.inButtonRange():
                return 1
            # 如果点击的是“返回选关”
            elif returnToChoose.inButtonRange():
                return 2
    # 绘制背景图片
    screen.blit(interface, (0,0))
    # flag表示是否不是最后一关，如果不是则显示“下一关”按钮，否则不显示
    if flag:
        nextChapter.show(screen)
    # 显示“返回选关”按钮
    returnToChoose.show(screen)
    return 0