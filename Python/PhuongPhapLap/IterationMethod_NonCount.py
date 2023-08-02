# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


from math import pi,sin

def f(x):
    return (3*(x**2)+3)**0.25

def IterationMethod(x0,e):
    x = x0
    y = f(x)
    while abs(x-y) >= e:
        x = y
        y = f(x)
    return y


def Table_IterationMethod(x0,e):
    U = ["x", "f(x)"]
    x = x0
    C = [x]
    y = f(x)
    C.append(y)
    while abs(x - y) > e:
        x = y
        C.append(x)
        y = f(x)
        C.append(y)
    print(U)
    U = []
    for i in C:
        U.append(i)
        if len(U)==2:
            print(U)
            U = []


def main():
    x0 = float(input("Nhap gia tri x0: "))
    e = float(input("Nhap gia tri sai so: "))
    print("Bang gia tri")
    Table_IterationMethod(x0, e)
    print("\nGia tri nghiem x: ", IterationMethod(x0, e))

if __name__ == '__main__':
    main()