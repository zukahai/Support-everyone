import math

x = (float)(input())

def SQRT(n):
    l, r, mid, int_Sqrt, sqrt_temp = 0, 10**9, 0, 123, 0
    while l < r:
        mid = (l + r + 1) // 2
        if mid * mid < n:
            l = mid
        else:
            r = mid - 1
    int_Sqrt = l
    if int_Sqrt * int_Sqrt == n:
        return int_Sqrt
    l, r = 0, 10**17 - 1
    while l < r:
        mid = (l + r) // 2
        sqrt_temp = int_Sqrt + mid / 10**17
        if sqrt_temp * sqrt_temp < n:
            l = mid + 1
        else:
            r = mid
    sqrt_temp = int_Sqrt + l / 10**17
    return sqrt_temp

print(format(SQRT(x), '.52f'))
print(format(math.sqrt(x), '.52f'))
print(2**30)