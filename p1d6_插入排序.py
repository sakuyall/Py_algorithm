# p1-插入排序-9/25/25---------------------------------------------
"""
先将列表头两个元素顺序排列
接着每次将一个待排序的元素 取出，将其插入前面的有序序列
后面的元素向前插入过程中，跳过的元素向后 覆盖(后挪)
满足条件停止比较时该元素 覆盖当前位置(留在原处)
"""
def InsertionSort(list):
    n = len(list)
    for i in range(1, n):     # 边界固定，从第二个数开始
        x = list[i]           # 提取所选数,初始为第二个
        j = i - 1             # 与前面对比
        while j >= 0:         # 左边有数继续移动
            if x <= list[j]:
                list[j + 1] = list[j]
                j -= 1
                # 先向右覆盖，再向左判断
                # 比如此数最小，j在完成while后会变为-1，也就把插入元素放在了0位置上
            else:
                break 
                # 不小于就不动，看下一个数
        list[j + 1] = x       # 一轮结束后，提取出的数放回正确位置
        # 这两个list[j + 1]赋值可以看出，此值不是被前边覆盖，就是被插入覆盖
        # 可以优先寻找这种值构建框架
        print(list)           # 每轮冒泡完毕的可视化

a = [8, 5, 6, 4, 3, 7, 10, 2]
InsertionSort(a)
# end
# 如果用j在0,i范围内for循环迭代呢？
"""
Failed------
for i in range(1, n):
    ins = list[i]            # 提取i位置元素
    for j in range(i - 1, -1, -1):
        if ins <= list[j]:
            list[j + 1] = list[j]   # 覆盖当前位置
        # j到头了就下一个i循环
        else:
            break
    list[j + 1] = ins
"""