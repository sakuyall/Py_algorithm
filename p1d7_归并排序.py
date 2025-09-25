# p1-归并排序-9/25/25---------------------------------------------
def Merge(list, start, mid, end):
    tmp = []
    l = start
    r = mid + 1
    while l <= mid and r <= end:
        if list[l] <= list[r]:
            tmp.append(list[l])
            l += 1
        else:
            tmp.append(list[r])
            r += 1
    tmp.extend(list[l : mid + 1])   # 加入剩余内容，若切片反向则会加入空列表
    tmp.extend(list[r : end + 1])   # 注意，切片也是左闭右开原则,若步长为负则会返回列表
    for i in range(start, end + 1):
        list[i] = tmp[i - start]            # 深拷贝
    print(start, end, tmp)
    # 输出合并结果

def MergeSort(list, start, end):
    if start == end:                  # 递归结束条件为列表长度为1或0
        # 长度为1不做操作
        return
    mid = (start + end) // 2
    # 默认取中点扒左右两堆
    MergeSort(list, start, mid)       # 左右两边进行递归
    MergeSort(list, mid + 1, end)
    Merge(list, start, mid, end)

a = [8, 5, 6, 4, 3, 7, 10, 2]
MergeSort(a, 0, 7)