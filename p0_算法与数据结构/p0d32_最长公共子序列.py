"""11/22/25
最长公共子序列(LCS)
    子序列顺序确保与原先一致,无需一定连续如"BDF"是ABCDEFG的子序列,空串也算子序列
    应用场景:字符相似度比对,模糊查找
    其他拓展可参考p55_最长公共前缀

暴力穷举
    对于一个长度为m和n的序列,找最长公共子序列复杂度需要2^(m+n)

动态规划
    课程中96节的图比较直观,可以类比为迷宫问题,最后值不相等就往上格子或左格子走
    例如:求取a="ABCBDAB"与b="BDCABA"的LCS
    由于ab最后一位不相同,则可确定ab的LCS是 a去掉尾巴与b的LCS 或 b去掉尾巴与a的LCS
    从表格左上角开始求解子问题,不断向右下角扩充,遇到匹配情况就将LCS值加1,初始值为0

递推式
                0                               if i = 0 or j = 0
    c[i, j] =   c[i - 1, j - 1] + 1             if i, j > 0 and xi = yi
                max(c[i, j - 1], c[i - 1, j])   if i, j > 0 and xi != yi
"""
def lcs_length(x, y):
    # x, y都是字符串,列表也行
    m = len(x)
    n = len(y)
    # 建立二维列表
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:# 这是由于列表是从0开始编号
                # ij位置字符匹配的时候,来自于左上方加1
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                # 不匹配时,来自于左方和上方最大的
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    for _ in c:
        print(_)
    return c[m][n]

def lcs(x, y):
    # 同时使用二维列表b记录路径
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # b用于记录箭头方向,确定1为左上,2为上,3为左,0默认填充
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1  # 左上 赋值为 1
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2  # 上 赋值为 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3  # 左 赋值为 3\
    for _ in c:
        print(_)
    for _ in b: 
        print(_)
    return c[m][n], b

def lcs_traceback(x, y):
    # 回溯算法
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(res))

print(lcs_length("ABCBDAB", "BDCABA"))
# 返回4