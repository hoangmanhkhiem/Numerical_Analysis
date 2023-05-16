# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


from math import pi,sin

def f(x):
    return (3*(x**2)+3)**0.25

def IterationMethod(x0,n):
    x = x0
    y = f(x)
    while n:
        x = y
        y = f(x)
        n = n - 1
    return y


def Table_IterationMethod(x0,n):
    C = []
    U = ["x", "f(x)"]
    x = x0
    C.append(x)
    y = f(x)
    C.append(y)
    while n:
        x = y
        C.append(x)
        y = f(x)
        C.append(y)
        n = n -1
    print(U)
    U = []
    for i in C:
        U.append(i)
        if len(U)==2:
            print(U)
            U = []


def main():
    x0 = float(input("Nhap gia tri x0: "))
    n = int(input("Nhap so lan lap"))
    print("Bang gia tri")
    Table_IterationMethod(x0, n)
    print("\nGia tri nghiem x: ", IterationMethod(x0, n))

if __name__ == '__main__':
    main()