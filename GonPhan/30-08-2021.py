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


#################################
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


#########################
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 1
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
        size = size + 1
    
print(b)

#################################
bài tập liên quan về đếm 
""" [[1],[2], [3,4] ,[5,6] , [7,8,9], [8,9,10]]"""
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
size =1
dem_size =0 #biến đém 
index = 0 # biến đếm 
b=[]
for i in range(len(a)):
    if index ==0:
        c =[] 
    c.append(a[i]) 
    index = index +1 
    if index ==size:
        
        b.append(c)
        dem_size = dem_size +1    
        if dem_size%2==0:
           size = size +1
        index =0
print(b)   

