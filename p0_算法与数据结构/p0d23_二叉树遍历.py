"""11/9/25
二叉树的链式储存
    将二叉树的节点定义为一个对象
    节点间通过类似链表方式连接
对于这样一个二叉树:
        E
     A     G
       C     F
      B D
"""
# 手动定义二叉树节点
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None   # 定义左右子节点
        self.rchild = None

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

print(root.lchild.rchild.data)
# 返回C
"""
二叉树的遍历
    对于一棵树的根D不同位置关系遍历,选定一节点后立刻看该节点作为根节点的树

DLR前序遍历EACBDGF
    根左右。前序遍历首先访问根结点然后遍历左子树，最后遍历右子树
    在遍历左、右子树时，仍然先访问根节点，然后遍历左子树，最后遍历右子树
    若二叉树为空则结束返回，否则：
    1)访问根结点
    2)前序遍历左子树
    3)前序遍历右子树
    需要注意的是：遍历左右子树时仍然采用前序遍历方法。

LDR中序遍历ABCDEGF
    左根右。中序遍历首先遍历左子树，然后访问根结点，最后遍历右子树
    比如选定一棵树先看左子树,左子树全部遍历完才会遍历根节点,右子树同理

LRD后序遍历BDCAFGE
    左右根。后序遍历首先遍历左子树，然后遍历右子树，最后访问根结点
    在遍历左、右子树时，仍然先遍历左子树，然后遍历右子树，最后遍历根结点
    若二叉树为空则结束返回，
    否则：
    1)后序遍历左子树
    2)后序遍历右子树
    3)访问根结点

层次遍历EAGCFBD
    按照层数从上到下从左到右进行遍历
    也就是顺序储存为列表的格式
"""
# 前序遍历递归
def pre_order(root):
    if root:  # root非空
        print(root.data, end = ",") # 根左右
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):
    if root:
        in_order(root.lchild)       # 左根右
        print(root.data, end = ",")
        in_order(root.rchild)

def post_order(root):
    if root:
        post_order(root.lchild)      # 左右根
        post_order(root.rchild)
        print(root.data, end = ",")

from collections import deque
def level_order(root):
    q = deque()
    q.append(root)
    while len(q) > 0:    # 只要队不空
        node = q.popleft()      # 出队一个元素,返回它的节点值
        print(node.data, end = ",")
        if node.lchild:         # 若存在子节点则子节点入队
            q.append(node.lchild)
        if node.rchild:
            q.append(node.rchild)

level_order(root)