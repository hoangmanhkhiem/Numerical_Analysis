_Max = 100

def F(x):
    return x
X = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2]
Y = [4, 3.3, 2.4, 4.3, 10.2, 6.2, 7.4]

def Khoi_tao(n):
    Z = []
    for i in range(n+1):
        Z.append(X[i]*Y[i]*Y[i]+4.4*X[i]*X[i]*X[i]) # Phương trình ẩn Fx x
    return Z
#Phương pháp hình thang
def TTPHinhThang(X,n):
    # if n == 0:
    #     n = _Max
    ans = 0
    h = 0.2
    # for i in range (n+1):
    #     X.append(a + i * h)
    #     Y.append(F(a + i * h))
    Z = Khoi_tao(n)
    for i in range(n+1):
        if i == 0 or i == n:
            ans += Z[i]
        else:
            ans += 2 * Z[i]
    return h / 2 * ans

def main():
    n = int(input('Nhap gia tri cho n: '))
    ans = TTPHinhThang(X, n)
    print('Gia tri cua tich phan la',ans)
    print('Giatri X la: ' , X)
    print('Giatri Y la: ' , Y)
    print('Giatri Z la: ' , Khoi_tao(n))
if __name__ == '__main__':
    main()