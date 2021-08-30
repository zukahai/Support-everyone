import math

x = (float)(input())

def SQRT(n):
    x, x2 = 1, 10**17
    while x != x2 :
        x = x2
        x2 = (x + n / x) / 2
    return x

print(format(SQRT(x), '.52f'))
print(format(math.sqrt(x), '.52f'))