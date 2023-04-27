# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


from math import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import sys

np.set_printoptions(suppress=True, linewidth=np.inf, precision=5)#chỉnh số chữ số sau dấu phẩy

def Input():
    x, y = [], []
    with open('input.txt','r+') as f: # đọc file input
        for line in f.readlines(): # duyệt từng hàng trong file
            if float(line.split()[0]) not in x:
                x.append(float(line.split()[0]))
                y.append(float(line.split()[1]))
    return x, y

# kết nạp mốc x[i] vào Bảng tỷ hiệu
def BuildBTH(BTH, x, y, i):
    TH_row_i = np.zeros(len(x))
    TH_row_i[0] = y[i]
    for j in range(1, i+1):
        TH_row_i[j] = (TH_row_i[j-1] - BTH[j-1]) / (x[i] - x[i-j])
    return TH_row_i

# kết nạp mốc x[i] vào Bảng tính tích
def BuildBTT(BTT, x, i):      
    TT_row_i = np.zeros(len(x))
    TT_row_i[i+1] = 1                 #sử dụng lược đồ Hoocne
    for j in range(i, 0, -1):   
        TT_row_i[j] = BTT[j-1] - x[i]*BTT[j]
    TT_row_i[0] = -x[i]*BTT[0]
    return TT_row_i

# kết nạp mốc x[i] vào đa thức
def fx(BTH, BTT, i, f):   
    for j in range(0, i+1):
        f[j] += BTH[i]*BTT[j]
    return f

# Xây dựng đa thức nội suy Newton tiến
def Newton_interpolation_Forward(BTH, BTT, f, x, y, n):
    for i in range(1, n+1):
        BTH = BuildBTH(BTH, x, y, i)
        BTT = BuildBTT(BTT, x, i-1)
        f = fx(BTH, BTT, i, f)
    return f, BTH, BTT

# ước tính f(x0)
def fx0(f, n, x0):   
    value = f[n]
    for i in range(n-1, -1, -1):  #sử dụng lược đồ Hoocne
        value = value*x0 + f[i]
    return value
# Xây dựng đa thức nội suy Newton lùi
def Newton_interpolation_Backward(BTH, BTT, f, x, y, n):
    x.reverse()
    y.reverse()
    BTH[0], f[0] = y[0], y[0]
    return Newton_interpolation_Forward(BTH, BTT, f, x, y, n)

# Thêm mốc nội suy
def add_Newton(BTH, BTT, f, x, y, n):
    BTH = BuildBTH(BTH, x, y, n)
    BTT = BuildBTT(BTT, x, n-1)
    f = np.hstack((f, np.zeros(1))) # tạo thêm 1 cột cho f
    f =  fx(BTH, BTT, n, f)
    return f, BTH, BTT

# vẽ hình
def plot(x, y, f, n):
    plt.title("Newton interpolation")
    plt.scatter(x,y)
    xx = np.linspace(min(x), max(x), 100)
    ft = simplify("1/(25*t**2+1)")   #Nhập hàm muốn vẽ
    ftt = [ft.subs(Symbol("t"), xxx) for xxx in xx]
    plt.plot(xx, ftt, color = 'red', label = f"ft = {ft}")
    plt.plot(xx, fx0(f, n, xx), color = 'blue', label = "f_Newton")
    plt.legend()
    plt.savefig("newton")
    plt.show()

# đổi biến 
def doi_bien(x, x0):
    var = x0     # t = x - var
    for i in range(len(x)):
        x[i] = x[i] - var
    x0 = x0 - var
    return x, x0

def main():
    x, y = Input()
    n = len(x) - 1
    x0 = float(input("Mời nhập giá trị cần tính: "))

    print("Các mốc nội suy: ")
    print(x)

    # khởi tạo ma trận không 1 chiều
    BTH, BTT, f = np.zeros(n+1), np.zeros(n+1), np.zeros(n+1)
    BTH[0], BTT[0], f[0] = y[0], 1, y[0]

    #x, x0 = doi_bien(x, x0)
    #print("Các mốc nội suy sau khi đổi biến:")
    #print(x)

    #f, BTH, BTT = Newton_interpolation_Backward(BTH, BTT, f, x, y, n)
    f, BTH, BTT = Newton_interpolation_Forward(BTH, BTT, f, x, y, n)

    value = fx0(f, n, x0)
    print("Hệ số đa thức nội suy Newton là: (bắt đầu từ hệ số tự do)")
    print(f)
    print("Giá trị cần tính tại", x0, " là:", value)
        
    plot(x, y, f, n)
    k = int(input("Nhập số lượng thêm mốc nội suy: "))
    if k <= 0:
        sys.exit()
    for i in range(k):
        xt, yt = input("Nhập mốc và giá trị nội suy: ").split()
        if float(xt) not in x:
            n += 1
            x.append(float(xt))
            y.append(float(yt))
            f, BTH, BTT = add_Newton(BTH, BTT, f, x, y, n)

    value = fx0(f, n, x0)
    print("Hệ số đa thức nội suy Newton là: (bắt đầu từ hệ số tự do)")
    print(f)
    print("Giá trị cần tính tại", x0, " là:", value)
    plot(x, y, f, n)
        
if __name__=='__main__':
    main()