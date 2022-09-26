#include <bits/stdc++.h>

using namespace std;

int arr[100][100][100];
int darr[6][3] = {
    {1, 0, 0},
    {-1, 0, 0},
    {0, 1, 0},
    {0, -1, 0},
    {0, 0, 1},
    {0, 0, -1}};

struct Pos
{
    int x, y, z;
};

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int M, N, H;
    cin >> M >> N >> H;

    queue<Pos> q;
    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
            {
                cin >> arr[i][j][k];

                if (arr[i][j][k] == 1)
                    q.push({k, j, i});
            }
        }
    }

    int answer = 1;
    while (!q.empty())
    {
        auto [x, y, z] = q.front();
        q.pop();

        for (auto &[dx, dy, dz] : darr)
        {
            int nx = x + dx, ny = y + dy, nz = z + dz;
            if (nx < 0 || nx >= M)
                continue;
            if (ny < 0 || ny >= N)
                continue;
            if (nz < 0 || nz >= H)
                continue;
            if (arr[nz][ny][nx])
                continue;

            arr[nz][ny][nx] = arr[z][y][x] + 1;
            answer = max(answer, arr[nz][ny][nx]);

            q.push({nx, ny, nz});
        }
    }

    bool check = true;
    for (int i = 0; check && i < H; i++)
        for (int j = 0; check && j < N; j++)
            for (int k = 0; check && k < M; k++)
                if (arr[i][j][k] == 0)
                    check = false;

    if (check)
        cout << answer - 1 << '\n';
    else
        cout << -1 << '\n';

    return 0;
}