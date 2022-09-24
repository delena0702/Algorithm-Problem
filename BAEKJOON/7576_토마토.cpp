#include <bits/stdc++.h>

using namespace std;

int arr[1000][1000];
int darr[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int M, N;
    cin >> M >> N;

    queue<pair<int, int>> q;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 1)
                q.push({j, i});
        }
    }

    while (!q.empty())
    {
        auto [x, y] = q.front();
        q.pop();

        for (auto [dx, dy] : darr)
        {
            int nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= M || ny < 0 || ny >= N)
                continue;
            if (arr[ny][nx])
                continue;

            arr[ny][nx] = arr[y][x] + 1;
            q.push({nx, ny});
        }
    }

    int answer = 1;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (arr[i][j] == -1)
                continue;

            if (arr[i][j] == 0)
            {
                answer = 0;
                break;
            }

            answer = max(answer, arr[i][j]);
        }

        if (answer == 0)
            break;
    }

    cout << answer - 1 << '\n';

    return 0;
}