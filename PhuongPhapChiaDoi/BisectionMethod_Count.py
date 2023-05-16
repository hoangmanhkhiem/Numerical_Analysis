# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


import math

def f(x):
    return x**3 - x - 1

def BisectionMethod(a,b,e):
    e = e + 1
    while(e):
        x = (a+b)/2
        if(f(x)*f(a)>0):
            a = x
        else:
            b = x
        e = e - 1
    return x

def Table_BisectionMethod(a,b,e):
    C =[]
    C.append(b)
    C.append(a)
    e = e + 1
    while (e):
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
        e = e - 1
    O = []
    for i in C:
        O.append(i)
        if len(O) == 4:
            print(O)
            O = []

def main():
    a = float(input('Nhap gia tri a: '))
    b = float(input('Nhap gia tri b: '))
    n = float(input('Nhap so lan chia doi: '))
    print("Bang gia tri")
    Table_BisectionMethod(a, b, n)
    print("\nGia tri nghiem x: ", BisectionMethod(a, b, n))

if __name__ == '__main__':
    main()
