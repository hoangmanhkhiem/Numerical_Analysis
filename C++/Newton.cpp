//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include <iostream>
using namespace std;

double SaiPhan(double* y, int n, int k) {
    if (k == 0) {
        return y[0];
    }

    double* nextDifferences = new double[n];
    for (int i = 0; i < n - k; ++i) {
        nextDifferences[i] = y[i + 1] - y[i];
    }

    double result = SaiPhan(nextDifferences, n - 1, k - 1);

    delete[] nextDifferences;
    return result;
}

double Newton(double* x, double* y, int n, double target) {
    double* differences = new double[n];
    for (int i = 0; i < n; ++i) {
        differences[i] = SaiPhan(y, n, i);
    }

    double result = y[0];
    double term = 1.0;
    for (int i = 1; i < n; ++i) {
        term *= (target - x[i - 1]);
        result += term * differences[i];
    }

    delete[] differences;
    return result;
}

int main() {
    const int n = 4;
    double x[n] = { 1.0, 2.0, 3.0, 4.0 };
    double y[n] = { 2.0, 4.0, 6.0, 8.0 };

    double target = 2.5;
    double y0 = Newton(x, y, n, target);

    cout << "Gia tri noi suy tai " << target << " = " << y0 << endl;

    return 0;
}
