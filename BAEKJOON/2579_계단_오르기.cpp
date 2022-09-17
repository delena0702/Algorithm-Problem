#include <bits/stdc++.h>

using namespace std;

int arr[300];
int dp[300][2];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    dp[0][0] = arr[0], dp[0][1] = 0;
    dp[1][0] = arr[0] + arr[1], dp[1][1] = arr[1];

    for (int i = 2; i < N; i++)
    {
        dp[i][0] = dp[i - 1][1] + arr[i];
        dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + arr[i];
    }

    cout << max(dp[N - 1][0], dp[N - 1][1]) << '\n';

    return 0;
}
