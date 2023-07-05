//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include <iostream>
#include <cmath>
using namespace std;
double f(double x) {
    return x * x - 4;
}

double g(double x) {
    return sqrt(4 - x * x);
}

double PPLap(double x0, double epsilon, int maxIterations) {
    double x = x0;
    int iteration = 0;
    while (fabs(f(x)) > epsilon && iteration < maxIterations) {
        x = g(x);
        ++iteration;
    }
    return x;
}

int main() {
    double x0 = 2.0;
    double epsilon = 0.0001;
    int maxIterations = 100;
    double solution = PPLap(x0, epsilon, maxIterations);
    cout << "Solution: " << solution << endl;
}
