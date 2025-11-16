"""11/16/25
数字拼接
    有n个非负整数,按照字符串拼接的方式拼为一个整数,使得到整数最大
    字符串的比较通过比较相同位置的大小实现
    也可以比较拼接 前拼后 与 后拼前 两者大小来判断如何获得最大值

案例
    32, 94, 128, 1286, 6, 71拼接最大整数为94716321286128
"""
from functools import cmp_to_key
# 这个东西继承了python2中sort方法的cmp参数,将此函数套用进key实现cmp方法
# cmp=的输入内容为一个两参数函数,返回两者比较结果+-1,接下来会定义出这个比较函数
# 可参考这里https://www.runoob.com/python/func-number-cmp.html
def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_join(li):
    li = list(map(str, li))
    li.sort(key = cmp_to_key(xy_cmp))   # 此处也可以用冒泡排序实现
    return "".join(li)

li = [32, 94, 128, 1286, 6, 71]
print(number_join(li))
# 返回94716321286128