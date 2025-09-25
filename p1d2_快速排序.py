# 方法三：双指针方法----------------------------------------------------
"""
设定两个指针分别在原始序列两侧往中间移送
若左侧小于分界点,右侧大于分界点则ij移动
接着判断i与j是否相遇(位于同一元素处),未相遇则交换ij索引的元素,都向中间走一步
再次走到无法前进,此时以ji分界,形成了左右两个小区间，接着递归
"""
def quick_sort(list, left, right):
    """列表名称，左边界，右边界"""
    if left == right:     # 长度为1直接返回
        return
    i, j = left - 1, right + 1     # 由于最后要往中间走一步，所以初始位置往外扩一步
    x = list[(left + right) // 2]  # 中间值为锚点
    while i < j:
        while True:                # 依次对ij进行移动
            i += 1
            if list[i] >= x:
                break              # 不能动了就退出i的判断，执行j移动
        while True:
            j -= 1
            if list[j] <= x:
                break
            
        if i < j:
            list[i], list[j] = list[j], list[i]   # 如果仍未相遇则交换位置
    quick_sort(list, left, j)
    quick_sort(list, j+1 , right)

q = list(map(int,input("比如输入3 1 2 4 5\n").split())) # 默认空格分割
print(q)
quick_sort(q, 0, len(q)-1)
for i in q:
    print(i, end=",")
