# def countOdd(a):
#     count = 0
#     for i in a:
#         count += i % 2
#     return count

def countOdd(a):
    return sum(1 for i in a if i % 2 == 1)

a = [1, 2, 3, 4, 5, 7]
print(countOdd(a))
