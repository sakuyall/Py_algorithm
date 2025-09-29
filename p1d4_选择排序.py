# p1-选择排序-9/25/25---------------------------------------------
"""
依次选出序列中最小数值放入正确位置,注意最后一个数无需对比,如果考虑速度的话
"""
def SelectionSort(list):
    for i in range(len(list) - 1):          # 左往右左减少的边界，n-1是由于最后一个无需对比
        min = i                             # 预设第一个数为最小序号
        for j in range(i + 1, len(list)):   # 选一个数，后边所有与它对比，覆盖出最小值
            if list[j] < list[min]:
                min = j                     # 找出更小值覆盖序号
        list[min], list[i] = list[i], list[min] 
        # 循环结束,将i位置数与遍历最小值交换，并接着从下一位开始循环
        print(list)                         # 每轮排列完毕的可视化

a = [8, 5, 6, 4, 3, 7, 10, 2]
SelectionSort(a)
# 先确定边界再进行遍历，左边减少不用特意设定反序
# fin