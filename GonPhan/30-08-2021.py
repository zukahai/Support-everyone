# Cau A:
#     Imput: a = [1, 2, 3, 4, 5]
#     Output: 5 4 3 2 1
# Cau B:
#     Input a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     OutPut [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

#       Câu C:Tính tổng các phần tử trong mảng 2 chiều:
#       Input a = [[1], [2, 3], [4], [1, 1, 1]]
#       Output: 13


câu a
a=[1,5,2,4,3,6]
a.sort()
print(a)
a.sort(reverse=True)
print(a)



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 2
print(a)

b = []
index = 0
for i in range(len(a)):
    if index == 0:
        c = []
    
    c.append(a[i])
    index = index + 1
    if index == size:
        b.append(c)
        index = 0
    
print(b)
