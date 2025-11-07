"""11/7/25
双链表
    单链表指针在后,双链表前后都有指针
插入
    类似于单链表的方法,先连接后边,只不过双链表是要建立两个前后的关系
    p.next = curNode.next
    curNode.next.prior = p
    p.prior = curNode
    curNode.next = p

删除
p = curNode.next
curNode.next = p.next   # 或curNode.next.next
p.next.prior = curNode
del p

顺序表与链表总结

    复杂度对比      顺序表          链表
    按元素值          n              n
    按下标            1              n
    某处插入删除      n              1  

链表的插入与删除操作明显快于顺序表
链表的内存分配更灵活,解决c数组长度固定的问题
链式存储结构对树与图具有很大启发
"""