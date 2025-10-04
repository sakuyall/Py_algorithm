# p2-简单模拟-9/30/25---------------------------------------------
"""
第三部分:坐标系两点间距离
    某国部署了两套导弹拦截系统,工作半径为R1R2,设计成本为工作半径的平方和
导弹位置分别为(-4,-2)(-2,3)(4,0)(6,-2)(9,1),系统分别位于(0,0)(6,0)
如何用最低成本拦截所有导弹

考虑计算出每个系统拦截全部导弹情况，并将两个集合于一起判断寻找最优组合
优化:对系统一导弹距离进行排序,一号剩余的留给二号,从而剩余距离二号最远的便是二号半径,进而寻找最优组合
优化的目的便是去掉部分循环
"""
import math
# 半径测量
def Route1(a, b):
    c1 = a * a + b * b
    # d1 = math.sqrt(c1)
    return c1
def Route2(a, b):
    c2 = (a - 6) * (a - 6) + b * b
    # d2 = math.sqrt(c2)
    return c2

# 冒泡排序，直接调用sort接口就可以了
def BubbleSort(list):
    n = len(list)
    for i in range(n, -1, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        print(list)

lr1 = [Route1(-4,-2), Route1(-2,3), Route1(4,0), Route1(6,-2), Route1(9,1)]
lr2 = [Route2(-4,-2), Route2(-2,3), Route2(4,0), Route2(6,-2), Route2(9,1)]
print(lr1, lr2)
# 对基地一的距离表进行排序选择拦截距离，循环求出该排序下剩余导弹到基地二最大距离，最后判断方案最小值
zipped = list(zip(lr1, lr2))
# zipped选取两列表对应位置打包为元组并组成一个列表，返回内容为一个可迭代对象需用list()展开
print(zipped)
# 返回[(20, 104), (13, 73), (16, 4), (40, 4), (82, 10)]
DoubleList = sorted(zipped, key=lambda x:x[0])
print(DoubleList)
# 返回[(13, 73), (16, 4), (20, 104), (40, 4), (82, 10)]

unzipped = zip(*DoubleList)
lr1, lr2 = [list(i) for i in unzipped]
print(lr2)
# 返回[73, 4, 104, 4, 10]取出第二个列表

# 然后取一列中i以及二列中剩余最小值相加即为成本内容
results = []
for j in range(len(DoubleList) - 1):  # 不用选到最后一个
    first = DoubleList[j][0]
    second = max(lr2[j + 1 : len(lr2)])
    result = first + second
    results.append(result)

print(f"成本的最小值为{min(results)}")

# lambda表达式的使用见 function_note4 或 p_39 一节