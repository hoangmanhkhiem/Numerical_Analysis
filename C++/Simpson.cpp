//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include<bits/stdc++.h>
#define f(x) (x*x*exp(x))/(5*x*x+10)
using namespace std;
double simpson(double a, double b, int n){
    double h=(b-a)/n;
    double s=f(a)+f(b);
    for(int i=1; i<n; i++){
        double x=a+i*h;
        if(i%2==0) s+=2*f(x);
        else s+=4*f(x);
    }
    s*=h/3;
    return(s);
}
int main(){
    cout << "Gia tri tich phan: %f" << simpson(1.2, 4, 4);
}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 0;
}
