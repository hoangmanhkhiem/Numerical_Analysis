#include <iostream>
#include <vector>
using namespace std;
struct DataPoint {
    double x;
    double y;
};

double Lagrange(const vector<DataPoint>& data, double x) {
    double result = 0.0;
    for (int i = 0; i < data.size(); ++i) {
        double term = data[i].y;
        for (int j = 0; j < data.size(); ++j) {
            if (j != i) {
                term *= (x - data[j].x) / (data[i].x - data[j].x);
            }
        }
        result += term;
    }
    return result;
}

int main() {
    vector<DataPoint> data = {
            {1.0, 2.0},
            {2.0, 4.0},
            {3.0, 6.0},
            {4.0, 8.0}
    };

    double x = 2.5;
    double y = Lagrange(data, x);
    cout << "Gia tri noi suy tai " << x << " = " << y << endl;
}
