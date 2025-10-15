"""10/13/25 [困难]
堆排序的过程见p23过程演示
    1)建立一个堆
    从后往前依次调整最后一个非叶子节点子树
    也就是从后往前依次找小三角形624这种小三角形排好
                9
            8       7
          6   5   0   1
        2  4 3
    还是以这个为例
    2)拿出根节点9,把最后一个放到根处
                3
            8       7
          6   5   0   1
        2  4 
    3)进行堆的向下调整得到
                8
            6       7
          4   5   0   1
        2  3 
    4)重复2)3)步骤直到堆变空

向下调整函数的实现"""
def sift(li, low, high):
    # 列表，列表第一个元素，最后一个元素
    i = low            # 初始指向根节点(之后一直作为父节点)
    j = 2 * i + 1      # i位置的左子节点
    tmp = li[low]
    # 取出根节点(堆顶)与其子节点比较进行调整
    # 当索引j大于high时，说明i已位于最后一层，此时超限不再循环
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            # 比较左右子节点大小，并将j指向更大者，不过前提是右子节点存在(已加入判断)
            j = j + 1
        if li[j] > tmp:
            # 就将子节点上移
            li[i] = li[j]
            # 接着ij全部下移一层
            i = j
            j = 2 * i + 1
        else:
            # tmp更大的情况，把tmp放在新i位置就结束了
            li[i] = tmp  # 这句可以不写，留在while结束后放入也可以
            # 这里没有删掉是便于看懂的缘故
            break
    # 此时跳出while循环若在最后一层，j大于high了，仍要把tmp放入
    else:
        li[i] = tmp

"""
使用sift函数实现堆排序
    1)首先建立一个堆
    从子节点往前找父节点(找的便是5, 6, 7, 8, 9这几个节点)
                9
            8       7
          6   5   0   1
        2  4 3(hi) (j)

    68行调用sift函数:这里示意的是最后位置hi与新j位置演示
    还是以这个为例
    比如列表长度为n,最后一个索引便是i = n-1
    其父节点为(i-1)//2, 也就是(n-2)//2, 或者说n//2-1这个说法
"""
def HeapSort(li):
    n = len(li)
    for i in range((n - 1)//2, -1, -1):
        # i就代表了需要调整部分的根的下标
        sift(li, i, n - 1)
        # 在这一点，对于high参数的选取，先前sift函数high的意义在于使i到达最后一行及时跳出循环
        # 此小三角形最后一数可以写为2i+2，即j大于high时结束循环
        # 此时的j位置同时也会大于列表最后一数
        # 从而使用n-1作为high来节省计算
    # 堆建立完成，接着挨个出数，此时堆顶为最大值
    # 接着拿出堆顶元素与最后一数交换位置(节省空间)，并继续重新向下调整
    for i in range(n - 1, -1, -1):
        # i指向当前堆的最后一个元素，并先做交换再做调整
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)
        # 此时最后一个元素已经交换，因此堆的high应设定为i-1位置
        
li = [i for i in range(100)]
import random
random.shuffle(li)

HeapSort(li)
print(li)
"""
堆排序的时间复杂度：
其中sift函数仅走一个树的高度，因从复杂度为logn
排序过程中每一个for循环中调用一次sift函数
分别为n/2logn以及nlogn，放在一起仍然是O(nlogn)
时间复杂度上与快速排序相同，但在应用中仍然快速排序更快
"""
# 堆排序在python中有内置模块 调用heapq接口
import heapq            # q-->queue  优先队列(人为设定小的或者大的先出)
import random

li = list(range(100))
random.shuffle(li)
heapq.heapify(li)     # 建立一个小根堆

n = len(li)
for i in range(n):
    print(heapq.heappop(li), end = ",")
    # 取出列表内最小元素