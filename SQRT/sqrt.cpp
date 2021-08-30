#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

double SQRT(double n) {
    long long l = 0;
    long long r = 10e9;
    long long mid = 0;
    long long int_Sqrt = 123;
    double sqrt_temp = 0;
    while (l < r){
        mid = (l + r + 1) / 2;
        if (mid * mid < n)
            l = mid;
        else
            r = mid - 1;
    }
    int_Sqrt = l;
    if (int_Sqrt * int_Sqrt == n)
        return int_Sqrt;
    l = 0;
    r = 10e17 - 1;
    while(l < r){
        mid = (l + r) / 2;
        sqrt_temp = int_Sqrt + mid / 10e17;
        if (sqrt_temp * sqrt_temp < n)
            l = mid + 1;
        else
            r = mid;
    }
    sqrt_temp = int_Sqrt + l / 10e17;
    return sqrt_temp;
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
