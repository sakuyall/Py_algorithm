"""11/13-14/25
二叉搜索树
    首先它是一棵二叉树
    其次左子树及其下属都比根节点小,右子树及其下属都比根节点大

查找,插入
    查找和插入的性质相差不大,按深度搜索

删除
    删除叶子节点-直接删除
    删除有两个孩子的节点-将其右子树最小节点(该节点最多有一个右子节点)删除并替换到当前位置
    用左边最大的也行(因为要保证二叉搜索树的定义)

效率
    平均情况下二叉搜索树的搜索时间复杂度为O(nlogn)
    可能存在最坏情况二叉树全为同一方向的子节点(偏斜)

解决方案
    随机化插入
    AVL树(见下节)
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
    
    def query(self, node, val):    # 查找
        if not node:
            return None
        elif node.data < val:
            return self.query(node.lchild, val)
        elif node.data > val:
            return self.query(node.rchild, val)
    
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None     # 找不到返回空

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

    def __remove_node_1(self, node):
        # 情况一 node是叶子节点的情况
        if not node.parent:
            # node的parent为空时(说明是根节点)
            self.root = None
        if node == node.parent.lchild:
            # 若node是其父节点的左子节点
            node.parent.lchild = None
        elif node == node.parent.rchild:
            # 若node是其父节点的右子节点
            node.parent.rchild = None
    
    def __remove_node_21(self, node):
        # 情况21 node只有一个左子节点
        if not node.parent:
            # 是根节点就把它唯一的子节点上位作为根
            self.root = node.lchild
            node.lchild.parent = None    # 将左子节点升为根节点(父节点None)
        elif node == node.parent.lchild:
            # 若node是其父节点的左子节点
            node.parent.lchild = node.lchild    # node父节点与node左子节点连接
            node.lchild.parent = node.parent    # 孙子把爷爷当父亲
        else:
            # 若node是其父节点的右子节点
            node.parent.rchild = node.lchild    # 一个道理
            node.lchild.parent = node.parent
        
    def __remove_node_22(self, node):
        # 情况22 node只有一个右子节点
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:
            # 首先判断不是空树,再开始删除
            node = self.query_no_rec(val)
            if not node:
                # 87行找不到对应元素就返回空
                # 此时返回False
                raise ValueError("查找的值在树中不存在")
        if not node.lchild and not node.rchild:
            # 左右子节点都为空
            self.__remove_node_1(node)
        elif not node.rchild:
            # 仅有左子节点
            self.__remove_node_21(node)
        elif not node.rchild:
            # 仅有右子节点
            self.__remove_node_22(node)
        else:
            # 两个都有,找右子树最小节点出来,找左边最大也行
            min_node = node.rchild
            # 也就是进入根节点右子树,重复寻找左子节点的左子节点直至没有位置
            while min_node.lchild:
                min_node = min_node.lchild
            # 将获取到值的覆盖到当前node位置
            node.data = min_node.data
            # 接着在原位置删除min_node(它没有左子节点)执行删除函数
            # 所以它要么是叶子节点,要么还有一个右子节点
            if min_node.rchild:
                # 若存在右子节点
                self.__remove_node_22(min_node)
            else:
                self.__remove_node_1(min_node)

import random
li = list(range(100))
random.shuffle(li)

# tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
# tree = BST(li)
tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
# tree.pre_order(tree.root)   # 前序返回4,2,1,3,6,5,7,9,8,
# print("")
tree.in_order(tree.root)    # 中序返回1,2,3,4,5,6,7,8,9,
print("")                   # 二叉搜索树的中序序列按照左中右能够按升序输出
# tree.post_order(tree.root)  # 后序返回1,3,2,5,8,9,7,6,4,
# print("")
tree.delete(4)
tree.in_order(tree.root)   # 返回1,2,3,5,6,7,8,9,