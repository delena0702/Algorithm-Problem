#include <bits/stdc++.h>

using namespace std;

int N, K;
int arr[105];
int dp[10005];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> K;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    dp[0] = 1;
    for (int i = 0; i < N; i++)
        for (int j = arr[i]; j <= K; j++)
            dp[j] += dp[j - arr[i]];

    cout << dp[K] << '\n';

    return 0;
}