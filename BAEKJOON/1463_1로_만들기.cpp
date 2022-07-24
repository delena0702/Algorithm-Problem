#include <bits/stdc++.h>

#define SIZE 1000000

using namespace std;

int dp[SIZE + 1];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    dp[1] = 0;
    for (int i = 2; i <= N; i++)
    {
        dp[i] = dp[i - 1] + 1;
        if (i % 3 == 0)
            dp[i] = min(dp[i], dp[i / 3] + 1);
        if (i % 2 == 0)
            dp[i] = min(dp[i], dp[i / 2] + 1);
    }

    cout << dp[N] << endl;

    return 0;
}