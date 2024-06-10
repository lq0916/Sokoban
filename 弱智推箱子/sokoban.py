'''

符号说明：
"." 空白处，可通过
"#" 墙,不可通过
"@" 人,可移动
"$" 箱子,可推动
"*" 终点
"&" 到终点的箱子

'''

class Sokoban:
    # 构造函数
    def __init__(self):
        # 设置关卡地图（三个）
        self.level = [list('...#######' + \
                           '####.....#' + \
                           '#..***.$.#' + \
                           '#..*..#.##' + \
                           '#.#####.#.' + \
                           '#.#...#.#.' + \
                           '#...$.#.#.' + \
                           '###$#.#.#.' + \
                           '#...$...#.' + \
                           '#.@.##..#.' + \
                           '#########.'),
                      list('.#######....' + \
                           '##.....##...' + \
                           '#..#.$..#...' + \
                           '#.$.$$#.#...' + \
                           '##.#.$..###.' + \
                           '.#...##.*.##' + \
                           '.#####..*..#' + \
                           '.....#.#*..#' + \
                           '.....#..*..#' + \
                           '.....#..*@.#' + \
                           '.....#######'),
                      list('....#####..........' + \
                           '....#...#..........' + \
                           '....#$..#..........' + \
                           '..###..$##.........' + \
                           '..#..$.$.#.........' + \
                           '###.#.##.#...######' + \
                           '#...#.##.#####..**#' + \
                           '#.$..$..........**#' + \
                           '#####.###.#@##..**#' + \
                           '....#.....#########' + \
                           '....#######........')]
        # 设置每个关卡地图大小（宽度、高度）
        self.w = [10, 12, 19]
        self.h = [11, 11, 11]
        # 设置每个关卡开始时，人在地图中的坐标位置
        self.man = [92, 117, 163]
        # 设置每个关卡中的箱子总数
        self.boxCnt = [4, 5, 6]
        # 设置每个关卡中到达目标点的箱子总数
        self.boxInPositionCnt = [0, 0, 0]

    # 以下是元素变换函数
    # 转换为箱子
    def toBox(self, chapter, index):
        if self.level[chapter][index] == '.' or self.level[chapter][index] == '@':
            self.level[chapter][index] = '$'
        else:
            self.level[chapter][index] = '&'

    # 转换为人
    def toMan(self, chapter, index):
        if self.level[chapter][index] == '.' or self.level[chapter][index] == '$':
            self.level[chapter][index] = '@'
        else:
            self.level[chapter][index] = '+'

    # 转换为地面
    def toFloor(self, chapter, index):
        if self.level[chapter][index] == '@' or self.level[chapter][index] == '$':
            self.level[chapter][index] = '.'
        else:
            self.level[chapter][index] = '*'
    # 偏移量计算函数
    def offset(self, d, width):
        d4 = [-1, -width, 1, width]
        m4 = ['l', 'u', 'r', 'd']
        return d4[m4.index(d.lower())]
    # 绘图函数，在窗口中绘制图当前地图及布局
    def draw(self, screen, chapter, skin):
        w = skin.get_width() / 4
        # print(self.level)
        # print(self.w[chapter], self.h[chapter])
        for i in range(0, self.w[chapter]):
            for j in range(0, self.h[chapter]):
                if self.level[chapter][j * self.w[chapter] + i] == '#':
                    screen.blit(skin, (i * w, j * w), (0, 2 * w, w, w))
                elif self.level[chapter][j * self.w[chapter] + i] == '.':
                    screen.blit(skin, (i * w, j * w), (0, 0, w, w))
                elif self.level[chapter][j * self.w[chapter] + i] == '@':
                    screen.blit(skin, (i * w, j * w), (w, 0, w, w))
                elif self.level[chapter][j * self.w[chapter] + i] == '$':
                    screen.blit(skin, (i * w, j * w), (2 * w, 0, w, w))
                elif self.level[chapter][j * self.w[chapter] + i] == '*':
                    screen.blit(skin, (i * w, j * w), (0, w, w, w))
                elif self.level[chapter][j * self.w[chapter] + i] == '+':
                    screen.blit(skin, (i * w, j * w), (w, w, w, w))
                elif self.level[chapter][j * self.w[chapter] + i] == '&':
                    screen.blit(skin, (i * w, j * w), (2 * w, w, w, w))
# 移动函数（返回1表示推了箱子的移动，返回0表示没推箱子的移动，返回-1表示移动不成功）
    def move(self, chapter, op):
        # 计算偏移
        h = self.offset(op, self.w[chapter])
        # 人前方没有障碍物
        if self.level[chapter][self.man[chapter] + h] == '.' or self.level[chapter][self.man[chapter] + h] == '*':
            # 只有人移动（没有推箱子）
            self.toMan(chapter, self.man[chapter] + h)
            self.toFloor(chapter, self.man[chapter])
            self.man[chapter] += h
            return 0
        # 人前方有障碍物
        elif self.level[chapter][self.man[chapter] + h] == '&' or self.level[chapter][self.man[chapter] + h] == '$':
            # 障碍物为箱子
            if self.level[chapter][self.man[chapter] + 2 * h] == '.' or self.level[chapter][
                self.man[chapter] + 2 * h] == '*':
                # 人推着箱子移动
                if self.level[chapter][self.man[chapter] + h] == '&':
                    # 原来到达目标点的箱子被移出，数量-1
                    self.boxInPositionCnt[chapter] -= 1
                    # print(self.boxInPositionCnt)
                self.toBox(chapter, self.man[chapter] + 2 * h)
                self.toMan(chapter, self.man[chapter] + h)
                self.toFloor(chapter, self.man[chapter])
                self.man[chapter] += h
                if self.level[chapter][self.man[chapter] + h] == '&':
                    # 有新的箱子到达目标点，数量+1
                    self.boxInPositionCnt[chapter] += 1
                    # print(self.boxInPositionCnt)
                return 1
            else:
                return -1
        else:
            return -1
# 还原函数
    def revmove(self, chapter, op):
        d = op[0]
        # flag记录之前一步的移动的布局变化情况，即move()函数返回的值
        flag = op[1]
        h = self.offset(d, self.w[chapter])
        # 人推着箱子移动了
        if flag == 1:
            # 还原上一步箱子的状态和人的状态
            if self.level[chapter][self.man[chapter] + h] == '&':
                # 原来到达目标点的箱子被移出，数量-1
                self.boxInPositionCnt[chapter] -= 1
                # print(self.boxInPositionCnt)
            self.toBox(chapter, self.man[chapter])
            self.toMan(chapter, self.man[chapter] - h)
            self.toFloor(chapter, self.man[chapter] + h)
            self.man[chapter] -= h
            if self.level[chapter][self.man[chapter] + h] == '&':
                # 有新的箱子到达目标点，数量+1
                self.boxInPositionCnt[chapter] += 1
                # print(self.boxInPositionCnt)
        # 只有人移动了
        elif flag == 0:
            # 还原人的状态
            self.toMan(chapter, self.man[chapter] - h)
            self.toFloor(chapter, self.man[chapter])
            self.man[chapter] -= h