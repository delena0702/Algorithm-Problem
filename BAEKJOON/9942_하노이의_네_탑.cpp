#include <bits/stdc++.h>

#define SIZE 1000

using namespace std;

unsigned long long dp[SIZE + 1];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    dp[1] = 1;
    for (int i = 2; i <= 1000; i++)
    {
        dp[i] = ULLONG_MAX;
        for (int j = 1; j < min(i, 64); j++)
            dp[i] = min(dp[i], 2 * dp[i - j] + ((1ULL << j) - 1));
    }

    int N = 0;
    for (int t = 1; cin >> N; t++)
        cout << "Case " << t << ": " << dp[N] << endl;

    return 0;
}