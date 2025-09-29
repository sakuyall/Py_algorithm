# p1-计数排序-9/29/25---------------------------------------------
"""
缺点是哈希表的设定
另外设定一个计数器数组比如1-n,遍历原序列,对应位置计数器加一
最后按照计数器内同一元素次数输出
经典的空间换时间
索引太多了
"""
def CountingSort(list):
    n = len(list)
    cntlen = max(list) + 1    # 哈希表长度
    cnt = [0] * cntlen        # 建立哈希表cnt
    # 比如对于1与100两个数，会设定101个位置，索引为0-100
    for val in list:          # 从头开始遍历每一个数
        cnt[val] += 1         # 遍历到100就在cnt[100]索引处加1
    print(cnt)
    n = 0
    for val in range(0, cntlen):
        while cnt[val] > 0:   # 还有数就一直取
            list[n] = val     # 普通的赋值
            cnt[val] -= 1     # 计数作用
            n += 1            # 指向下一个list空位

a = [8, 5, 6, 4, 3, 7, 10, 2]
CountingSort(a)
print(a)
# fin