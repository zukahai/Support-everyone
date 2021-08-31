# Input  
# N = 4
# Output:
#     *
#    **
#   ***
#  ****

# Input  
# N = 6
# Output:
#       *
#      **
#     ***
#    ****
#   *****
#  ******


n = int(input("Nhập N: "))

for i in range(n):
    print(" " * (n - i), end = "")
    print("*" * (i + 1))
