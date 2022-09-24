#include <bits/stdc++.h>
#define INF INT_MAX

using namespace std;

int N;
char arr[50][50];
int dijk[50][50];
int darr[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int bfs(pair<int, int> s, pair<int, int> t)
{
    queue<pair<int, int>> q;
    q.push({s.first, s.second});

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            dijk[i][j] = INF;
    dijk[s.second][s.first] = 0;

    while (!q.empty())
    {
        auto [x, y] = q.front();
        q.pop();

        if (x == t.first && y == t.second)
            break;

        vector<pair<int, int>> next;
        for (auto [dx, dy] : darr)
        {
            int nx, ny;
            bool check = true;
            for (nx = x + dx, ny = y + dy;; nx += dx, ny += dy)
            {
                if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                    break;
                if (arr[ny][nx] == '*')
                    break;
                if (arr[ny][nx] != '.')
                    next.push_back({nx, ny});
            }
        }

        for (auto [nx, ny] : next)
        {
            if (dijk[ny][nx] <= dijk[y][x] + 1)
                continue;

            dijk[ny][nx] = dijk[y][x] + 1;
            q.push({nx, ny});
        }
    }

    return dijk[t.second][t.first] - 1;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    vector<pair<int, int>> door;
    for (int i = 0; i < N; i++)
    {
        string str;
        cin >> str;

        for (int j = 0; j < N; j++)
        {
            arr[i][j] = str[j];
            if (arr[i][j] == '#')
                door.emplace_back(j, i);
        }
    }

    cout << bfs(door[0], door[1]) << '\n';

    return 0;
}