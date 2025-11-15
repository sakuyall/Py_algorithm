"""11/15/25
背包问题
    一个小偷在商店发现n个商品,第i个商品价值vi元,重wi千克
    他希望拿走的价值尽量高,但背包最多能容纳W千克东西,如何实现利益最大化
    分为 0-1背包(同一个东西只能选择拿走或放下) 与 分数背包(同一个东西可以只拿走一部分)

举例
    商品1   v1=60   w1=10
    商品2   v2=100  w2=20
    商品3   v3=120  w3=30
    容量    W=50

    0-1背包判断性价比优先,拿1和2价值160
"""
# 分数背包
goods = [(60, 10), (100, 20), (120, 30)]   # 价格与重量

def fractional_backpack(goods, W):
    # 选取性价比最高优先排序
    goods.sort(key = lambda x: x[0]/x[1], reverse = True)   # 定义匿名x返回:后内容,降序开
    m = [0 for _ in range(len(goods))]                # 每个商品拿了多少]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if W >= weight:
            m[i] = 1   # 全拿走了
            W -= weight
            total_v += prize
        else:
            m[i] = W / weight   # 拿了分数
            W = 0      # 装满
            total_v += m[i] * prize
            break
    return m, total_v  # 返回的是排序后的顺序
    
print(fractional_backpack(goods, 50))
# 返回([1, 1, 0.6666666666666666], 240.0)