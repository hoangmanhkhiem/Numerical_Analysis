from sympy import sympify, symbols
from sympy import *
import math


# Công thức hình thang

def trapezoidal(A):
    """ Tính gần đúng tích phân xác định bằng công thức hình thang """
    trape = 1/2*(A[0] + A[n])
    for i in range(1, n):
        trape = trape + A[i]
    print("Tích phân bằng công thức hình thang      :", trape*h)

def trapezoidal_error():
    """ Sai số của công thức hình thang """
    m = max(f, 2)
    print("Sai số công thức hình thang :", m/12*(b-a)*(h**2))

def trpezoidal_intervals():
    """ Số khoảng chia để thỏa mãn sai số cho trước trong công thức hình thang"""
    m = max(f, 2)
    print("Số khoảng chia cần thiết (Hình thang)    :",math.floor((abs(((m*(b-a)**3)*(1/12)*(1/eps))))**(1/2))+1)


# Công thức Simpson

def simpson(A):
    """ Tính gần đúng tích phân xác định bằng công thức Simpson """
    simp = h/3*(A[0]+A[n])
    simp_odd = 0
    simp_even = 0        
    for i in range(1, n, 2):
        simp_odd += A[i]
    for i in range(2, n, 2):
        simp_even += A[i]
    simp = simp + h/3*4*simp_odd + h/3*2*simp_even
    print("Tích phân bằng công thức Simpson         :", simp)

def simpson_error():
    """ Sai số của công thức Simpson """
    m = max(f, 4)
    print("Sai số công thức Simpson                 :", m/180*(b-a)*(h**4))

def simpson_intervals():
    """ Số khoảng chia để thỏa mãn sai số cho trước trong công thức Simpson"""
    m = max(f, 4)
    n = math.floor((abs((m*(b-a)**5)*(1/180)*(1/eps)))**(1/4))+1
    if n % 2 == 1:
        print("Số khoảng chia cần thiết (Simpson)       :",n+1)
    else:
        print("Số khoảng chia cần thiết (Simpson)       :",n+2)


# Công thức Newton - Cotes

def multiply_horner(A, i) -> list:
    """ Nhân một đa thức với (x-i) """
    A.append(0)
    for j in range(len(A)-1,0,-1):
        A[j] = A[j] - A[j - 1] * i
    return A

def devide_horner(A, i) -> list:
    """ Chia một đa thức với (x-i) """
    X = A.copy()
    X.pop()
    for j in range(1, len(X)):
        X[j] = i*X[j-1] + X[j]
    return X

def poly_integral(A, a, b) -> float:
    I = 0
    """ Tính tích phân xác định của đa thức """
    for j in range(0, len(A)):
        if (A[j] == 0):
            continue
        else:
            A[j] = A[j]/(len(A)-j)     
        I = I + A[j]*(b**(len(A)-j)-a**(len(A)-j))
    return I

def cotez_coef(i) -> float:
    """ Tính hệ số Cotez H_i"""
    # D là tích các đa thức (t-j), j từ 0 đến n, nhưng để tiết kiệm thời gian, tính 
    # nó một lần duy nhất ở dưới.
    X = devide_horner(D, i)
    h = (1/n)*((-1)**(n-i))/(math.factorial(i)*math.factorial(n-i))*poly_integral(X, 0, n)
    return h
    
def newton_cotez() -> float:
    """ Tính gần đúng tích phân xác định bằng công thức Newton - Cotez """
    E = 0
    Hs = [1]*(n+1)
    for i in range(0, n+1):
        Hs[i]   = cotez_coef(i)
        E       = E + Hs[i]*A[i]
    print(f'Hệ số Cotes ứng với n = {n}                :',Hs)
    print('Tích phân bằng công thức Newton - Cotez  :', E*(b-a))

def newton_cotez_error() -> float: 
    """ Sai số của công thức Newton - Cotez"""
    g = Derivative(f,(x, n), evaluate=True)
    if (n % 2 == 0):
        D1 = D.copy()
        multiply_horner(D1, n+1)
        m2 = max(g, 2)
        print("Sai số công thức Newton - Cotez          :", abs(float(m2)*poly_integral(D1, 0, n)*(h**(n+3))/math.factorial(n+2)))
    else:
        m1 = max(g, 1)
        print("Sai số công thức Newton - Cotez          :", abs(float(m1)*poly_integral(D, 0, n)*(h**(n+2))/math.factorial(n+1)))


def max(fx, i):
    """ Tìm maximum của đạo hàm cấp i của hàm f(x)"""
    g   = Derivative(fx,(x, i), evaluate=True)
    m1  = abs(maximum(g, x, Interval(a, b)))
    m2  = abs(minimum(g, x, Interval(a, b)))
    if m1 > m2:
        m = m1
    else:
        m = m2
    return m


def main():
    global n, a, b, f, h, x, D, A, eps
    x           = symbols('x')
    func        = input('Nhập hàm f(x): ')
    f           = sympify(func)
    init_value  = input('Nhập khoảng lấy tích phân a, b (a < b) cách nhau bởi dấu cách: ')
    a, b        = [float(i) for i in init_value.split()]
    q           = int(input('Chọn bài toán bạn muốn giải quyết (Nhập số theo bài toán)''\n''(1) Tính tích phân (2) Tính số khoảng chia cần thiết: '))
    if q == 1:
        n       = int(input('Nhập số khoảng chia n: '))
        h       = (b-a)/n
    
        D       = [1]
        for i in range(0, n+1):
            multiply_horner(D, i)                           # Tích các (t-j), j từ 0 đến n
        
        A       = [f.subs(x,a+i*h) for i in range(n+1)]     # Tạo mảng lưu giá trị hàm tại các mốc nội suy

        if n % 2 == 0:
            trapezoidal(A)
            trapezoidal_error()
            print()
            simpson(A)
            simpson_error()
            print()
            newton_cotez()
            newton_cotez_error()
        else:
            trapezoidal(A)
            trapezoidal_error()
            print()
            newton_cotez()
            newton_cotez_error()

    if q == 2:
        eps     = float(input('Nhập epsilon: '))
        trpezoidal_intervals()
        simpson_intervals()


if __name__ == '__main__':
    main()
