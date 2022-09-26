#include <bits/stdc++.h>

using namespace std;

int arr[10000], dp[10000];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    dp[0] = arr[0], dp[1] = arr[0] + arr[1];
    dp[2] = max(arr[0] + arr[2], max(arr[1] + arr[2], arr[0] + arr[1]));

    for (int i = 3; i < N; i++)
    {
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);
        dp[i] = max(dp[i], dp[i - 1]);
    }

    cout << dp[N - 1] << '\n';

    return 0;
}