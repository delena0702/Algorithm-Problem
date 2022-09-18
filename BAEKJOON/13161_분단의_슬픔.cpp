#include <bits/stdc++.h>

#define INF INT_MAX

using namespace std;

int N;
int flow[502][502];
int level[502];
int cnt[502];

bool bfs()
{
    fill(level, level + (N + 2), -1);
    level[0] = 0;

    queue<int> q;
    q.push(0);
    while (!q.empty())
    {
        int here = q.front();
        q.pop();

        for (int there = 0; there < N + 2; there++)
        {
            if (level[there] != -1)
                continue;
            if (flow[here][there] <= 0)
                continue;

            level[there] = level[here] + 1;
            q.push(there);
        }
    }

    return level[N + 1] != -1;
}

int dfs(int here, int f)
{
    if (here == N + 1)
        return f;

    for (int &there = cnt[here]; there <= N + 1; there++)
    {
        if (level[here] >= level[there])
            continue;
        if (flow[here][there] <= 0)
            continue;

        int nflow = dfs(there, min(f, flow[here][there]));
        if (nflow)
        {
            flow[here][there] -= nflow;
            flow[there][here] += nflow;
            return nflow;
        }
    }

    return 0;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        int team;
        cin >> team;
        if (team == 1)
            flow[0][i] = INF;
        if (team == 2)
            flow[i][N + 1] = INF;
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            int num;
            cin >> num;
            flow[i][j] = flow[j][i] = num;
        }
    }

    int answer = 0;
    while (bfs())
    {
        fill(cnt, cnt + (N + 2), 0);
        int res = 0;
        while (res = dfs(0, INF))
            answer += res;   
    }
    cout << answer << '\n';

    for (int i = 1; i <= N; i++)
        if (level[i] != -1)
            cout << i << ' ';
    cout << '\n';
    for (int i = 1; i <= N; i++)
        if (level[i] == -1)
            cout << i << ' ';
    cout << '\n';

    return 0;
}