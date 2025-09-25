# p1-冒泡排序-9/25/25---------------------------------------------
def BubbleSort(list):
    n = len(list)
    time = 0
    for i in range(n - 1, -1, -1):   # 反向循环n-1指向0位置(注意左闭右开)
        # 这一步是限制了下面j取值的右边界
        for j in range(i):           # 初始i表示最后一位
            if list[j] > list[j + 1]:
                # 若前者大于后者，则交换
                list[j], list[j + 1] = list[j + 1], list[j]
            # 不满足判断条件则j继续通过for循环,将此次阻挡的下一个大数往右推
        print(list)                  # 每轮冒泡完毕的可视化

a = [8, 5, 6, 4, 3, 7, 10, 2]
BubbleSort(a)