"""11/6/25
用队列实现迷宫问题
    队列-广度优先搜索
    思路:从一个结点开始,寻找所有接下来能走的节点,直到找到出口
    采用队列来储存当前节点路径,走下一步时上一步出队
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

from collections import deque
def print_r(path):
    curNode = path[-1]
    realpath = []     # 到达终点的路径

    while curNode[2] != -1:       # 这个-1也是同理
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]

    realpath.append(curNode[0:2])     # 加入起点
    realpath.reverse()                # 改变原有列表
    for node in realpath:
        print(node, end = "--")

def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))    # 起点入队,坐标以及位置,这个-1是为后边len(path)包的饺子
    path = []
    while len(queue) > 0:         # 只要队不空就是有路
        curNode = queue.pop()
        # 队首出队
        path.append(curNode)      # 将先前走过的路径加入到path中,而不是保留在队列中
        if curNode[0] == x2 and curNode[1] == y2:
            # 若到达终点
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                # 下一节点进队,并带上它的由来,便于最后寻找整体路径
                # curNode让它来的,所以这里写curNode在path中的索引位置,也就是最后的位置
                maze[nextNode[0]][nextNode[1]] = 2      # 走过位置标记为2
    else:
        print("没有路")
        return False

maze_path_queue(1, 1, 8, 8)