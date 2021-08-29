"""bài 1
inpt a=[1,2,3]
output 1 2 3"""
# a =[1,2,3]
# for i in a:
#     print(i, end=" ")# end là ngăn xuống dòng .. range là khi khi các chỉ số ,,


"""N=3
output
*
**
***
****
"""
n = int(input("nhạp n :"))
for i in range(1,n+1):
    for item in range(i):
        print("*",end="")
    print()
 
#######################

n = int(input("Nhập N: "))
for i in range(1, n + 1):
    print("*" * i)
    
  bài toán ngược
n = int(input("Nhập N: "))
for i in range(n, 0,-1):
    print("*" * i)

