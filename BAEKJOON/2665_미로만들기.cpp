#include <iostream>
#include <string>
#include <queue>
#include <utility>

#define INF 987654321

using namespace std;

int N;
int dp[50][50];
string input[50];
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {-1, 0, 1, 0};

int min(int a, int b) {
    return a < b ? a : b;
}

int aaaaa = 10;
int bfs(void) {
    queue<pair<int, int>> q;
    int answer = INF;
    q.push(make_pair(0, 0));

    while (!q.empty()) {
        pair<int, int> now = q.front();
        int x = now.first % N, y = now.first / N, cnt = now.second;
        q.pop();

        if (x == N-1 && y == N-1) {
            answer = min(answer, cnt);
            continue;
        }

        if (dp[y][x] <= cnt)
            continue;

        dp[y][x] = cnt;
        for (int i=0; i<4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                continue;
            q.push(make_pair(ny * N + nx, cnt + (input[ny][nx] == '0' ? 1 : 0)));
        }
    }

    return answer;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    for (int i = 0; i < N; i++) {
        string temp;
        cin >> temp;
        input[i] = temp;
    }

    for (int i=0;i<N; i++)
        for (int j=0;j<N; j++)
            dp[i][j] = INF;
    
    cout << bfs();

    return 0;
}