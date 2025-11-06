"""11/4/25
双向队列
    队首队尾都支持进队和出队
    也可以看作是两个栈底对在了一起
"""
# 内置模块双向队列
from collections import deque
q = deque([1, 2, 3], 5)     # 分别为队列, 队列长度 空队列就什么也不加
q.append(1)                 # 队尾入队,如果队列已满则全部自动前移,队首元素直接被挤出去
q.popleft()                 # 队首出队

# 以下是用于双向队列的方法
q.appendleft(1)             # 队首进队
q.pop()                     # 队尾出队
# 因为默认的append和pop都是对队尾操作的

# 实现打印文件后几行
def tail(n):
    with open("D:/engifiles/code/py/test/exception/test.txt", "r") as f:
        q1 = deque(f, n)
        return q1
for line in tail(5):
    print(line, end = "")