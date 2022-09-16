#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int N, M;
int arr[505][505];
ll dp[505][505];
int darr[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

ll solve(int x, int y)
{
    if (x == M - 1 && y == N - 1)
        return 1;
    if (dp[y][x] != -1)
        return dp[y][x];

    ll &retval = dp[y][x];
    
    retval = 0;
    for (auto &[dx, dy] : darr)
    {
        int nx = x + dx, ny = y + dy;
        if (nx < 0 || nx >= M || ny < 0 || ny >= N)
            continue;
        if (arr[y][x] <= arr[ny][nx])
            continue;
        retval += solve(nx, ny);
    }
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
            dp[i][j] = -1;
        }
    }

    cout << solve(0, 0) << '\n';

    return 0;
}