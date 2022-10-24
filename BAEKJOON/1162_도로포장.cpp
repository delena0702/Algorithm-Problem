#include <bits/stdc++.h>
#define INF LLONG_MAX
using namespace std;

int N, M, K;
vector<pair<int, int>> edges[10001];

struct Dist
{
    int here, k;
    long long distance;
    bool operator<(const Dist &d) const
    {
        return distance > d.distance;
    }
};

long long dist[10001][21];

long long dijkstra()
{
    for (int i = 1; i <= N; i++)
        for (int j = 0; j <= K; j++)
            dist[i][j] = INF;

    priority_queue<Dist> pq;
    pq.push({1, 0, 0});
    while (!pq.empty())
    {
        auto [here, k, distance] = pq.top();
        pq.pop();

        if (here == N)
            return distance;

        if (distance > dist[here][k])
            continue;

        for (auto [there, cost] : edges[here])
        {
            if (dist[there][k] > distance + cost) {
                dist[there][k] = distance + cost;
                pq.push({there, k, distance + cost});
            }

            if (k + 1 <= K && dist[there][k + 1] > distance) {
                dist[there][k + 1] = distance;
                pq.push({there, k + 1, distance});
            }
        }
    }

    return 0;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M >> K;
    int a, b, c;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b >> c;
        edges[a].push_back({b, c});
        edges[b].push_back({a, c});
    }

    cout << dijkstra() << '\n';

    return 0;
}