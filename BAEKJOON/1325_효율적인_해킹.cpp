#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> edges[10001];
bool visited[10001];
int dp[10001], order[10001];

int dfs(int here)
{
    if (visited[here])
        return 0;
    visited[here] = true;

    int retval = 1;
    for (int there : edges[here])
        retval += dfs(there);
    return retval;
}

bool comp(int a, int b)
{
    if (dp[a] != dp[b])
        return dp[a] > dp[b];
    return a < b;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;

    int a, b;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        edges[b].push_back(a);
    }

    for (int i = 1; i <= N; i++)
        dp[i] = -1;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++)
            visited[j] = false;
        dp[i] = dfs(i);
    }

    for (int i = 1; i <= N; i++)
        order[i] = i;
    sort(order + 1, order + N + 1, comp);

    cout << order[1] << ' ';
    for (int i = 2; i <= N; i++)
    {
        if (dp[order[i]] != dp[order[i - 1]])
            break;
        cout << order[i] << ' ';
    }
    cout << '\n';

    return 0;
}