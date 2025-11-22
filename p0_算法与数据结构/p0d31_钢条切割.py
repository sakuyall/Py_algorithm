"""11/19-22/25
钢条切割问题
    某公司出售钢条,长度与价格关系如下
    长度i 1 2 3 4  5  6  7  8  9  10
    价格p 1 5 8 9  10 17 17 20 24 30
    最优u 1 5 8 10 13 17 18 22 25 30
    现有一段长度为n的钢条,求切割钢条方案使总收益最大

分析
    从1开始逐个确定每种长度最优价值
    避免子问题重复计算,后续只考虑前面哪两种相加最大

递推式
    r(n) = max{p(n), r(1)+r(n-1), r(2)+r(n-2),…,r(n-2)+r(2), r(n-1)+r(1)}
    p(n)表示不切割,其他表示n-1种切割方案,切割为i和n-i两段
    方案i的收益为切割两段最优收益之和,考察所有i选择其中最大收益方案
    分为两段后,左端长度为i不再进行切割,只对右侧剩下一段切割
    则可简化为r(n) = max(pi + r(n-1))
"""
# 自顶向下递归实现n -> n-1 -> n-2...
# 时间复杂度为O(2^n)
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# 下标代表几米的钢条
def cut_rod_recurision(p, n):
    if n == 0:    # 终止条件
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            # 按照公式写
            res = max(res, cut_rod_recurision(p, i) + cut_rod_recurision(p, n-i))  
        return res

def cl(p, n):
    return cut_rod_recurision(p, n)

def cut_rod_recurision_2(p, n):
    if n == 0:
        return 0
    else:
        # 简化公式
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recurision_2(p, n - i))
        return res

print(cut_rod_recurision(p, 9))
print(cut_rod_recurision_2(p, 9))
# 两个公式均返回25
"""
钢条切割-自底向上动态规划
    依然使用式子r(n) = max(pi + r(n-1))
    时间复杂度O(n^2)
"""
def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 2):
        res = 0
        for j in range(1, n + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]

"""
钢条切割问题-重构解
如何修改动态规划算法,使其不仅输出最优解,还输出最优切割方案
对每个子问题保留切割一次时左边切下的长度
"""
def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0        # 价格最大值
        res_s = 0        # 价格最大值对应方案的左边不切割部分长度
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s

def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans

r, s = cut_rod_extend(p, 10)
print(s)
# 需积累动态规划题目