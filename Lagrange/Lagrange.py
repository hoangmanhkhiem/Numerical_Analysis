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
        # y = f(x)
        y = np.array(y, dtype=float)
        inp.close()
    else:
        y = y.strip().split()
        y = np.array(y, dtype=float)
        inp.close()
    return x, y


def hoocnerNhan(x):
    a = [1, -x[0]]
    for i in range(1, len(x)):
        a.append(0)
        temp = a.copy()
        for j in range(1, len(a)):
            a[j] = temp[j] - temp[j - 1] * x[i]
        a[0] = 1
    return a


def hoocnerChia(a, value):
    b = [a[0]]
    for i in range(1, len(a)):
        b.append(a[i] + b[i - 1] * value)
    return b


def noiSuyLagrange(x, y):
    a = np.zeros(len(x))
    phi = hoocnerNhan(x)
    for i in range(len(x)):
        omega = hoocnerChia(phi, x[i])
        omega.pop()
        k = y[i] / hoocnerChia(omega, x[i]).pop()
        for j in range(len(a)):
            a[j] += k * omega[j]
    return a.tolist()


def main():
    x, y = doc_input("inputLagrange.txt")
    print("Mốc nội suy x: {0}".format(x))
    print("Mốc nội suy y: {0}\n".format(y))
    a = noiSuyLagrange(x, y)
    print("Đa thức nội suy là: Bậc đa thức nội suy: {0}".format(len(a) - 1))
    for i in range(len(a)):
        print("{0} x^{1}".format(a[i], len(a) - 1 - i))
    # Cần tính giá trị nội suy tại điểm x_
    x_ = 2.4

    print("Giá trị đa thức nội suy tại: x = {0}\nLà: {1}".format(x_, hoocnerChia(a, x_).pop()))


if __name__ == '__main__':
    main()
