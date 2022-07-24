#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

struct Edge
{
    int there;
    long long weight;
    bool isTrain;

    Edge(int there, long long weight, bool isTrain)
        : there(there), weight(weight), isTrain(isTrain) {}
};

vector<Edge> graph[SIZE + 1];
long long dijkstra[SIZE + 1];
bool visited[SIZE + 1];
bool isTrain[SIZE + 1];

int main(void)
{
    int N, M, K;
    cin >> N >> M >> K;

    int u, v, x;
    for (int i = 0; i < M; i++)
    {
        cin >> u >> v >> x;
        graph[u].push_back(Edge(v, x, false));
        graph[v].push_back(Edge(u, x, false));
    }

    int s, y;
    for (int i = 1; i <= K; i++)
    {
        cin >> s >> y;
        graph[1].push_back(Edge(s, y, true));
    }

    priority_queue<pair<long long, int>> pq;
    pq.push(make_pair(0, 1));

    for (int i = 2; i <= N; i++)
        dijkstra[i] = -1;

    int trainCount = 0;

    while (!pq.empty())
    {
        auto &p = pq.top();
        long long distance = (-p.first) / 2;
        bool train = (-p.first) % 2 == 1;
        int here = p.second;
        pq.pop();

        if (dijkstra[here] != distance)
            continue;
        if (visited[here])
            continue;

        visited[here] = true;

        if (train)
            trainCount++;

        for (auto &e : graph[here])
        {
            if (dijkstra[e.there] != -1 && dijkstra[e.there] < distance + e.weight)
                continue;
            if (visited[e.there])
                continue;

            dijkstra[e.there] = distance + e.weight;
            isTrain[e.there] = e.isTrain;
            pq.push(make_pair(-((distance + e.weight) * 2 + (e.isTrain ? 1 : 0)), e.there));
        }
    }

    printf("%d\n", K - trainCount);

    return 0;
}