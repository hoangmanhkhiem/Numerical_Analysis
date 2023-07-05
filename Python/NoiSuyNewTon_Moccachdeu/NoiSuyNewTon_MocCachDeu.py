# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


import numpy as np
import pandas as pd


def doc_input(ten_file):
    # tra ve gia tri cua x va y tu file input.txt
    # doc file input.txt
    inp = open(ten_file, "r")
    # doc du lieu cua x va y
    x = inp.readline()
    y = inp.readline()
    # xu ly du lieu cua x va y
    x = x.strip().split()
    x = np.array(x, dtype=float)
    if (y == ""):
        y = f(x)
        y = np.array(y, dtype=float)
        inp.close()
    else:
        y = y.strip().split()
        y = np.array(y, dtype=float)
        inp.close()
    return x, y


def hoocnerChia(a, value):
    b = [a[0]]
    for i in range(1, len(a)):
        b.append(a[i] + b[i - 1] * value)
    return b


def hoocnerNhanBoSung(coeffTich, t):
    if len(coeffTich) == 0:
        coeffTich.append(1)
        coeffTich.append(-t)
    else:
        coeffTich.append(0)
        temp = coeffTich.copy()
        for i in range(1, len(coeffTich)):
            coeffTich[i] = coeffTich[i] - t * temp[i - 1]
    return coeffTich


# Nội suy Newton tiến
def saiPhanTien(delta, yk):
    temp = delta.copy()
    delta.append(0)
    delta[0] = yk
    for i in range(1, len(delta)):
        delta[i] = delta[i - 1] - temp[i - 1]
    return delta


def ns_NewtonTien(x, y):
    a = [y[0]]
    delta = [y[0]]
    coeffTich = []
    giaiThua_k = 1
    for i in range(1, len(x)):
        delta = saiPhanTien(delta, y[i])
        coeffTich = hoocnerNhanBoSung(coeffTich, i - 1)
        giaiThua_k *= i
        c = delta[len(delta) - 1] / giaiThua_k
        a_1 = a.copy()
        a.append(0)
        for j in range(1, len(a)):
            a[j] = a_1[j - 1] + c * coeffTich[j]
        a[0] = c
    return a


# Nội suy Newton lùi
def saiPhanLui(lamda, yk):
    temp = lamda.copy()
    lamda.append(0)
    lamda[0] = yk
    for i in range(1, len(lamda)):
        lamda[i] = temp[i - 1] - lamda[i - 1]
    return lamda


def ns_NewtonLui(x, y):
    a = [y[len(y) - 1]]
    lamda = [y[len(y) - 1]]
    coeffTich = []
    giaiThua_k = 1
    for i in range(1, len(x)):
        lamda = saiPhanLui(lamda, y[len(y) - 1 - i])
        coeffTich = hoocnerNhanBoSung(coeffTich, 1 - i)
        giaiThua_k *= i
        c = lamda[len(lamda) - 1] / giaiThua_k
        a_1 = a.copy()
        a.append(0)
        for j in range(1, len(a)):
            a[j] = a_1[j - 1] + c * coeffTich[j]
        a[0] = c
    return a


def Newton_Tien():
    x, y = doc_input("inputNewtonCachDeu.txt")
    a = ns_NewtonTien(x, y)
    print("Đa thức nội suy NEWTON TIEN là: \nBậc đa thức nội suy: {0}\n".format(len(a) - 1))
    for i in range(len(a)):
        print("{0} x^{1}".format(a[i], len(a) - 1 - i))
    # Cần tính giá trị nội suy tại điểm x_
    x_ = 2.2

    h = x[1] - x[0]
    t = (x_ - x[0]) / h
    print("Giá trị đa thức nội suy tại: x = {0}\nLà: {1}".format(x_, hoocnerChia(a, t).pop()))


def Newton_Lui():
    x, y = doc_input("inputNewtonCachDeu.txt")
    b = ns_NewtonLui(x, y)
    print("Đa thức nội suy NEWTON LÙI là: \nBậc đa thức nội suy: {0}\n".format(len(b) - 1))
    for i in range(len(b)):
        print("{0} x^{1}".format(b[i], len(b) - 1 - i))
    # Cần tính giá trị nội suy tại điểm x_
    x_ = 2.2

    h = x[1] - x[0]
    t = (x_ - x[len(x) - 1]) / h
    print("Giá trị đa thức nội suy tại: x = {0}\nLà: {1}".format(x_, hoocnerChia(b, t).pop()))

def main():
    Newton_Tien()
    Newton_Lui()

if __name__ == '__main__':
    main()
