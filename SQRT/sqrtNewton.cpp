#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

double SQRT(double n) {
    double x = 1, x2 = 10e17;
    while (x != x2){
        x = x2;
        x2 = (x + n / x) / 2;
    }
    return x;
}

int count(double a, double b) {
    int c = -1;
    a = fabs(a - b);
    if (a == 0)
        return -1;
    while (a < 1) {
        c++;
        a *= 10;
    }
    return c;
}

int main() {
    double n;
    cin >> n;
    cout << fixed << "SQRT() = " << setprecision(52) << SQRT(n) << endl;
    cout << fixed << "sqrt() = " << setprecision(52) << sqrt(n) << endl;
    int k = count(SQRT(n), sqrt(n));
        if (k != -1)
            cout << "Sai so: 10 ^ -" << k; 
        else
            cout << "Khong co sai so.";
    cout << endl << " " << endl;
}
