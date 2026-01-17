"""10/2/25
查找
    内置列表查找函数:index()
    对于查找算法,输入一般为 列表 待查找元素;输出一般为 元素下标
    无结果返回None或-1
"""
# 顺序查找(Linear Search)
def LinearSearch(li, val):
    for ind, v in enumerate(li):
        # enumerate函数将可迭代对象转化为具有索引的元组
        if v == val:
            return ind
    else:
        # 这里直接return就可以,此else对应的是for,是一种pythonic的写法
        return

# 二分查找(Binary Search)
# 排序后一半一半查找,减少了查找次数
def BinarySearch(li, search):
    left = 0
    right = len(li) - 1
    while left <= right:
        # 若候选区仍有值
        mid = (left + right) // 2
        if li[mid] == search:
            # 如果找到search了直接返回下标
            return mid
        elif li[mid] > search:
            # search在左边,右半区域舍去
            right = mid - 1
        else:
            # search在右边
            left = mid + 1
    # 还有找不到的情况
    else:
        return None
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(BinarySearch(li, 3))
# 由于循环在不断减半,所以复杂度为logn
# 复习装饰器看看
