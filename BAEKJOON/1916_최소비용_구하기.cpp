#include <bits/stdc++.h>
#define INF INT_MAX

using namespace std;

int N;
vector<pair<int, int>> edges[1001];

int dijkstra(int s, int t)
{
    vector<int> dijk(N + 1, INF);
    priority_queue<pair<int, int>> pq;
    pq.push({0, s});
    dijk[s] = 0;

    while (!pq.empty())
    {
        auto [distance, here] = pq.top();
        distance *= -1;
        pq.pop();

        if (here == t)
            break;

        if (distance > dijk[here])
            continue;

        for (auto &[there, cost] : edges[here])
        {
            if (dijk[there] <= distance + cost)
                continue;

            dijk[there] = distance + cost;
            pq.push({-dijk[there], there});
        }
    }

    return dijk[t];
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int M;
    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        edges[a].emplace_back(b, c);
    }

    int s, t;
    cin >> s >> t;

    cout << dijkstra(s, t) << '\n';

    return 0;
}