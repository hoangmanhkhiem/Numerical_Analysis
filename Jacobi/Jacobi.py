# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


# Nhập dữ liệu từ file input
# file input là ma trận cấp n x (n+1)
# trong đó n cột đầu biểu diễn ma trận A, cột cuối cùng biểu diễn vecto b

A = []
b = []
f1 = open("input.txt", "r")
data = f1.readlines()
n = sum(1 for _ in data)
f1.close()
for s in data:
        row = s.strip().split(' ')
        row1 = [float(i) for i in row]
        row2 = []
        for i in range(len(row1) - 1):
            row2.append(row1[i])
        A.append(row2)
        b.append(row1[len(row1) - 1])
print("A = ", A)
print("b = ", b)
# sai số e
eps = e = 10e-10


# Gói A
# kiểm tra điều kiện chéo trội của A
def kt(A):
    m = []
    m = [sum(abs(j) for j in r) for r in A]
    if all(2 * abs(A[i][i]) > m[i] for i in range(n)):
        return 0
    else:
        m = [sum([abs(x[i]) for x in A]) for i in range(len(A[0]))]
        if all(2 * abs(A[j][j]) > m[j] for j in range(n)):
            return 1
        else:
            return -1


# chuẩn vc của ma trận
def chuanvc(a):
    a1 = []
    for r in a:
        m = (sum(abs(i) for i in r))
        a1.append(m)
    c = max(i for i in a1)
    return c


# chuẩn 1 của ma trận
def chuan1(a):
    a1 = [sum([abs(x[i]) for x in a]) for i in range(len(a[0]))]
    m = max(abs(i) for i in a1)
    return m


# xác định loại chuẩn ma trận
def chuan(a):
    if kt(A) == 0:
        return chuanvc(a)
    else:
        if kt(A) == 1:
            return chuan1(a)
        else:
            print("error!")


# xác định loại chuẩn vecto
def chuan_vecto(v):
    if kt(A) == 0:
        return sum(abs(i) for i in v)
    if kt(A) == 1:
        return max(abs(i) for i in v)
    if kt(A) == -1:
        print("error!")


# Hiệu hai vecto
def sub(x, y):
    m = []
    for i in range(len(x)-2):
        m.append((x[i] - y[i]))
    return m


# Gói C:
# xác định ma trận B và vecto tự do
B = []
d = []


def xacdinh_b():
    for i in range(n):
        B.append([])
        for j in range(n):
            if i == j:
                B[i].append(0)
            else:
                B[i].append(-(A[i][j]) / (A[i][i]))


def xacdinh_d():
    for i in range(n):
        d.append(b[i] / A[i][i])


# lặp đơn
def lap_don(B, d, e):
    x0 = d

    # xây dựng hàm phi(x)
    def phi(B, x, d):
        m = []
        y = []
        for r in B:
            p = sum(x[i] * r[i] for i in range(n))
            m.append(p)
        for i in range(n):
            y.append(m[i] + d[i])
        return y

    xk = phi(B, x0, d)
    dem = 0
    while chuan_vecto(sub(x0, xk)) > e:
        x0 = xk
        xk = phi(B, x0, d)
        dem = dem + 1
    print("Số bước lặp: ", dem)
    print("Nghiem của hệ phương trình là: ", xk)
    return xk


def kiemtra(sol):
    m = []
    t = []
    for r in A:
        p = sum(sol[i] * r[i] for i in range(n))
        m.append(p)
    for i in range(n):
        t.append(m[i] - b[i])
    return t


# main
# Bước 1: Kiểm tra A
def main():
    if kt(A) == -1:
        print("Ma trận A không phải ma trận chéo trội.")
    else:
        if kt(A) == 0:
            print("A là ma trận chéo trội hàng")
            xacdinh_d()
            xacdinh_b()
            eps = e * (1 - chuan(B)) / (chuan(B))
            print("chuan(B) = ", chuan(B))
        if kt(A) == 1:
            print("A là ma trận chéo trội cột")
            xacdinh_d()
            xacdinh_b()
            chuanT = max(abs(1 / A[i][i]) for i in range(n))
            chuanD = max(abs(A[i][i]) for i in range(n))
            chuan_B1 = max([sum([abs(x[j] / A[j][j]) for x in A]) for j in range(n)]) - 1
            eps = e * (1 - chuan_B1) / (chuan_B1 * chuanT * chuanD)
            print("chuan(B1) = ", chuan_B1)
        # Bước 2: lặp đơn
        nghiem = lap_don(B, d, eps)

        # Kiểm tra tính đúng đắn của thuật toán
        print("kiểm tra tính đúng đắn của thuật toán: ")
        print("Ax* - b = ", kiemtra(nghiem))


if __name__ == '__main__':
    main()


