import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import sys


def Input():
    x, y = [], []
    with open('input.txt','r+') as f: # đọc file input
        for line in f.readlines(): # duyệt từng hàng trong file
            if float(line.split()[0]) not in x:
                x.append(float(line.split()[0]))
                y.append(float(line.split()[1]))
    return x, y


def fx0(f, n, x0):
    value = f[n]
    for i in range(n-1, -1, -1):  #sử dụng lược đồ Hoocne
        value = value*x0 + f[i]
    return value


def plot(x, y, f, n):
    plt.title("Pilot")
    plt.scatter(x, y)
    xx = np.linspace(min(x), max(x), 100)
    ft = simplify("abchihi")  # Nhập hàm muốn vẽ
    ftt = [ft.subs(Symbol("t"), xxx) for xxx in xx]
    plt.plot(xx, ftt, color='red', label=f"ft = {ft}")
    plt.plot(xx, fx0(f, n, xx), color='blue', label="f_Newton")
    plt.legend()
    plt.savefig("Pilot")
    plt.show()


def main():
    x,y = Input()

    plot(x,y,f,n)