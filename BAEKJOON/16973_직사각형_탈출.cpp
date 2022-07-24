#include <iostream>
#include <queue>
#include <utility>

#define SIZE 1000

using namespace std;

int N, M, W, H, sx, sy, fx, fy;
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {-1, 0, 1, 0};
bool arr[SIZE][SIZE], visited[SIZE][SIZE];

bool checkNext(int x, int y, int dir)
{
    switch (dir)
    {
    case 0:
        for (int i = 0; i < W; i++)
            if (arr[y - 1][x + i])
                return false;
        break;
    case 1:
        for (int i = 0; i < H; i++)
            if (arr[y + i][x + W])
                return false;
        break;
    case 2:
        for (int i = 0; i < W; i++)
            if (arr[y + H][x + i])
                return false;
        break;
    case 3:
        for (int i = 0; i < H; i++)
            if (arr[y + i][x - 1])
                return false;
        break;
    }

    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    int temp;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> temp;
            arr[i][j] = (temp == 1);
        }
    }
    cin >> H >> W >> sy >> sx >> fy >> fx;
    sx--, sy--, fx--, fy--;

    queue<pair<int, int>> q;
    q.push(make_pair(M * sy + sx, 0));
    visited[sy][sx] = true;

    int x, y, cnt, nx, ny;

    while (!q.empty())
    {
        pair<int, int> &p = q.front();
        q.pop();
        x = p.first % M, y = p.first / M, cnt = p.second;
        if (x == fx && y == fy)
        {
            cout << cnt;
            return 0;
        }

        for (int i = 0; i < 4; i++)
        {
            nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx + W - 1 >= M || ny < 0 || ny + H - 1 >= N)
                continue;
            if (visited[ny][nx])
                continue;
            if (!checkNext(x, y, i))
                continue;
            visited[ny][nx] = true;
            q.push(make_pair(M * ny + nx, cnt + 1));
        }
    }

    cout << -1;
    return 0;
}