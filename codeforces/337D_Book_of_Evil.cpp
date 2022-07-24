#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

vector<int> tree[SIZE + 1];
bool selected[SIZE + 1];
bool visited[SIZE + 1];
int dis[SIZE + 1][2];

int N, M, D;

int dfs1(int here)
{
    visited[here] = true;

    dis[here][0] = dis[here][1] = selected[here] ? 0 : -1;

    for (int there : tree[here])
    {
        if (visited[there])
            continue;

        int temp = dfs1(there);
        temp = (temp == -1) ? -1 : temp + 1;

        if (temp > dis[here][0])
        {
            dis[here][1] = dis[here][0];
            dis[here][0] = temp;
        }
        else if (temp > dis[here][1])
            dis[here][1] = temp;
    }
    return dis[here][0];
}

void dfs2(int here, int val)
{
    visited[here] = true;

    if (val > dis[here][0])
    {
        dis[here][1] = dis[here][0];
        dis[here][0] = val;
    }
    else if (val > dis[here][1])
        dis[here][1] = val;

    for (int there : tree[here])
    {
        if (visited[there])
            continue;

        int temp = dis[here][(dis[here][0] == dis[there][0] + 1) ? 1 : 0];
        temp = (temp == -1) ? -1 : temp + 1;
        dfs2(there, temp);
    }
}

int main(void)
{
    cin >> N >> M >> D;

    for (int i = 0; i < M; i++)
    {
        int temp;
        cin >> temp;
        selected[temp] = true;
    }

    for (int i = 0; i < N - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    dfs1(1);
    for (int i = 1; i <= N; i++)
        visited[i] = false;
    dfs2(1, -1);
    int cnt = 0;
    for (int i = 1; i <= N; i++)
        if (dis[i][0] <= D)
            cnt++;
    printf("%d\n", cnt);

    return 0;
}