pt = []
b = []

n = 0
m = 0

a = []
hs = []

s = []
mp = []


# Hàm tìm ước chung lớn nhất của hai số
def ucln(a1, a2):
    if a1 * a2 == 0:
        return a1+a2
    while a1 % a2 != 0:
        tmp = a1 % a2
        a1 = a2
        a2 = tmp
    return a2

# Hàm nhân hàng row trong ma trận a lên k lần


def mul(row, k):
    for i in range(n):
        a[row][i] *= k

# Hàm trừ 2 hàng trong ma trận a: row1 = row1 - row2


def sub(row1, row2):
    for i in range(n):
        a[row1][i] -= a[row2][i]


# Hàm hoán đổi 2 hàng với nhau
def swap(row1, row2):
    for i in range(n):
        tmp = a[row1][i]
        a[row1][i] = a[row2][i]
        a[row2][i] = tmp

# Hàm rút gọn ma trận a


def rutgon():
    for i in range(m):
        for j in range(n):
            if a[i][j] != 0:
                k = a[i][j]
                break
        for j in range(n):
            if a[i][j] != 0:
                k = ucln(k, a[i][j])
        for j in range(n):
            a[i][j] //= k

# Hàm biến đổi ma trận a về ma trận đường chéo


def biendoi():
    k1 = 1
    k2 = 1
    for i in range(n-1):
        k = m-1
        while a[k][i] == 0:
            k -= 1
        for j in range(k-1, i-1, -1):
            if a[j][i] == 0:
                swap(j, k)
                k -= 1
        for j in range(m-1, i, -1):
            if a[j][i] != 0:
                k1 = a[j][i]
                k2 = a[i][i]
                mul(i, k1)
                mul(j, k2)
                sub(j, i)
    rutgon()

    for i in range(n-2):
        for j in range(i+1, n-1):
            if a[i][j] != 0:
                k1 = a[j][j]
                k2 = a[i][j]
                mul(i, k1)
                mul(j, k2)
                sub(i, j)
    rutgon()


# Hàm tìm các hệ số cân bằng của phương trình hóa học
# Trả về biến hs
def canbang():
    k3 = 1
    for i in range(n-1):
        k3 *= a[i][i]
    for i in range(n-1):
        hs.append(k3*a[i][n-1]//a[i][i])
    hs.append(k3)
    k3 = hs[0]
    for i in range(n):
        k3 = ucln(k3, hs[i])
    for i in range(n):
        hs[i] = abs(hs[i]//k3)

# Hàm xuất ma trận a ra màn hình


def show():
    for i in a:
        print(i)
    print("------------------")

# Hàm in phương trình hóa học đã cân bằng ra màn hình


def ketqua():
    print()
    print("Phuong trinh hoa hoc da can bang:")
    print()
    equal = b.index(-1)
    for i in range(0, n):
        if hs[i] > 1:
            print(hs[i], end="")
        print(pt[i], end=" ")
        if i == equal-1:
            print("=", end=" ")
        elif i != n-1:
            print("+", end=" ")
        else:
            print()

# Hàm tách các phân tử và hệ số ban đầu từ phương trình hóa học
# Trả về biến pt và b


def get_pt(str):
    str = str + "+"
    global n
    global m
    n = 0
    k = 1
    S = ""
    for i in range(len(str)):
        if str[i] == " ":
            continue
        if str[i] == "+":
            b.append(k)
            pt.append(S)
            n += 1
            S = ""
        elif str[i] == "=":
            b.append(k)
            pt.append(S)
            n += 1
            S = ""
            k = -1
        else:
            S = S+str[i]

# Hàm tạo ma trận a


def get_a():
    global n
    global m
    nt = ""
    lst = {}
    for v in range(n):
        k = 1
        nt = ""
        tmp = 0
        i = len(pt[v])-1
        while i >= 0:
            if pt[v][i] >= "0" and pt[v][i] <= "9":
                if k == 1 and pt[v].find("(") < len(pt[v]) and pt[v].find("(") >= 0:
                    k = int(pt[v][i])
                else:
                    t = 1
                    k2 = 0
                    while pt[v][i] >= "0" and pt[v][i] <= "9":
                        k2 += t*int(pt[v][i])
                        t *= 10
                        i -= 1
                    while pt[v][i] >= "a" and pt[v][i] <= "z":
                        nt = pt[v][i]+nt
                        i -= 1
                    nt = pt[v][i]+nt
                    lst[nt] = k*k2*b[v]
                    tmp += k*k2*b[v]
                    nt = ""
            elif pt[v][i] >= "a" and pt[v][i] <= "z":
                while pt[v][i] >= "a" and pt[v][i] <= "z":
                    nt = pt[v][i]+nt
                    i -= 1
                nt = pt[v][i] + nt
                lst[nt] = k*b[v]
                tmp += k*b[v]
                nt = ""
            elif pt[v][i] >= "A" and pt[v][i] <= "Z":
                nt = pt[v][i]+nt
                lst[nt] = k*b[v]
                tmp = k*b[v]
                nt = ""
            elif pt[v][i] == "(":
                k = 1
            i -= 1
        mp.append(lst)
        lst = {}

    check = []
    pt1 = []
    for i in range(n):
        for item in mp[i]:
            if item in check:
                pass
            else:
                for j in range(n):
                    if mp[j].get(item) == None:
                        hs1 = 0
                    else:
                        hs1 = mp[j].get(item)
                    pt1.append(hs1)
                check.append(item)
                a.append(pt1)
                pt1 = []
    m = len(a)


# Chương trình chính
print("Nhap vao phuong trinh hoa hoc:")
ptr = input()
get_pt(ptr)
get_a()
biendoi()
canbang()
ketqua()
input()
