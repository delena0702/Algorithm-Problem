#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int>> edges[100000];
vector<pair<int, int>> result;

vector<bool> visited;
int max_node, max_dist;
void dfs1(int here, int dist)
{
    visited[here] = true;

    if (max_dist < dist)
    {
        max_node = here;
        max_dist = dist;
    }

    int retval = 0;
    for (auto [there, cost] : edges[here])
    {
        if (visited[there])
            continue;
        dfs1(there, dist + cost);
    }
}

vector<bool> visited2;
int pre[100000], pre_cost[100000];
void dfs2(int here, int dist)
{
    visited2[here] = true;

    if (max_dist < dist)
    {
        max_node = here;
        max_dist = dist;
    }

    int retval = 0;
    for (auto [there, cost] : edges[here])
    {
        if (visited2[there])
            continue;
        dfs2(there, dist + cost);
        pre[there] = here;
        pre_cost[there] = cost;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, M, L;
    cin >> N >> M >> L;

    int a, b, t;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b >> t;
        edges[a].emplace_back(b, t);
        edges[b].emplace_back(a, t);
    }

    visited.resize(N);
    int answer = 0;
    for (int i = 0; i < N; i++)
    {
        if (visited[i])
            continue;

        max_dist = -1;
        dfs1(i, 0);
        int a = max_node;

        visited2.clear();
        visited2.resize(N);
        max_dist = -1;
        dfs2(a, 0);
        int b = max_node;
        int r = max_dist;

        int here = b, dist = 0, maximum = 0;
        while (here != a)
        {
            maximum = max(maximum, min(dist, r - dist));
            dist += pre_cost[here];
            here = pre[here];
        }
        result.emplace_back(r - maximum, maximum);
        answer = max(answer, r);
    }

    sort(result.begin(), result.end(), [](pair<int, int>& a, pair<int, int>& b) -> bool
         {
            if (a.first != b.first) return a.first > b.first;
            return a.second > b.second; });
    if (result.size() >= 2)
        answer = max(answer, result[0].first + result[1].first + L);
    if (result.size() >= 3)
        answer = max(answer, result[1].first + result[2].first + 2 * L);
    cout << answer << '\n';

    return 0;
}