from math import *
import numpy as np
import matplotlib.pyplot as plt
import sys

np.set_printoptions(suppress=True, linewidth=np.inf, precision=5) #chỉnh số chữ số sau dấu phẩy

def Input():  #giả thiết input được sắp xếp cách đều tăng dần
    x, y = [], []
    with open('input.txt','r+') as f: # đọc file input
        for line in f.readlines(): # duyệt từng hàng trong file
            if float(line.split()[0]) not in x:
                x.append(float(line.split()[0]))
                y.append(float(line.split()[1]))
    for i in range(1, len(x)): # kiếm tra cách đều
        if abs(x[i] - x[i-1] - (x[1] - x[0])) > 1e-6:
            print("Input không hợp lệ!")
            sys.exit()
    return x, y
    
#chọn ra num điểm gần x0 nhất
def pickPoint(x0, num, x, y):
    if num > len(x):
        print("Error!!!")
        sys.exit()
    i = int((x0 - x[0])/(x[1]-x[0]))  #x0 thuộc (x[i], x[i+1])
    left = min(len(x) - num, max(0, i + 1 - int(num/2))) 
            #max để xứ lí TH x0 < x[0], min xử lí TH x0 > x[n]
    right = left + num - 1
        #num điểm gần x0 nhất nằm trong đoạn x[left] đến x[right]
    x1, y1 = [], []
    x1[:] = x[left: right+1]
    y1[:] = y[left: right+1]

    return x1, y1

# kết nạp mốc x[i] vào Bảng sai phân Lùi
def BuildBSP(BSP, x, y, i):
    SP_row_i = np.zeros(len(x))
    SP_row_i[0] = y[i]
    for j in range(1, len(x)-i):
        SP_row_i[j] = BSP[j-1] - SP_row_i[j-1] 
    return SP_row_i

# kết nạp mốc x[i] vào Bảng tính tích
def BuildBTT(BTT, x, i):      
    TT_row_i = np.zeros(len(x))
    TT_row_i[-i] = 1                 #sử dụng lược đồ Hoocne
    for j in range(-i, 0, -1):   
        TT_row_i[j] = BTT[j-1] - i*BTT[j]
    if i != 0: TT_row_i[0] = -i*BTT[0]
    return TT_row_i

# kết nạp mốc x[i] vào đa thức newton Lùi
def fx(BSP, BTT, i, f):   
    for j in range(1, i+1):
        f[j] += BSP[i]*BTT[j-1]/factorial(i)
    return f

# Xây dựng đa thức nội suy Newton lùi
def Newton_interpolation_Backward(BSP, BTT, f, x1, y1, n):
    for i in range(1, n+1):
        BSP = BuildBSP(BSP, x1, y1, n-i)
        BTT = BuildBTT(BTT, x1, 1-i)
        f = fx(BSP, BTT, i, f)
    return f, BSP, BTT

# ước tính f(x0)
def fx0(f, x0, x1):
    t = (x0 - x1[len(x1) - 1])/(x1[1] - x1[0])
    value = f[len(x1) - 1]
    for i in range(len(x1) - 2, -1, -1):  #sử dụng lược đồ Hoocne
        value = value*t + f[i]
    return value

# Thêm mốc nội suy
def add_Newton(BSP, BTT, f, x1, y1, n):
    BSP = BuildBSP(BSP, x1, y1, 0)
    BTT = BuildBTT(BTT, x1, 1-n)
    f = np.hstack((f, np.zeros(1))) # tạo thêm 1 cột cho f
    f = fx(BSP, BTT, n, f)
    return f, BSP, BTT
    
#vẽ hình
def plot(x, y, f):
    plt.title("Newton interpolation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(x,y)
    xx = np.linspace(min(x), max(x), 1000)
    # ft = simplify("1/(25*t**2+1)") #Nhập hàm muốn vẽ
    # ftt = [ft.subs(Symbol("t"), xxx) for xxx in xx]
    # plt.plot(xx, ftt, color = 'red', label = f"ft = {ft}")
    plt.plot(xx, fx0(f, xx, x), color = 'blue', label = "f_Newton")
    # plt.legend()
    plt.savefig("newton")
    # plt.show()

def main():
    x, y = Input()
    x0 = float(input("Mời nhập giá trị cần tính: "))
    num = int(input(f"Chọn số lượng mốc nội suy tính (<= {len(x)}): "))

    h = x[1] - x[0]
    
    x1, y1 = pickPoint(x0, num, x, y) # chọn deg điểm gần x0 nhất
    print("Các mốc nội suy: ")
    print(x1)
    # x1 từ x[left] đến x[right]
    n = len(x1) - 1

    BSP, BTT, f = np.zeros(n+1), np.zeros(n+1), np.zeros(n+1)
    BSP[0], BTT[0], f[0] = y1[n], 1, y1[n]

    f, BSP, BTT = Newton_interpolation_Backward(BSP, BTT, f, x1, y1, n)
    print("Hệ số của đa thức nội suy Newton: (bắt đầu từ hệ số tự do)")
    print(f)
    print(f"t = (x - {x1[n]})/{round(x1[1]-x1[0], 6)}")

    value = fx0(f, x0, x1)
    print("Giá trị cần tính tại", x0, " là:", value)
    
    plot(x1, y1, f)
    k = int(input("Nhập số lượng thêm mốc nội suy: "))
    if k <= 0:
        sys.exit()
    for i in range(k):
        xt, yt = input("Nhập mốc và giá trị nội suy: ").split()
        if float(xt) not in x1 and abs(x1[0] - float(xt) - h) < 1e-6:
            n += 1
            x1.insert(0, float(xt))
            y1.insert(0, float(yt))
            f, BSP, BTT = add_Newton(BSP, BTT, f, x1, y1, n)
    
    print("Hệ số của đa thức nội suy Newton: (bắt đầu từ hệ số tự do)")
    print(f)
    print(f"t = (x - {x1[n]})/{abs(round(h, 6))}")

    value = fx0(f, x0, x1)
    print("Giá trị cần tính tại", x0, " là:", value)
    
    plot(x1, y1, f)

if __name__=='__main__':
    main()
