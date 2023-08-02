# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


import math

def f(x):
    return x**3-x-1

def BisectionMethod(a,b,e):
    while(abs(b-a)>e):
        x = (a+b)/2
        if(f(x)*f(a)>0):
            a = x
        else:
            b = x
    return x


def Table_BisectionMethod(a,b,e):
    C = [b, a]
    while (abs(b - a) >= e):
        x = (a + b) / 2
        C.append(x)
        C.append(f(x))
        if (f(x) * f(a) > 0):
            a = x
            C.append(a)
            C.append(b)
        else:
            b = x
            C.append(b)
            C.append(a)
    O = []
    for i in C:
        O.append(i)
        if len(O) == 4:
            print(O)
            O = []

def main():
    a = float(input('Nhap gia tri a: '))
    b = float(input('Nhap gia tri b: '))
    eps = float(input('Nhap gia tri sai so: '))
    print("Bang gia tri")
    Table_BisectionMethod(a, b, eps)
    print("\nGia tri nghiem x: ",BisectionMethod(a,b,eps))

if __name__ == '__main__':
    main()
