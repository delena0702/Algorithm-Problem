#include <bits/stdc++.h>

using namespace std;

int dp[16], psum[16];

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    
    if (N % 2) {
        cout << 0 <<'\n';
        return 0;
    }

    dp[1] = 3, psum[1] = 3;
    for (int i = 2; i <= N / 2; i++)
    {
        dp[i] = 2 * psum[i - 1] + dp[i - 1] + 2;
        psum[i] = dp[i] + psum[i - 1];
    }
    cout << dp[N / 2] <<'\n';

    return 0;
}