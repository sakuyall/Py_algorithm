"""11/7-8/25
哈希表(散列表)
    构成了python的字典与集合
    好的哈希表将关键字尽可能平均地排布

哈希函数
    insert(key, value)插入键值对
    get(key)返回value,不存在key则返回空值
    delete(key)删除键为key的键值对

    除法哈希法:h(k) = k % m               # 最常见
    乘法哈希法:h(k) = floor(m*(A*key%1))  # A是个小数,对1取模即取小数部分
    全域哈希法:h(k) = ((a*key+b)%p)%m     # %也可写作mod
    方法仍在发展

直接寻址表
    当关键字的全域比较小时,直接寻址是一种简单有效的方法
    类似于计数排序中的用法,以关键字作为索引序列
    缺点:当全域较大时,需要消耗大量内存,且无法处理关键字不是数字的情况
    前边排序时介绍的也差不多了

哈希表(Hashing)
    以上两者的结合就是哈希表
    将key为k的元素放到函数h(k)上,而不是原来的k位置上
    假设有一长度为7的哈希表,哈希函数为h(k)=k%7,列表T为[0:6]
    那么如何区分取余相同的元素,这种情况叫做 哈希冲突
    解决方法如下

开放寻址法
    如果哈希函数返回位置已经有值,则向后探查新的位置来储存这个值
    线性探查:位置i被占用则向后探查i+1,i+2...布局过密则会导致查找次数过多
    二次探查:探查i+1^2,1-1^2,i+2^2,i-2^2...
    二次哈希:有n个哈希函数,第一个函数h1冲突就用h2...
    (不用这个)

拉链法
    冲突的元素将会接在已有元素后形成链表,头插尾插都可以
    查找时先带入哈希函数寻找索引位置,接着遍历该链表寻找
    使用链表提高了删除与插入的效率
"""
# 先建立链表类
class LinkList:        # 单链表
    class Node:        # 创建链节点类,上节做过
        def __init__(self, item = None):   # 定义了节点的性质
            self.item = item
            self.next = None
    
    class LinkList_Iterator:      # 创建迭代器类,使其可以转换为迭代器,并定义迭代器方法
        def __init__(self, node): # 这是为了使链表可以使用循环
            self.node = node

        def __next__(self):  # next方法
            if self.node:    # 若node非空,则储存原node,并更新为下一个
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item     # 最后返回原node值
            else:
                raise StopIteration
        def __iter__(self):  # iter方法,返回自己
            return self
        
    def __init__(self, iterable = None):  # 初始化定义类的参数便于后面其他方法使用它
        # 和变量定义一个意思,这里写的是需要在调用时需传入参数部分,还可以写无需传入的(get)
        self.head = None
        self.tail = None
        if iterable:           # 假如头尾节点不为空则执行
            self.extend(iterable)
    
    # 模仿列表创建相应函数
    def append(self, obj):      # 使用尾插法
        s = LinkList.Node(obj)     # 把obj作为item参数传入节点中作为值
        if not self.head:          # 初始head为空,则把插入作为头尾
            self.head = s
            self.tail = s
        else:                      # 不为空则往他后边使用尾插法
            self.tail.next = s     # 链接下一个并改链尾
            self.tail = s

    def extend(self, iterable):    # 对传入列表iterable循环执行插入append
        for obj in iterable:
            self.append(obj)
    
    def find(self, obj):           # 设定链表内for循环进行查找
        for n in self:
            if n == obj:
                return True
        else:
            return False
        
    def __iter__(self):    # 传入链表头进行迭代,前边定义的一堆为这里服务
        return self.LinkList_Iterator(self.head)
    
    def __repr__(self):    # 返回迭代器的格式
        return "<<" + ",".join(map(str, self)) + ">>"
    
# 使用拉链法定义哈希表
class HashTable:         
    def __init__(self, size = 101):
        self.size = size
        self.T = [LinkList() for _ in range(self.size)] # 相应长度下每位置都是空链表,注意linklist加()

    def h(self, k):    # 哈希函数
        return k % self.size
    
    def insert(self, k):
        i = self.h(k)    # 获取哈希值(k计算后 应放入的位置)
        if self.find(k):
            print("Duplicated insert")  # 找到了返回重复插入,这样能实现哈希去重,类似于列表
        else:
            self.T[i].append(k)         # 没找到就插入

    def find(self, k):
        i = self.h(k)              # 先获取放入位置
        return self.T[i].find(k)   # 这里是因为T的定义已经使用了linklist()实例化成对象
"""
lk = LinkList([1, 2, 3, 4, 5])   # 为 iterable参数 传入 列表 的LinkList类实例化对象
# 思路为init方法 --> extend方法 --> append方法 --> linklist的node类
for element in lk:
    print(element, end = " ")
    # 返回1 2 3 4 5 
"""
ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(102)
print(",".join(map(str, ht.T)))   # 打印出哈希表发现1和102处于同一链表中(顺序表的长度为101)
print(ht.find(102))   # 返回True