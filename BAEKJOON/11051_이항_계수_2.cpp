#include <bits/stdc++.h>

using namespace std;

int dp[1001][1001];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, K, answer = 0;
    cin >> N >> K;

    for (int i = 0; i <= N; i++)
    {
        dp[i][0] = dp[i][i] = 1;
        for (int j = 1; j <= i - 1; j++)
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007;
    }

    cout << dp[N][K] << '\n';

    return 0;
}