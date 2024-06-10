import pygame
'''

设计button类

'''

'''
convert_alpha() 方法是一个 Pygame Surface 对象的方法，
它用于创建一个新的具有透明度（alpha 通道）的表面。这在你需要透明背景的图片时特别有用。

convert_alpha() 方法是一个 Pygame Surface 对象的方法，它用于创建一个新的具有透明度（alpha 通道）的表面。
这在你需要透明背景的图片时特别有用。

'''

# 按钮类
class Button(object):
    # 构造函数
    def __init__(self, buttonUpImage, buttonDownImage, pos):
        # 按钮未按下的图片样式
        self.buttonUp = pygame.image.load(buttonUpImage).convert_alpha()
        # 按钮按下的图片样式
        self.buttonDown = pygame.image.load(buttonDownImage).convert_alpha()
        # 按钮在窗口中的位置
        self.pos = pos

    # 检查鼠标是否在按钮图片范围内
    def inButtonRange(self):
        # 获取鼠标的位置
        mouseX, mouseY = pygame.mouse.get_pos()
        x, y = self.pos
        w, h = self.buttonUp.get_size()
        inX = x - w / 2 < mouseX < x + w / 2
        inY = y - h / 2 < mouseY < y + h / 2
        return inX and inY

    # 在窗口中显示按钮
    def show(self, screen):
        w, h = self.buttonUp.get_size()
        x, y = self.pos
        # 根据鼠标位置变换样式
        if self.inButtonRange():
            screen.blit(self.buttonDown, (x - w / 2, y - h / 2))
        else:
            screen.blit(self.buttonUp, (x - w / 2, y - h / 2))
