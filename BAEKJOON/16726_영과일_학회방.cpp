#include <iostream>
#include <string>

#define LIMIT 50

using namespace std;

int N, M;
string input[LIMIT];
bool visited[LIMIT * LIMIT];
int match[LIMIT * LIMIT];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int dfs(int x, int y)
{
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i], ny = y + dy[i], ni = M * ny + nx;
        if (nx < 0 || nx >= M || ny < 0 || ny >= N)
            continue;
        if (visited[ni])
            continue;
        if (input[ny][nx] == 'X')
            continue;
        visited[ni] = true;
        if (match[ni] == -1 || dfs(match[ni] % M, match[ni] / M))
        {
            match[ni] = M * y + x;
            return 1;
        }
    }

    return 0;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    string temp;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input[i] = temp;
    }

    for (int i = 0; i < N * M; i++)
        match[i] = -1;
    int answer = 0;
    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (input[i][j] == '.')
                cnt++;
            if (i % 2 != j % 2 || input[i][j] == 'X')
                continue;
            for (int k = 0; k < N * M; k++)
                visited[k] = false;
            answer += dfs(j, i);
        }
    }

    cout << cnt - answer;

    return 0;
}