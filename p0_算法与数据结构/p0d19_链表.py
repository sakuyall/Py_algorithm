"""11/7/25不理解需要复听p59节
链表
    链表由一系列节点组成,节点包含两部分
    数据域item与指向下一个节点的指针next
创建与遍历
"""
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
# 手动建立链表的方法
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
# print(a.next.next.next.item) # 超限返回AttributeError: 'NoneType' object has no attribute 'item'

# 头插法
def create_linklist_head(li):
    head = Node(li[0])         # 最开始的链头
    for element in li[1:]:
        node = Node(element)   # 新界点插入到头节点前
        node.next = head       # 先进行连接,新链尾指开始链头
        head = node            # 再更新链头
    return head                # 返回最终链头
def print_linklist(lk):
    while lk:       # lk不是None情况下执行
        print(lk.item, end = ",")
        lk = lk.next

lk = create_linklist_head([1, 2, 3])
print(lk.item)                 # 返回3
print_linklist(lk)             # 返回3,2,1,
print("\n")

# 尾插法
def create_linklist_tail(li):
    head = Node(li[0])      # 要同时维护头和尾巴位置节点
    tail = head             # 第一个链头尾一样的
    for element in li[1:]:
        node = Node(element)
        tail.next = node    # 先连接下一个
        tail = node         # 再把tail后移
    return head
lk = create_linklist_tail([1, 2, 3, 6, 8])
print_linklist(lk)
"""
插入
    对于列表的insert方法进行插入,其时间复杂度平均为O(n)
    而链表进行插入需要进行以下步骤
    先把插入链尾连接下一链头,再把前链尾连到插入链头
    
    使用p代表插入链,curNode代表前链,则插入可以写作:
    p.next = curNode.next
    curNode.next = p
    不按照此顺序则会导致后链丢失在内存中

删除
    先把欲删除的下链指定为p,接着连接上链与下下链,随后删除p
    p = curNode.next
    curNode.next = curNode.next.next    # 把下下个作为下一个
                                        # 或者写作curNode.next = p.next
    del p
"""