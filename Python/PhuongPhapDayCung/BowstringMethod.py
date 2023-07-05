# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


import math

def f(x):
    return x**4+2*x*x*x-x-1

def Bowstring_Method(a,b,e):
    f_a = f(a)
    f_b = f(b)
    dx = f_a*(b-a)/(f_a-f_b)
    x = 0
    while abs(dx) > e:
        x = a + dx
        f_a = f(x)
        if f_a * f_b <= 0:
            a = x
        else:
            b = x
        f_a = f(a)
        f_b = f(b)
        dx = f_a*(b-a)/(f_a-f_b)
    return x


def main():
    a = float(input("Nhap gia tri cho a : "))
    b = float(input("Nhap gia tri cho b : "))
    eps = float(input("Nhap gia tri cho sai so: "))
    print("Gia tri cua nghiem x : ", Bowstring_Method(a , b, eps))


if __name__ == '__main__':
    main()