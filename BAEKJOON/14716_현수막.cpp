#include <bits/stdc++.h>

using namespace std;

int arr[250][250];
int darr[8][2] = {
    {1, -1},
    {1, 0},
    {1, 1},
    {-1, -1},
    {-1, 0},
    {-1, 1},
    {0, 1},
    {0, -1},
};

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int M, N;
    cin >> N >> M;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> arr[i][j];

    int answer = 0;
    for (int i = 0; i < N * M; i++)
    {
        int x = i % M, y = i / M;
        if (arr[y][x] == 0)
            continue;

        queue<pair<int, int>> q;
        q.push({x, y});
        arr[y][x] = 0;

        while (!q.empty())
        {
            auto [x, y] = q.front();
            q.pop();

            for (auto &[dx, dy] : darr)
            {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || nx >= M)
                    continue;
                if (ny < 0 || ny >= N)
                    continue;
                if (arr[ny][nx] == 0)
                    continue;

                arr[ny][nx] = 0;
                q.push({nx, ny});
            }
        }
        answer++;
    }

    cout << answer << '\n';

    return 0;
}