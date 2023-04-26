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


def hoocne_product(x):
    a = []
    Li = [np.array([1])]
    a.append(np.array([1, 0]))
    for i in x:
        b = a[-1]
        c = []
        c.append(1)
        for j in range(len(b) - 1):
            c.append(b[j + 1] - b[j] * i)
        c.append(0)
        a.append(np.array(c))
        Li.append(np.delete(a[-1], -1))
    return Li


def hoocne_quatient(a, x):
    y = []
    y.append(a[0])
    for i in range(len(a) - 1):
        y.append(y[i] * x + a[i + 1])
    b = np.array(y[:-1])
    b_0 = np.array(y[-1])
    return b, b_0


def nsNewton_bat_ki(x, y):
    P = []
    Z = []
    Li = hoocne_product(x)
    for i in range(x.shape[0]):
        z = [y[i]]
        for j in range(i):
            z.append((z[j] - Z[i - 1][j]) / (x[i] - x[i - j - 1]))
        Z.append(np.array(z))
        Fi = Z[i][i]
        if i == 0:
            P.append(np.array(Fi * Li[i]))
        else:
            P.append(np.concatenate((np.array([0]), P[i - 1])) + Fi * Li[i])
    return P[-1].tolist()


def main():
    x, y = doc_input("inputNewtonBatKy.txt")
    print("Mốc nội suy x: {0}".format(x))
    print("Mốc nội suy y: {0}\n".format(y))
    a = nsNewton_bat_ki(x, y)
    print("Đa thức nội suy là: \nBậc đa thức nội suy: {0}\n".format(len(a) - 1))
    for i in range(len(a)):
        print("{0} x^{1}".format(a[i], len(a) - 1 - i))
    # Cần tính giá trị nội suy tại điểm x_
    x_ = 2.8
    print("Giá trị đa thức nội suy tại: x = {0}\nLà: {1}".format(x_, hoocnerChia(a, x_).pop()))

if __name__ == '__main__':
    main()