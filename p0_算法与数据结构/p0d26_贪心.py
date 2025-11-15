"""11/15/25
贪心算法引入
    做出当前最好情况,获取局部最优解
    接下来直到动态规划前都是贪心问题的内容
"""
# 找零问题
# 找零n元钱,面额有100,50,20,5,1,使找零所需纸币数量最少
t = [100, 50, 20, 5, 1]
def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):    # 返回索引,内容
        m[i] = n // money
        n = n % money
    return m, n   # 返回张数,剩余未找开金额

print(change(t, 376))