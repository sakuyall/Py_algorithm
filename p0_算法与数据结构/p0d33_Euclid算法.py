"""11/23/25
欧几里得算法Euclid-最大公约数GCD
    可回顾p_50最大公因数
    gcd(a, b) = gcd(b, a mod b)
    反复为长的取短的余数
    证明略
"""
def gcd(a, b):
    if b == 0:
        return 0
    else:
        return gcd(b, a % b)

def gcd2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
# print(gcd2(12, 16))

# 实现分数计算
class Fraction:
    @staticmethod
    # 静态
    def gcd(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgs(self, a, b):
        # 最小公倍数12, 16 --> 4
        x = self.gcd(a, b)
        return a * b / x

    def __add__(self, other):
        # 3/5 + 2/7
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * fenmu / b + c * fenmu / d
        return Fraction(fenzi, fenmu)

    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    def __str__(self):
        return "%d/%d" % (self.a, self.b)

a = Fraction(1, 3)
b = Fraction(1, 2)
print(a+b)
# 返回5/6