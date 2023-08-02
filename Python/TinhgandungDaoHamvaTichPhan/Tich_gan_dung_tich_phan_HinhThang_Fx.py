# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


from sympy import *
import math
import numpy as np
_Max = 100
def F(x):
    return x*x*math.exp(x)/(5*x*x+10)
# es = 0.5e-7

#hàm tính GTLN của hàm số trong một khoảng [a,b]
def max_f(a, b, f):
    my_list = [limit(f, x, a), limit(f, x, b)]
    L = solve(f.diff(x), x)
    if L != []:
        for i in range (len(L)):
            if a <= L[i] <= b:
                my_list.append(limit(f, x, L[i]))
    return max(my_list)

# Max_2 = 0
# Max_4 = 0
# x = Symbol('x')
# f = F(x)
# for i in range(2):
#     f = f.diff(x)
# print("Đạo hàm cấp 2 của hàm số: ",f)
# Max_2 = max_f(a, b, f)
# print("Giá trị lớn nhất của đạo hàm cấp 2:", Max_2)
# for i in range(2):
#     f = f.diff(x)
# print("Đạo hàm cấp 4 của hàm số: ",f)
# Max_4 = max_f(a, b, f)
# print("Giá trị lớn nhất của đạo hàm cấp 4:", Max_4)


X1 = []
Y1 = []
def TTPHinhThang(a,b,n):
    h = (b-a)/n
    for i in range (n+1):
        X1.append(a + i * h)
        Y1.append(F(a + i * h))
    ans = sum(Y1[i] if i in [0, n] else 2 * Y1[i] for i in range(n+1))
    return h / 2 * ans


X2 = []
Y2 = []
#PP Simpson
def TTPSimpson(a,b,m):
    # if m == 0:
    #     m = _Max
    ans = 0
    h = (b - a) / m
    for i in range (m+1):
        X2.append(a+ i * h)
        Y2.append(F(a + i * h))
    for i in range(m+1):
        if i in [0, m]:
            ans += Y2[i]
        elif i % 2 == 1:
           ans += 4 * Y2[i]
        else:
            ans += 2 * Y2[i]
    return h / 3 * ans

def main():
    a = float(input('Nhap gia tri can duoi: '))
    b = float(input('Nhap gia tri can tren: '))
    n = int(input('Nhap gia tri cho n: '))
    ans = TTPHinhThang(a , b, n)
    print('Giatri X la: ', X1)
    print('Giatri Y la: ', Y1)
    print('Gia tri gan dung cua tich phan theo PP hinh thang la' , ans)
    ans = TTPSimpson(a, b, n)
    print('Giatri X la: ', X2)
    print('Giatri Y la: ', Y2)
    print('Gia tri gan dung cua tich phan theo PP SimpSon la', ans)

if __name__ == '__main__':
    main()