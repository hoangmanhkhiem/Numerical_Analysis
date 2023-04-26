import numpy as np
import math


def input_data(x):
    data_x = np.array([])
    data_y = np.array([])
    data_x = np.loadtxt("inputX.txt")
    data_y = np.loadtxt("inputY.txt")
    check_input(data_x, data_y)
    # x = float(input("Tinh dao ham tai X = "))
    dx = float(data_x[1] - data_x[0])
    return [data_x, data_y, x, dx]


def check_input(data_x, data_y):
    # tra ve 1 khi input hop le va 0 khi input khong hop le
    # kiem tra kich thuoc du lieu
    if (data_x.shape[0] != data_y.shape[0]):
        print("Kich thuoc X, Y khong bang nhau!")
        return 0
    # kiem tra so luong moc noi suy
    if len(data_x) - 1 < 3:
        print("So luong moc noi suy qua it!")
        return 0
    # kiem tra du lieu trung
    for i in data_x:
        if (np.where(data_x == i)[0].shape[0] > 1):
            print("Du lieu cua data_x o cac vi tri ", np.where(data_x == i)[0], " trung nhau")
            return 0
    # kiem tra khoang cach cac moc noi suy
    dx = data_x[1] - data_x[0]
    for i in range(2, data_x.size):
        # SAI SO KHOANG CACH
        if abs(data_x[i] - data_x[i - 1] - dx) > 1e-4:
            raise Exception("Cac moc phai cach deu nhau!")
            return 0
    # input hop le
    print("Input hop le!\n")
    return 1


# ---------------------------------- SAI PHAN TIEN XAP XI P3-------------------------------------------------
# Su dung sai phan tien tinh dao ham cap 1
def forward_difference_first_order(data_x, data_y, x, dx):
    idx = np.where(data_x == x)
    if idx[0].size != 0:
        if idx[0] + 3 > len(data_x) - 1:
            print("Khong the su dung phuong phap sai phan tien tinh dao ham cap 1 tai 3 diem cuoi!")
        else:
            return (2 * data_y[idx[0][0] + 3] - 9 * data_y[idx[0][0] + 2] + 18 * data_y[idx[0][0] + 1] - 11 * data_y[
                idx[0][0]]) / (6 * dx)
    else:
        print("Diem X khong thuoc cac moc noi suy da cho!")


# Sai phan tien tinh dao ham cap 2
def forward_difference_second_order(data_x, data_y, x, dx):
    idx = np.where(data_x == x)
    if idx[0].size != 0:
        if idx[0] + 3 > len(data_x) - 1:
            print("Khong the su dung phuong phap sai phan tien tinh dao ham cap 2!")
        else:
            return (-data_y[idx[0][0] + 3] + 4 * data_y[idx[0][0] + 2] - 5 * data_y[idx[0][0] + 1] + 2 * data_y[
                idx[0][0]]) / (dx * dx)
    else:
        print("Diem X khong thuoc cac moc noi suy da cho!")


# ----------------------------------- SAI PHAN LUI XAP XI P3---------------------------------------------
# Sai phan lui tinh dao ham cap 1
def backward_difference_first_order(data_x, data_y, x, dx):
    idx = np.where(data_x == x)
    if idx[0].size != 0:
        if idx[0] <= 2:
            print("Khong the su dung phuong phap sai phan lui tinh dao ham cap 1 tai 3 diem dau!")
        else:
            return (11 * data_y[idx[0][0]] - 18 * data_y[idx[0][0] - 1] + 9 * data_y[idx[0][0] - 2] - 2 * data_y[
                idx[0][0] - 3]) / (6 * dx)
    else:
        print("Diem X khong thuoc cac moc noi suy da cho!")


def backward_difference_second_order(data_x, data_y, x, dx):
    idx = np.where(data_x == x)
    if idx[0].size != 0:
        if idx[0] <= 2:
            print("Khong the su dung phuong phap sai phan lui tinh dao ham cap 2 tai 3 diem dau tien!")
        else:
            return (-data_y[idx[0][0] - 3] + 4 * data_y[idx[0][0] - 2] - 5 * data_y[idx[0][0] - 1] + 2 * data_y[
                idx[0][0]]) / (dx * dx)
    else:
        print("Diem X khong thuoc cac moc noi suy da cho!")


# -----------------------------SAI PHAN GIUA XAP XI P4----------------------------

def centered_difference_first_order_P4(data_x, data_y, x, dx):
    if (len(data_x) - 1 <= 3):
        print("So luong phan tu it hon 5!")
    else:
        idx = np.where(data_x == x)
        if idx[0].size != 0:
            if idx[0] <= 1 or idx[0] + 2 > len(data_x) - 1:
                print("Tinh dao ham tai 2 diem dau tien va 2 diem cuoi cung khong the su dung phuong phap nay!")
            else:
                return (-data_y[idx[0][0] + 2] + 8 * data_y[idx[0][0] + 1] - 8 * data_y[idx[0][0] - 1] + data_y[
                    idx[0][0] - 2]) / (12 * dx)
        else:
            print("Diem X khong thuoc cac moc noi suy da cho!")


# Sai phan giua tinh dao ham cap 2
def centered_difference_second_order(data_x, data_y, x, dx):
    if (len(data_x) - 1 <= 3):
        print("So luong phan tu it hon 5!")
    else:
        idx = np.where(data_x == x)
        if idx[0].size != 0:
            # Kiem tra vi tri cua X trong data_x
            if idx[0] <= 1 or idx[0] + 2 > len(data_x) - 1:
                print("Tinh dao ham tai 2 diem dau tien va 2 diem cuoi cung khong the su dung phuong phap nay!")
            else:
                return (-data_y[idx[0][0] + 2] + 16 * data_y[idx[0][0] + 1] - 30 * data_y[idx[0][0]] + 16 * data_y[
                    idx[0][0] - 1] - data_y[idx[0][0] - 2]) / (12 * dx * dx)
        else:
            print("Diem X khong thuoc cac moc noi suy da cho!")


# --------------------------------------------------------------------------------
def test_forward_difference(x):
    data_x, data_y, x, dx = input_data(x)
    dy = forward_difference_first_order(data_x, data_y, x, dx)
    print("Tinh theo sai phan tien:")
    print("Dao ham cap 1 tai X = {} : {}".format(x, dy))
    dy2 = forward_difference_second_order(data_x, data_y, x, dx)
    print("Dao ham cap 2 tai X = {} : {}".format(x, dy2))
    print("\n")


def test_backward_difference(x):
    data_x, data_y, x, dx = input_data(x)
    dy = backward_difference_first_order(data_x, data_y, x, dx)
    print("Tinh theo sai phan lui:")
    print("Dao ham cap 1 tai X = {} : {}".format(x, dy))
    dy2 = backward_difference_second_order(data_x, data_y, x, dx)
    print("Dao ham cap 2 tai X = {} : {}".format(x, dy2))
    print("\n")


def test_centered_difference(x):
    data_x, data_y, x, dx = input_data(x)
    dy = centered_difference_first_order_P4(data_x, data_y, x, dx)
    print("Tinh theo sai phan giua xap xi P4(x)")
    print("Dao ham cap 1 tai X = {} : {}".format(x, dy))
    dy2 = centered_difference_second_order(data_x, data_y, x, dx)
    print("Dao ham cap 2 tai X = {} : {}".format(x, dy2))
    print("\n")

def main():
    # Nhập giá trị x (cần tính giá trị đạo hàm tại x)
    x = 65
    test_forward_difference(x)
    test_backward_difference(x)
    test_centered_difference_P2(x)

if __name__ == '__main__':
    main()