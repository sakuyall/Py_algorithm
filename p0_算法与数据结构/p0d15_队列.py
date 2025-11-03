"""11/2/25
队列(Queue)
    队列是一个数据集合,仅允许在一端插入,另一端删除
    特点:FIFO(first-in,first-out)也叫先进先出
    队尾入队队头出队
"""
# 建立环形队列
class Queue:
    """
    front == maxsize + 1时,再前进一个位置就到0,所以
    队首指针前进1:front = (front + 1) % maxsize
    队尾指针前进1:rear = (rear + 1) % maxsize
    队空条件:rear = front
    队满条件:(rear + 1) % maxsize == front(同样是解决下一个位置为0的情况)
    为区分队空与队满,规定对首队尾之间空一格
    """
    def __init__(self, size = 100):
        self.size = size
        self.queue = [0 for _ in range(size)]   # 长度为100的空列表0占位
        self.rear = 0    # 队尾指针
        self.front = 0   # 队首指针
    
    def push(self, element):
        if not self.is_filled():     # 不满进行添加
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element     # 队尾进栈
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():      # 非空进行排除
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]       # 队首出栈
        else:
            raise IndexError("Queue is empty")
    
    def is_empty(self):
        return self.rear == self.front      # 判断队空

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front  # 判断队满
    
q = Queue(5)
for i in range(4):
    q.push(i)
print(q.pop())

