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
    while abs(x-y)>e:
        x = y
        y = f(x)
    return y


def main():
    x0 = float(input("Nhap gia tri x0: "))
    e = float(input("Nhap gia tri sai so: "))
    print("Gia tri nghiem x: ", IterationMethod(x0, e))

if __name__ == '__main__':
    main()