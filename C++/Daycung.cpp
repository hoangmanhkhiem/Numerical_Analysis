#include <bits/stdc++.h>
using namespace std;

double f(double x){
    return  x*x*x - x -1;
}

double Daycung(double a, double b, double e)
{

    double x, fu, x0;
    if(f(a)>0){
        fu = a;
        x0 = b;
    }
    else{
        fu = b;
        x0 = a;
    }
    tinh: x = x0 - f(x0)*(fu-x0)/(f(fu)-f(x0));
    while(fabs(x-x0)>e){
        x0 = x;
        goto tinh;
    }
    return x;
}

int main()
{
    double a =0;
    double b = 2;
    double e= 0.0001;
    cout << "Gia tri gan dung cua phuong trinh la : "<< Daycung(a, b, e);
}
