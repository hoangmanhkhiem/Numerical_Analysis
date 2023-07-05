//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include<bits/stdc++.h>
using namespace std;

double f(double x){
    return  x*x*x - x -1;
}

double Tieptuyen(double a, double b, double e)
{
    double fu, x;
    if(f(a)>0) fu = a;
    else fu = b;
    tinh: x = fu - f(fu)*e/(f(fu + e) - f(fu));
    while(fabs(x - fu)>e){
        fu = x;
        goto tinh;
    }
    return x;
}

int main()
{
    double a = 0;
    double b =1;
    double e = 0.0001;
    float result = Tieptuyen(a, b, e);
    printf("x = %.4f", result);
    return 0;
}
