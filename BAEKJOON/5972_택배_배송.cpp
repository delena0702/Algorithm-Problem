#include <bits/stdc++.h>
#define INF INT_MAX

using namespace std;

int N;
vector<pair<int, int>> edges[50001];

int dijkstra(int s, int t) {
    priority_queue<pair<int, int>> pq;
    vector<int> dijk(N + 1, INF);
    dijk[s] = 0;
    pq.push({0, s});

    while (!pq.empty()) {
        auto [distance, here] = pq.top();
        pq.pop();

        if (distance > dijk[here])
            continue;

        for (auto [there, cost] : edges[here]) {
            if (dijk[there] <= dijk[here] + cost)
                continue;
            dijk[there] = dijk[here] + cost;
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
        edges[b].emplace_back(a, c);
    }

    cout << dijkstra(1, N) << '\n';

    return 0;
}