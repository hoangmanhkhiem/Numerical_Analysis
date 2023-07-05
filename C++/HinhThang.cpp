#include<bits/stdc++.h>
using namespace std;
#define f(x) (x*x/(4*x*x+11))*atan(x)
double Hinhthang(int n, double a, double b){
    double h = (b-a)/n;
    double s = f(a) + f(b);
    for (int i=1;i<n;i++)
    {
        double x = a + i*h;
        s += 2*f(x);
    }
    s = (h/2)*s;
    return s;
}
int main() {
	cout << "Gia tri Tich Phan tinh theo cong thuc Hinh thang = " << Hinhthang(10,1,2);
}
