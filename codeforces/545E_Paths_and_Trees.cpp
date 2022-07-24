#include <bits/stdc++.h>

#define SIZE 300000

using namespace std;

struct Edge
{
    int there;
    long long weight;
    int index;

    Edge(int there, int weight, int index)
        : there(there), weight(weight), index(index)
    {
    }
};

vector<Edge> graph[SIZE + 1];
bool visited[SIZE + 1];
long long dijk[SIZE + 1];
int pre[SIZE + 1];
int pre_edge[SIZE + 1];

int main(void)
{
    int N, M;
    cin >> N >> M;

    int a, b, w;
    for (int i = 1; i <= M; i++)
    {
        cin >> a >> b >> w;
        graph[a].push_back(Edge(b, w, i));
        graph[b].push_back(Edge(a, w, i));
    }

    int u;
    cin >> u;

    for (int i = 1; i <= N; i++)
        dijk[i] = -1;
    dijk[u] = 0;

    priority_queue<pair<long long, int>> pq;
    pq.push(make_pair(0, u));

    while (!pq.empty())
    {
        auto &edge = pq.top();
        long long distance = -edge.first;
        int here = edge.second;
        pq.pop();

        if (visited[here])
            continue;
        if (distance != dijk[here])
            continue;

        visited[here] = true;

        for (auto &e : graph[here])
        {
            if (dijk[e.there] != -1 && dijk[e.there] < distance + e.weight)
                continue;
            if (visited[e.there])
                continue;

            dijk[e.there] = distance + e.weight;
            pre[e.there] = here;
            pre_edge[e.there] = e.index;

            pq.push(make_pair(-(distance + e.weight), e.there));
        }
    }

    long long answer = 0;
    for (int i = 1; i <= N; i++)
        answer += dijk[i] - dijk[pre[i]];
    printf("%lld\n", answer);

    sort(pre_edge + 1, pre_edge + N + 1);
    for (int i = 2; i <= N; i++)
        printf("%d ", pre_edge[i]);

    return 0;
}