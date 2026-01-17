"""10/15/25
计数排序可参考p1d8_计数排序
用列表进行排序,已知列表内数范围都在0-100之间,设计时间复杂度为n的算法
最简单的排序 说是
速度快但局限性很大，且消耗大量内存
"""
def CountSort(li, maxcount = 100):
    count = [0 for _ in range(maxcount + 1)]
    for val in li:
        count[val] += 1
    # 此时信息都位于count中，元素作为出现次数，索引作为元素标志
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random
li = [random.randint(0,100) for _ in range(1000)]
print(li)
CountSort(li)
print(li)
