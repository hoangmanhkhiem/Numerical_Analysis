//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include <iostream>
#include <cmath>
using namespace std;
const int N = 3; // Kích thước của ma trận và vector

void gaussSeidelMethod(double A[N][N], double b[N], double x[N], double epsilon, int maxIterations) {
    double xNew[N]; // Vector mới sau mỗi lần lặp

    int iteration = 0;
    double error = epsilon + 1; // Sai số khởi tạo

    while (error > epsilon && iteration < maxIterations) {
        for (int i = 0; i < N; ++i) {
            xNew[i] = b[i];
            for (int j = 0; j < N; ++j) {
                if (j != i) {
                    xNew[i] -= A[i][j] * x[j];
                }
            }
            xNew[i] /= A[i][i];
        }

        error = 0.0; // Đặt sai số bằng 0 trước mỗi lần lặp
        for (int i = 0; i < N; ++i) {
            error += fabs(xNew[i] - x[i]);
            x[i] = xNew[i]; // Cập nhật vector x
        }

        ++iteration;
    }
}

int main() {
    double A[N][N] = {{4, 1, -1},
                      {2, 7, 1},
                      {1, -3, 12}}; // Ma trận hệ số
    double b[N] = {3, 19, 31}; // Vector hằng số
    double x[N] = {0, 0, 0}; // Vector nghiệm khởi tạo

    double epsilon = 0.0001; // Độ chính xác mong muốn
    int maxIterations = 100; // Số lần lặp tối đa

    gaussSeidelMethod(A, b, x, epsilon, maxIterations);

    cout << "Solution:" << endl;
    for (int i = 0; i < N; ++i) {
        cout << "x[" << i << "] = " << x[i] << endl;
    }

    return 0;
}
