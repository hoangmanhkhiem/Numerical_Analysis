# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


import matplotlib.pyplot as plt
import math
import sympy as sym
from Extension_KhiemSP import saiphan, bangsaiphan, mulConst, mulHorner, sumHorner, horner, display_poly_gauss_1, \
    display_poly_gauss_2
from Gauss1 import gauss1horner
from Gauss2 import gauss2horner


def gaussbig(x, y, value, num):
    # num là số lượng mốc muốn lấy để nội suy
    n = len(x)
    if (num > n):
        return "Số mốc quá nhiều"

    # lấy 2 mốc trong x gần giá trị value nhất: x1 < value < x2
    # cách tìm mốc gần nhanh hơn chia đôi
    temp = (value - x[0]) / (x[1] - x[0])
    index = int(temp)
    # x1 = x[index]
    # x2 = x[index + 1]

    so_moc_x1 = min(2 * (index + 1), 2 * (n - (index + 1)) + 1)  # số mốc tối đa nội suy quanh x1
    so_moc_x2 = min(2 * (index + 2), 2 * (n - (index + 2)) + 1)  # số mốc tối đa nội suy quanh x2

    # kiểm tra num và lựa chọn mốc nội suy
    if (so_moc_x1 < num) and (so_moc_x2 < num):
        return 'Không đủ mốc'
    elif (so_moc_x1 >= num) and (so_moc_x2 < num):
        x_index = x[index]
    elif (so_moc_x1 < num) and (so_moc_x2 >= num):
        index = index + 1
        x_index = x[index]
    else:
        if abs(x[index] - value) <= abs(x[index + 1] - value):
            x_index = x[index]
        else:
            index = index + 1
            x_index = x[index]
    print('Mốc được chọn: x =', x_index)

    # Lấy số mốc tương ứng với num
    if (num % 2 == 1):
        x_new = x[index - int(num / 2):index + int(num / 2) + 1]
        y_new = y[index - int(num / 2):index + int(num / 2) + 1]

        table = bangsaiphan(x_new, y_new)
        print('Bảng sai phân:')
        for i in range(num):
            print(x_new[i], end="\t")
            for j in range(num - i):
                print(table[j][i], end="\t")
            print("")
    else:
        x_new = x[index - int(num / 2) + 1:index + int(num / 2) + 1]
        y_new = y[index - int(num / 2) + 1:index + int(num / 2) + 1]

        table = bangsaiphan(x_new, y_new)
        print('Bảng sai phân:')
        for i in range(num):
            print(x_new[i], end="\t")
            for j in range(num - i):
                print(table[j][i], end="\t")
            print("")

    ans1 = gauss1horner(x_new, y_new, value)
    ans2 = gauss2horner(x_new, y_new, value)
    ans3 = display_poly_gauss_1(ans1[0], x_new)
    ans4 = display_poly_gauss_2(ans2[0], x_new)

    return ans1, ans2, ans3, ans4


def main():
    print('Phương pháp Gauss với dữ liệu lớn')

    # Hàm sinh dữ liệu để tự động xử lí bài toán
    # Dãy data lớn
    # x = range(1, 40, 1)
    # y = [i ** 7 - 4 * i ** 3 + i - 2 for i in x]
    # value = 21.4
    # num = 9

    # đọc dữ liệu từ file
    f = open("input.txt", "r")
    x = []
    y = []
    for line in f:
        val1, val2 = line.split()
        x.append(float(val1))
        y.append(float(val2))

    value = 1933  # tính tại giá trị 1933
    num = 7

    print('-----------------------------------------')
    a1 = gaussbig(x, y, value, num)
    if type(a1) == str:
        print(a1)
    else:
        print('\n')
        print('Gauss 1 Horner:')
        print('Hệ số:', a1[0][0])
        print('Giá trị tại', value, 'là:', a1[0][1])
        print('Đa thức theo t:', a1[2][0])
        print('Đa thức theo x:', a1[2][1])
        print('\n')
        print('Gauss 2 Horner:')
        print('Hệ số:', a1[1][0])
        print('Giá trị tại', value, 'là:', a1[1][1])
        print('Đa thức theo t:', a1[3][0])
        print('Đa thức theo x:', a1[3][1])


if __name__ == '__main__':
    main()