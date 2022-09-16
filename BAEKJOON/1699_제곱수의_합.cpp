#include <bits/stdc++.h>

#define SIZE 100000
#define INF INT_MAX

using namespace std;

int dp[SIZE + 1];

int main(void) {
    int N;
    cin >> N;

    dp[0] = 0;
    for (int i = 1; i <= N; i++)
    {
        dp[i] = INF;
        for (int j = 1; j * j <= i; j++)
            dp[i] = min(dp[i], dp[i - j * j] + 1);
    }

    cout << dp[N] << endl;

    return 0;
}