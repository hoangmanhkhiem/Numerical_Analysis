//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include <iostream>
#include <cmath>
using namespace std;
double f(double x) {
    return x*x*x - x -1;
}

double bisectionMethod(double a, double b, double epsilon) {
    double c;
    int it=1;
    do{
        c = (a+b)/2;
        if(f(c)*f(a)>0)
            a=c;
        else
            b=c;
        double saiso=fabs(b-a);
        cout<<"Iteration-"<< it <<":\t x = "<< c <<"\t sai so: "<<saiso<< endl;
        it++;
    }while(fabs(b-a)>=epsilon);
    return c;
}

int main() {
    double a = 0.0;
    double b = 5.0;
    double epsilon = 0.0001;

    double solution = bisectionMethod(a, b, epsilon);

    cout << "Solution: " << solution << std::endl;

    return 0;
}
