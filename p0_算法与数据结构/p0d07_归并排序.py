"""10/14/25
此部分内容可参考先前的p1d7_归并排序

一次合并
    如列表为[2, 5, 7, 8, 9, 1, 3, 4, 6]这样一个 分段有序列表
    思路：依次遍历两列表，每次输出小值，随后该边索引后移
    当一边列表为空时，将剩余直接加入
"""
def merge(li, low, mid, high):
    # 分为low-mid以及mid+1-high两段
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        # 只要左右两边均有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行结束有一边没有数了
    # 分别判断那边还有，有就加入
    # 其实也可以用extend
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    # 再把这个tmp写回原本的li列表
    li[low: high + 1] = ltmp
"""
一次递归
可以拆分为三步：
    1)分解：将列表越分越小，直至分为一个元素
    2)终止条件：长度为1的列表是有序的,即只剩一个或零个元素列表
    3)合并：将两个有序列表合并使列表越来越大
"""
def MergeSort(li, low, high):
    if low < high:       # 终止条件
        # 还是分三步，归并左边归并右边以及合并
        mid = (low + high) // 2
        MergeSort(li, low, mid)
        MergeSort(li, mid + 1, high)
        merge(li, low, mid, high)
# 结束条件-基本顺序-交给子程序解决

li = list(range(1000))
import random
random.shuffle(li)
print(li)
MergeSort(li, 0, len(li) - 1)
print(li)
"""10/15/25
归并排序时间复杂度
    不考虑递归过程,合并每层把列表遍历一次时间复杂度为n
    总共层数为logn层,因此时间复杂度为nlogn
    此外空间复杂度为n(额外申请了一维列表空间n,递归的logn从而省略)
    python内部sort接口就基于归并排序与插入排序的结合

NB三人组总结
    时间复杂度均为nlogn,一般而言在实际应用中快排最快,堆排最慢(n常数上的差异)
    各自的问题有:
    快速排序极端情况下效率低,复杂度会退化为n^2,注意由于快速排序用到了递归(递归开栈占用内存logn层)
    归并排序不是原地排序(建立新列表),需要额外的内存开销
    堆排序在这里比较慢
"""
