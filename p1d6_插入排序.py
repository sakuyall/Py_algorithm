# p1-插入排序-9/25/25---------------------------------------------
def InsertionSort(list):
    n = len(list)
    for i in range(1, n):
        x = list[i]           # 提取所选数,初始为第二个
        j = i - 1             # j也随着x自增
        while j >= 0:         # 左边有数继续移动，
            if x <= list[j]:
                list[j + 1] = list[j]
                # 类似于三个数交换，实现了j位置数右移
                j -= 1        # j继续向左遍历
            else:
                break 
                # 不小于就不动，看下一个数
        list[j + 1] = x       # 一轮结束后，提取出的数放回正确位置
        print(list)                  # 每轮冒泡完毕的可视化

a = [8, 5, 6, 4, 3, 7, 10, 2]
InsertionSort(a)