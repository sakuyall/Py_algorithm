"""11/14-15/25
AVL树(自平衡二叉搜索树)
性质
    任一节点左右子树高度差的绝对值不超过1(空节点高度为0,叶子为1,之后往上递增)
    且左右子树都是平衡二叉树

旋转
    在插入节点后可能会破坏AVL树的平衡
    从叶子节点向上找到第一个破坏平衡的位置K
    对 K 右子节点 K2 的右子树插入导致--左旋(左子节点给上级,自己上移,上级下移为它的左子节点),
    反过来同理就是右旋(右子节点给上级,自己上移,上级下移为它的右子节点)
    对右子节点K2的左子树插入导致--右旋左旋,反过来左右
"""
# 旋转实现
from p0d24_二叉搜索树 import BiTreeNode, BST
# 直接继承上一节的类,所以文件名尽量还是全英文比较好
class AVLNode(BiTreeNode):
    def __init__(self, data):
        super().__init__(data)  # 注意super不写self
        # BiTreeNode.__init__(self, data)
        self.bf = 0             # 定义的平衡因子balancefactor,右子树减左子树高度(度)获得-1偏左1偏右

class AVLTree(BST):
    def __init__(self, li=None):
        super().__init__(li)

    def rotate_left(self, p, c):
        # 注意在删除情况下这两个旋转函数是有问题的
        """左旋 变换示意,s3长度为h+1,s1s2为h
                p                                   c
            s1      c         --->              p       s3
                 s2   s3                     s1   s2
        """
        s2 = c.lchild     # 把s2确定为c左子节点(欲操作对象)
        p.rchild = s2     # 把s2给p
        if s2:
            # 注意反向连接回去要判断它是否为空
            s2.parent = p  # 则双向建立联系

        c.lchild = p     # 更新pc关系,先找子再认父
        p.parent = c
        p.bf = 0
        c.bf = 1
    
    def rotate_right(self, p, c):
        """右旋 变换示意,s1长度大于s2s3
                p                                c
            c      s3         --->           s1       p
         s1   s2                                   s2   s3
        """
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        
        c.rchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0

    def rotate_right_left(self, p, c):
        """右左旋 变换示意,s2s3长度为h或h-1
                p                              g
            s1      c         --->         p       c
                  g   s4                 s1 s2   s3 s4
                s2 s3
        """
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g
        
        if g.bf > 0:
            p.bf = -1   # 插入到了s3
            c.bf = 1
        elif g.bf < 0:
            p.bf = 0    # 插入到了s2
            c.bf = 1
        else:
            p.bf = 0    # 插入到了g
            c.bf = 0

    def rotate_left_right(self, p, c):
        """右左旋 变换示意,s2s3长度为h或h-1
                p                              g
            c      s4         --->         c       p
         s1   g                          s1 s2   s3 s4
            s2  s3
        """
        g = c.rchild

        s2 = g.lchild
        c.lchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g
        
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0

    def insert_no_rec(self, val):
        # 暂且搁置,听其他讲解*2
        pass