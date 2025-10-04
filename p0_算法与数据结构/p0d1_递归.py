"""10/1/25
递归
两个特点:调用自身,结束条件
"""
def func3(x):
    if x > 0:
        print(x)
        func3(x - 1)     # 加入假如输入x为3,调用后返回321
def func4(x):
    if x > 0:
        func4(x - 1)
        print(x)         # 返回123
"""
汉诺塔问题
在 function_note4 见过面之后,再次分析:
n个圆盘时可以分为三步:
    1)把n-1个圆盘从A经过C移动到B
    2)把第n个圆盘从A移动到C
    3)把n-1个圆盘从B经过A移动到C
    可以看出1)和3)两步便是原问题范围缩小后的同等问题
"""
def hanoi(n, a, b, c):
    # 表示n个圆盘从a经b移到c
    if n > 0:
        hanoi(n - 1, a, c, b)  # 第一步
        print("moving from %s to %s" % (a, c))
        hanoi(n - 1, b, a, c)  # 第三步
hanoi(3,"a", "b", "c")
# 不懂可以n=2推演一下
# %这个东西是旧版本的字符串格式化