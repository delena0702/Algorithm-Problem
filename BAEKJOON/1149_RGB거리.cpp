#include <bits/stdc++.h>

using namespace std;

int arr[1000][3], dp[1000][3];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < 3; j++)
            cin >> arr[i][j];

    for (int i = 0; i < 3; i++)
        dp[0][i] = arr[0][i];

    for (int i = 1; i < N; i++)
    {
        dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2]);
        dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1]);
    }

    int answer = INT_MAX;
    for (int i = 0; i < 3; i++)
        answer = min(answer, dp[N - 1][i]);
    cout << answer << '\n';

    return 0;
}