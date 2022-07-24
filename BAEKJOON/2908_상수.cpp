#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int num1, num2;
    int result1 = 0, result2 = 0;

    cin >> num1 >> num2;

    do {
        result1 = 10 * result1 + num1 % 10;
    } while (num1 /= 10);
    
    do {
        result2 = 10 * result2 + num2 % 10;
    } while (num2 /= 10);

    cout << max(result1, result2);

    return 0;
}