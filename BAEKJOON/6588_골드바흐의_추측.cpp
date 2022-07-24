#include <iostream>
#define MAX 1000000

using namespace std;

int main()
{
    bool isNotPrime[MAX/2];
    int num, x;

    cin.tie(NULL);
    cin.sync_with_stdio(false);

    for (int i=1; i<MAX/2; i++) {
        if (isNotPrime[i]) continue;
        for (int j=3*i+1; j<MAX/2; j+=(2*i+1))
            isNotPrime[j] = true;
    }

    while (true) {
        cin >> num;
        if (num == 0) return 0;
        for (x = 1; x < num/4 && (isNotPrime[x] || isNotPrime[num/2 - x - 1]); x++);
        cout << num << " = " << (2*x+1) << " + " << (num - 2*x - 1) << "\n";
    }
}
