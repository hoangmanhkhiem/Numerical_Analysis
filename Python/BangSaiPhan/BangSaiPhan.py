# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


def proterm(i, value, x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro


def DiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))
    return y


def applyFormula(value, x, y, n):
    sum = y[0][0]
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i])
    return sum


def prt(y, n):
    for i in range(n):
        # for j in range(n - i):
        #     print("y[", i, "][", j, "] = ", round(y[i][j], 4))
        print(y[i])
    print("")


def main():
    n = 6
    y = [[0 for _ in range(10)] for _ in range(10)]

    x = [11, 13, 14, 18, 19, 21]

    y[0][0] = 2342
    y[1][0] = 2210
    y[2][0] = 2758
    y[3][0] = 5850
    y[4][0] = 6878
    y[5][0] = 9282

    y = DiffTable(x, y, n)

    prt(y, n)

    value = 13.5
    print("Gia tri tai ", value, "la", applyFormula(value, x, y, n))


if __name__ == '__main__':
    main()
