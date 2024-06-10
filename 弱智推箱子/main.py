


from collections import deque

# 导入  模块
from display import *
from sokoban import Sokoban
from game_init import Game_init   # 游戏初始化加载


def main():
    # 初始化pygame
    ga = Game_init()

    # 设置游戏定时器
    clock = pygame.time.Clock()
    # 按住某个键每隔interval(50)毫秒产生一个KEYDOWN事件，delay(200)就是多少毫秒后才开始触发这个事件
    pygame.key.set_repeat(200, 50)
    while True:
        # 设置游戏绘制的最大帧率
        clock.tick(60)
        flag = showGameInterface(ga.screen, ga.interface, ga.button1, ga.button2)
        # 点击开始游戏
        if flag == 1:
            # 选择关卡界面循环
            while True:
                clock.tick(60)
                # chapter记录了用户在选择关卡界面上点击的是哪个按钮
                chapter = showChapterInterface(ga.screen, ga.choosechapter, ga.buttonc1, ga.buttonc2, ga.buttonc3, ga.buttonmain) - 1
                # 如果选择的是返回主界面，则退出本界面的循环
                if chapter == 3:
                    break
                # 没有选择则刷新等待
                if chapter == -1:
                    pygame.display.update()
                    continue
                # 如果选择了某一个关卡
                # 创建推箱子游戏主类的实例
                skb = Sokoban()
                # 绘制游戏窗口
                ga.screen.fill(ga.skin.get_at((0, 0)))
                skb.draw(ga.screen, chapter, ga.skin)
                # 加载并播放每一关对应的音乐
                pygame.mixer.music.load(ga.bgm[chapter])
                pygame.mixer.music.play(-1)
                # 利用双端队列deque来维护历史操作队列
                dq = deque([])
                # 游戏进程主循环
                while True:
                    clock.tick(60)
                    # retGameInterface记录是否返回选关界面
                    retGameInterface = False
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == KEYDOWN:
                            # 用户按下了Escape按键，则退出游戏进程循环
                            if event.key == K_ESCAPE:
                                retGameInterface = True
                                break
                            # 如果按下“上”、“下”、“左”、“右”的操作
                            # 画面更新，调用move函数进行移动改变布局
                            # 然后把这一步对象（包括由移动方向和move()函数返回值构成的操作记录元组）放进deque内保存
                            # 绘制改变布局后的新的界面
                            elif event.key == K_LEFT:
                                flag = skb.move(chapter, 'l')
                                dq.append(['l', flag])
                                skb.draw(ga.screen, chapter, ga.skin)
                            elif event.key == K_UP:
                                flag = skb.move(chapter, 'u')
                                dq.append(['u', flag])
                                skb.draw(ga.screen, chapter, ga.skin)
                            elif event.key == K_RIGHT:
                                flag = skb.move(chapter, 'r')
                                dq.append(['r', flag])
                                skb.draw(ga.screen, chapter, ga.skin)
                            elif event.key == K_DOWN:
                                flag = skb.move(chapter, 'd')
                                dq.append(['d', flag])
                                skb.draw(ga.screen, chapter, ga.skin)
                            # 如果按下Backspace按键，则进行回退操作
                            elif event.key == K_BACKSPACE:
                                # 如果队列不为空
                                if len(dq) > 0:
                                    # 取出当前队尾的对象（操作记录元组）
                                    op = dq.pop()
                                    # 调用还原函数
                                    skb.revmove(chapter, op)
                                    # 绘制改变布局后的新的界面
                                    skb.draw(ga.screen, chapter, ga.skin)
                            # 如果当前队列长度大于50（即存放的操作记录元组数超过50条），则取出队首的对象（即丢弃最早的一条记录），以保持当前队列长度在50以内
                            if len(dq) > 50:
                                dq.popleft()
                    # 如果到达目标点的箱子数量与本关卡箱子总数相等，则过关
                    if skb.boxInPositionCnt[chapter] == skb.boxCnt[chapter]:
                        clock.tick(60)
                        # 背景音乐停止播放
                        pygame.mixer.music.stop()
                        # 根据这是哪一关来显示不同的通关界面（第三关通关界面没有“下一关”的按钮）
                        if chapter == 0 or chapter == 1:
                            win = showWinInterface(ga.screen, ga.chapterpass, ga.buttonnext, ga.buttonret1, 1)
                        elif chapter == 2:
                            win = showWinInterface(ga.screen, ga.chapterpass, ga.buttonnext, ga.buttonret2, 0)
                        # 播放通关音效
                        ga.chapterpasssound.play()
                        # win记录了点击了哪个按钮
                        # 如果点击了“下一关”按钮
                        if win == 1:
                            # 清空队列
                            dq.clear()
                            # 如果不是最后一关
                            if chapter < 2:
                                # 自动跳到下一关
                                chapter += 1
                                # 停止通关音乐的播放
                                ga.chapterpasssound.stop()
                                # 绘制下一关的关卡地图布局
                                ga.screen.fill(ga.skin.get_at((0,0)))
                                skb.draw(ga.screen, chapter, ga.skin)
                                # 加载并播放下一关对应的背景音乐
                                pygame.mixer.music.load(ga.bgm[chapter])
                                pygame.mixer.music.play(-1)
                            pygame.display.update()
                            continue
                        # 如果点击了“返回选关”按钮，则退出该界面的循环
                        elif win == 2:
                            retGameInterface = True
                    # 如果退出推箱子游戏进程，则关闭所有的音乐
                    if retGameInterface == True:
                        ga.chapterpasssound.stop()
                        pygame.mixer.music.stop()
                        pygame.display.update()
                        break
                    pygame.display.update()
        # 如果点击了“游戏说明”按钮
        elif flag == 2:
            clock.tick(60)
            retGameInterface = False
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            retGameInterface = True
                            break
                ga.screen.blit(ga.gametips, (0,0))
                pygame.display.update()
                if retGameInterface == True:
                    break
        pygame.display.update()
if __name__ == '__main__':
    main()