"""10/4/25
排序
    快速排序代码可参照p1d2&3
    冒泡排序代码可参照p1d5
    选择排序代码可参照p1d4
    插入排序代码可参照p1d6
快速排序
快速排序思路分为:
1)任意取一个元素p使其归位
2)列表被p分为两部分,左边都比p小,右边都比p大(双指针挖坑填坑法可参考视频p17快排原理)
3)对子列表进行以上两操作完成排序(递归的结束条件为列表元素数0或1)
"""

def Partition(li, left, right):  # 这一部分仍然是双指针思想的详细讲解
    # 列表,左右边界
    tmp = li[left]     # 这里选取列表第一个元素(也可选取随机元素)取出用于接下来的对比
    # 这里存在一个问题,若选取中间元素,那么第一步(仅第一步)移位就必须移到空缺处而不是右边
    # 接下来另外的例程将展示这一问题
    # 终止条件设定为左右指针重合,因此里边的两个小循环也要判断指针是否重合
    while left < right:
        # 可以思考一下为什么先找右边--其实是因为空在最左边方便放过去
        while left < right and li[right] >= tmp:    # 从右边开始找比tmp小的数放到左边
            right -= 1            # 随后往左走一位
        li[left] = li[right]      # 把右边的值写到左边空位上
        # 接着对左边操作
        while left < right and li[left] <= tmp:
            left += 1             # 随后往右走一位
        li[right] = li[left]      # 把左边的值写到右边空位上
    # 循环结束后,最后的重合时的空位放入提取出来的元素
    li[left] = tmp
    # 最后返回中间指针
    return left
def QuickSort(li, left, right):
    if left < right:
        # 至少两个元素时执行递归
        mid = Partition(li, left, right)
        QuickSort(li, left, mid - 1)
        QuickSort(li, mid + 1, right)

li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
QuickSort(li, 0, len(li) - 1)
print(li)

# 修改选取中间tmp的失败复现
# 待寻找合适的解决方法
def Partition(li, left, right):
    middle = (left + right) // 2  # <------------
    tmp = li[middle]
    while left < right:
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
    li[left] = tmp
    return left
def QuickSort(li, left, right):
    if left < right:
        mid = Partition(li, left, right)
        QuickSort(li, left, mid - 1)
        QuickSort(li, mid + 1, right)

li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
QuickSort(li, 0, len(li) - 1)
print(li)   # 返回了[2, 2, 3, 3, 4, 4, 4, 7, 9]列表有误
