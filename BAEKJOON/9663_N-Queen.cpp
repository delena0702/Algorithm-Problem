#include <iostream>
#define ARRAY_SIZE 30
using namespace std;

int N;
bool c1[ARRAY_SIZE], c2[ARRAY_SIZE], c3[ARRAY_SIZE];

int _check(int now) {
    if (now == N) return 1;
    
    int retval = 0;
    for (int i=0; i<N; i++) {
        if (!c1[i] && !c2[i - now + N-1] && !c3[i + now]) {
            c1[i] = c2[i - now + N-1] = c3[i + now] = true;
            retval += _check(now + 1);
            c1[i] = c2[i - now + N-1] = c3[i + now] = false;
        }
    }
    return retval;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> N;
    cout << _check(0);

    return 0;
}