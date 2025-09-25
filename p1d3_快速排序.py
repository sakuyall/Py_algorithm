# 方法四：二叉树方法----------------------------------------------------
"""
通过比基准数小的数左移
"""
def QuickSortPrivate(a, start, end):
    privot = start        # 设定标准值为第一个数
    j = start + 1
    for i in range(start + 1, end + 1):  # 左闭右开
        if a[i] <= a[privot]:
            a[i], a[j] = a[j], a[i]
            j += 1                       # 若i位置数小于初始值，j往后走使j前全小于初始值
        a[privot], a[j - 1] = a[j - 1], a[privot]
        privot = j - 1
        print(a[privot], a[start:privot], a[privot + 1, end + 1])
    return privot

def QuickSort(a, start, end):
    if start >= end:
        return
    privot = QuickSortPrivate(a, start, end)
    QuickSort(a, start, privot - 1)
    QuickSort(a, privot + 1, end)

a = [8, 5, 12, 6, 4, 3, 7, 9, 2, 1, 10, 11]
QuickSort(a, 0, 11)
print(a)