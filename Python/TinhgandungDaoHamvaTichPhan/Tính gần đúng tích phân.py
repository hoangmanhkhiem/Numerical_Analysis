# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


_Max = 100

def F(x):
    return x
X = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.2]
Y = [4, 3.3, 2.4, 4.3, 10.2, 6.2, 7.4]

def Khoi_tao(n):
    return [X[i]*Y[i]*Y[i]+4.4*X[i]*X[i]*X[i] for i in range(n+1)]
#Phương pháp hình thang
def TTPHinhThang(X,n):
    h = 0.2
    # for i in range (n+1):
    #     X.append(a + i * h)
    #     Y.append(F(a + i * h))
    Z = Khoi_tao(n)
    ans = sum(Z[i] if i in [0, n] else 2 * Z[i] for i in range(n+1))
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