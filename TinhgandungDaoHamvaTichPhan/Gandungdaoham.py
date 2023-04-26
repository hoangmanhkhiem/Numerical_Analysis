import math

def Input():
    """ Nhập bảng số """
    global x, y, n, a, h, t
    x = []
    y = []
    with open('Input.txt','r+') as f:
        a = float(f.readline())                     
        while True:
            line = f.readline()
            if not line: break
            temp = [float(i) for i in line.split()]
            x.append(temp[0])
            y.append(temp[1])
    n = len(x)-1
    h = (x[n]-x[0])/n
    t = (a - x[0])/h

def multiply_horner(A, i) -> list:
    """ Nhân một đa thức với (t-i) """ 
    A.append(0)
    for j in range(len(A)-1,0,-1):
        A[j] = A[j] - A[j - 1] * i
    return A

def devide_horner(A, i) -> list:
    """ Chia một đa thức với (t-i) """
    for j in range(1, len(X)):
        X[j] = i*X[j-1] + A[j]
    return X

def P_t() -> list:
    """ Tính P(t) """
    Pt = [0]*(n+1)
    for i in range(n+1):
        D = devide_horner(A, i)
        for j in range(n+1):
            Pt[j] = Pt[j] + D[j]*((-1)**(n-i))/(math.factorial(i)*math.factorial(n-i))*y[i]
    return Pt

def deri_approx(Pt):
    """ Tính gần đúng đạo hàm cấp 1 """
    ans = 0
    for i in range(n):
        ans = ans + (1/h)*Pt[i]*(n-i)*(t**(n-i-1))
    print("Giá trị của đạo hàm : ", ans)
    
Input()

A = [1]
for i in range(0, n+1):
    A = multiply_horner(A, i)   # Mảng chứa tích các (t-i)

X = [1]*(n+1)   # Tạo mảng lưu giá trị phép chia A cho (t-i)

Pt = P_t()
deri_approx(Pt) 