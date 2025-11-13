"""11/13/25
二叉搜索树
    首先它是一棵二叉树
    其次左子树及其下属都比根节点小,右子树及其下属都比根节点大

查找,插入
    查找和插入的性质相差不大,按深度搜索
"""
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None   # 定义左右子节点与父节点
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self, li = None):
        self.root = None     # 根节点
        if li:
            # li非空
            for val in li:
                self.inset_no_rec(val)  # 有值使用非递归插入方法,递归较慢

    def insert(self, node, val):
        # node为递归的查找结点位置
        if not node:
            # 若node为空
            node = BiTreeNode(val) # 结束条件:此处无节点则落地
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)    # 对左子节点进行插入递归
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)    # 对右子节点进行插入递归
            node.rchild.parent = node
        # 一般不存在相同键值情况,所以不用考虑相等情况
        return node
    
    def inset_no_rec(self, val):
        p = self.root            # 初始位置,初始值定义为了None(line18)
        if not p:
            # 对空树情况进行处理
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                # 小于根节点往左走
                if p.lchild:
                    # 左子树有值,则指针p继续向下比较,直到落地
                    p = p.lchild
                else:
                    # 没有值则把节点直接放在这里
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p         # 完善双向关系
                    return
            elif val > p.data:
                # 往右走
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return
    
    def pre_order(self, root):
        if root:  # root非空
            print(root.data, end = ",") # 根左右
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)       # 左根右
            print(root.data, end = ",")
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)      # 左右根
            self.post_order(root.rchild)
            print(root.data, end = ",")

import random
li = list(range(100))
random.shuffle(li)

# tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
tree = BST(li)
tree.pre_order(tree.root)   # 前序返回4,2,1,3,6,5,7,9,8,
print("")
tree.in_order(tree.root)    # 中序返回1,2,3,4,5,6,7,8,9,
print("")                   # 二叉搜索树的中序序列按照左中右能够按升序输出
tree.post_order(tree.root)  # 后序返回1,3,2,5,8,9,7,6,4,
print("")