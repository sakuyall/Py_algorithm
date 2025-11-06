"""11/5/25
栈的应用:迷宫问题
    给一个二维列表表示迷宫,0表示通道,1表示围墙
    设计算法求一条走出迷宫的路径
回溯法:
    采用栈-深度优先搜索,思路为从一个节点开始,任意找下一个能走的点
    找到不能走的点时退回上一个点寻找是否有其他方向的点
    使用栈储存当前路径
"""
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x+1, y),  # lambda匿名函数,参数:返回结果
    lambda x, y: (x-1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x, y-1)
]

def maze_path(x1, y1, x2, y2):
    """分别代表起点与终点"""
    stack = []
    stack.append((x1, y1))    # 列表内存放的元组
    while len(stack) > 0:     # 栈空表明没有路了
        curNode = stack[-1]   # 当前位置
        if curNode[0] == x2 and curNode[1] == y2:
            # 判断是否走到终点
            for p in stack:
                print(p)
            for i in maze:
                print(i, end = "\n")
            return True       # 完成寻路
        
        # 接着往四个方向找,上(x-1, y)下(x+1, y)左(x, y-1)右(x, y+1)
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 把当前数值依次传入lambda表达式后输出下一步位置
            if maze[nextNode[0]][nextNode[1]] == 0:
                # 若maze矩阵中该位置为0则可走
                stack.append(nextNode)
                print(stack)
                maze[nextNode[0]][nextNode[1]] = 2  # 标记为2表示已走过
                # 找到了就找下一步
                break
        else:
            stack.pop()   # 这个格子出栈
    else:
        return False   # 栈空没有路

maze_path(1, 1, 8, 8)