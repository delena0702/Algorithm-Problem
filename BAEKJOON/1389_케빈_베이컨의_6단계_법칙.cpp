#include <bits/stdc++.h>

#define SIZE 100
#define INF 987654321

using namespace std;

int dp[SIZE + 1][SIZE + 1];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
            dp[i][j] = INF;
        dp[i][i] = 0;
    }

    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        dp[a][b] = 1;
        dp[b][a] = 1;
    }

    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            for (int k = 1; k <= N; k++)
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k]);

    int answer = -1;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 2; j <= N; j++)
            dp[i][1] += dp[i][j];
        if (answer == -1 || dp[i][1] < dp[answer][1])
            answer = i;
    }

    cout << answer << endl;

    return 0;
}