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
    while n:
        x = f(x)
        n = n - 1
    return x


def main():
    x0 = float(input("Nhap gia tri x0: "))
    n = float(input("Nhap gia tri lan lap: "))
    print("Gia tri nghiem x: ", IterationMethod(x0, n))

if __name__ == '__main__':
    main()