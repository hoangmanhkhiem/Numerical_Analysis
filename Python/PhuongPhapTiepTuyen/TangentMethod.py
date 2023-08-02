# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


import math


def f(x):
    return x**4+2*x*x*x-x-1

def Tangent_Method(a, b, e):
    f_u = a if f(a) > 0 else b
    x = f_u - f(f_u) * e / (f(f_u+e) - f(f_u))
    while abs(x-f_u) > e:
        f_u = x
        x = f_u - f(f_u) * e / (f(f_u + e) - f(f_u))
    return x


def main():
    a = float(input("Nhap gia tri cho a : "))
    b = float(input("Nhap gia tri cho b : "))
    e = float(input("Nhap gia tri sai so : "))
    print("Gia tri cua nghiem x : ",Tangent_Method(a, b, e))

if __name__ == '__main__':
    main()