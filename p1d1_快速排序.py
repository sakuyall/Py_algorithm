# 方法二：区间调整，空间换时间---------------------------------------
"""
设定三个额外序列abc用于存放
选取分界点并扫描原始序列,小于放a 等于放b 大于放c
小区间继续建立三个新数组,递归终止条件为区间长度为1或0
"""
def quick_sort(list):
    if len(list) == 1 or len(list) == 0:
        return list        # 特殊情况，输入长度为1或空列表直接返回
    
    x = list[len(list) // 2]  # 默认取中间数值作为分界点，应对数据增强情况
    a = []
    b = []
    c = []
    for i in list:
        if i < x:
            a.append(i) # 小于分界点 
        elif i == x:
            b.append(i) # 等于分界点
        else:
            c.append(i) # 大于分界点
    return quick_sort(a) + b + quick_sort(c) # ac递归,b就算有多个也不用排序

q = list(map(int,input("比如输入3 1 2 4 5\n").split())) # 默认空格分割
print(q)
q = quick_sort(q)
for i in q:
    print(i, end=",")
