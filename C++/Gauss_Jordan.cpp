//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include <iostream>
#include <vector>
using namespace std;
// Hàm kiểm tra trường hợp vô nghiệm hoặc vô số nghiệm
bool checkInconsistent(vector<vector<double>>& matrix) {
    int n = matrix.size();

    for (int i = 0; i < n; i++) {
        bool allZeros = true;
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] != 0) {
                allZeros = false;
                break;
            }
        }
        if (allZeros && matrix[i][n] != 0) {
            return true; // Hệ phương trình vô nghiệm
        }
    }
    return false;
}

// Hàm kiểm tra trường hợp vô số nghiệm
bool checkInfiniteSolutions(vector<vector<double>>& matrix) {
    int n = matrix.size();

    for (int i = 0; i < n; i++) {
        bool allZeros = true;
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] != 0) {
                allZeros = false;
                break;
            }
        }
        if (allZeros && matrix[i][n] == 0) {
            return true; // Hệ phương trình vô số nghiệm
        }
    }

    return false;
}

// Hàm thực hiện khử Gauss
void gaussElimination(vector<vector<double>>& matrix) {
    int n = matrix.size();

    for (int i = 0; i < n; i++) {
        // Tìm vị trí hàng có giá trị lớn nhất trong cột hiện tại
        int maxRow = i;
        for (int j = i + 1; j < n; j++) {
            if (matrix[j][i] > matrix[maxRow][i]) {
                maxRow = j;
            }
        }

        // Hoán đổi hàng
        for (int k = i; k < n + 1; k++) {
            double temp = matrix[i][k];
            matrix[i][k] = matrix[maxRow][k];
            matrix[maxRow][k] = temp;
        }

        // Lặp qua từng hàng và khử các biến
        for (int j = i + 1; j < n; j++) {
            double ratio = matrix[j][i] / matrix[i][i];

            for (int k = i; k < n + 1; k++) {
                matrix[j][k] -= ratio * matrix[i][k];
            }
        }
    }
}

// Hàm giải hệ phương trình bằng phương pháp lùi
vector<double> backSubstitution(vector<vector<double>>& matrix) {
    int n = matrix.size();
    vector<double> solution(n);

    for (int i = n - 1; i >= 0; i--) {
        solution[i] = matrix[i][n];

        for (int j = i + 1; j < n; j++) {
            solution[i] -= matrix[i][j] * solution[j];
        }

        solution[i] /= matrix[i][i];
    }

    return solution;
}

int main() {
    int n;
//    FILE *f;
//    f = freopen("D:\\Fileanswerltol\\gaussseide\\input10.txt","rt",stdin);
    cin >> n;
    vector<vector<double>> matrix(n, vector<double>(n + 1));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n + 1; j++) {
            cin >> matrix[i][j];
        }
    }
//    fclose(f);
//    f = freopen("D:\\Fileanswerltol\\gaussseide\\output10.txt","wt",stdout);
    // Áp dụng phương pháp khử Gauss
    gaussElimination(matrix);

    // Kiểm tra trường hợp vô nghiệm và vô số nghiệm
    if (checkInconsistent(matrix)) {
        cout << "Khong co nghiem thoa man" << endl;
    } else if (checkInfiniteSolutions(matrix)) {
        cout << "He co vo so nghiem" << endl;
    } else {
        // In ma trận sau khử Gauss

        // Giải hệ phương trình bằng phương pháp lùi
        vector<double> solution = backSubstitution(matrix);

        // In nghiệm
        for (int i = 0; i < n; i++) {
            cout << solution[i] << "\n";
        }
    }
}
