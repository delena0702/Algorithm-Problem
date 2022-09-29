#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    long long answer = 0;
    for (int i = 1, base = 1;; i++, base *= 10)
    {
        if (N < base * 10)
        {
            answer += (long long)i * (N - base + 1);
            break;
        }

        answer += (long long)i * base * 9;
    }
    
    cout << answer << '\n';

    return 0;
}