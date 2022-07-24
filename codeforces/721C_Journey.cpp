#include <bits/stdc++.h>

#define SIZE 5000
#define INF -1

using namespace std;

vector<pair<int, long long>> graph[SIZE + 1];
long long dp[SIZE + 1][SIZE + 1];
short pre[SIZE + 1][SIZE + 1];
int answer = 0;

void dfs(int here, int visitedCount)
{
    pre[here][visitedCount] = -1;

    if (visitedCount <= 1)
        return;

    for (pair<int, long long> &p : graph[here])
    {
        int there = p.first;
        long long weight = p.second;

        if (pre[there][visitedCount - 1] == 0)
            dfs(there, visitedCount - 1);

        if (dp[there][visitedCount - 1] != INF &&
            (dp[here][visitedCount] == INF ||
             dp[there][visitedCount - 1] + weight < dp[here][visitedCount]))
        {
            dp[here][visitedCount] = dp[there][visitedCount - 1] + weight;
            pre[here][visitedCount] = there;
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, u, v;
    long long T, t;
    cin >> N >> M >> T;

    for (int i = 0; i < M; i++)
    {
        cin >> u >> v >> t;
        graph[v].push_back(make_pair(u, t));
    }

    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            dp[i][j] = INF;

    pre[1][1] = 1;
    dp[1][1] = 0;

    for (int i = 0; i <= N; i++)
    {
        dfs(N, i);

        if (dp[N][i] != INF && dp[N][i] <= T)
            answer = i;
    }

    printf("%d\n", answer);
    stack<int> s;
    int cnt = answer;
    for (int here = N; cnt; here = pre[here][cnt--])
        s.push(here);

    while (!s.empty())
    {
        printf("%d ", s.top());
        s.pop();
    }

    return 0;
}