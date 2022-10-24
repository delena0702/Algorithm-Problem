#include <bits/stdc++.h>

using namespace std;

int R, C, K, arr[5][5], visited[5][5];
int darr[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}};

int dfs(int x, int y, int distance)
{
    if (x == C - 1 && y == 0)
        return (distance == K) ? 1 : 0;

    visited[y][x] = 1;

    int retval = 0;
    for (auto &[dx, dy] : darr)
    {
        int nx = x + dx, ny = y + dy;
        if (nx < 0 || nx >= C)
            continue;
        if (ny < 0 || ny >= R)
            continue;
        if (visited[ny][nx] || arr[ny][nx])
            continue;
        retval += dfs(nx, ny, distance + 1);
    }

    visited[y][x] = 0;
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> R >> C >> K;
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            char ch;
            cin >> ch;
            arr[i][j] = (ch == '.') ? 0 : 1;
        }
    }

    cout << dfs(0, R - 1, 1) << '\n';

    return 0;
}