"""10/15/25
希尔排序(Shell Sort)是一种分组插入排序算法
1)取整数d1=n/2,假如列表长度为9,d为4
将列表分为若干层,每层元素间隔为d
[5, 7, 4, 6, 3, 1, 2, 9, 8]
            |
            V
[5,  ,  ,  , 3,  ,  ,  , 8]
[ , 7,  ,  ,  , 1,  ,  ,  ]
[ ,  , 4,  ,  ,  , 2,  ,  ]
[ ,  ,  , 6,  ,  ,  , 9,  ]
接着对每层做插入排序得到
[3, 1, 2, 6, 5, 7, 4, 9, 8]

2)第二趟取d2/2继续上述操作得到
[3, 1, 2, 6, 5, 7, 4, 9, 8]
            |
            V
[3,  , 2,  , 5,  , 4,  , 8]
[ , 1,  , 6,  , 7,  , 9,  ]
插入排序
[2, 1, 3, 6, 4, 7, 5, 9, 8]

3)第三趟直到d3=1重复操作排完
希尔排序的意义在于使整体数据逐渐接近有序，最后一趟排序实现全部有序
"""
def InsertSortGap(li, gap):    # gap作为元素之间分组
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap    # gap距离前的数
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp

def ShellSort(li):
    d = len(li) // 2
    while d >= 1:
        InsertSortGap(li, d)
        d //= 2

li = list(range(1000))
import random
random.shuffle(li)
ShellSort(li)
print(li)
"""
数据量大时速度远超过简单插入排序,但速度慢于NB三人组
该算法有许多种实现形式,时间复杂度难于计算,与gap序列选择有关
"""
