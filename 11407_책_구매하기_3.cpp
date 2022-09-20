#include <bits/stdc++.h>
#define INF 987654321

using namespace std;

int N, M;
vector<pair<int, pair<int, int>>> edges[202];
vector<bool> inQ;
int flow[202][202], temp[101][101];
int dist[202], pre[202], pre_capacity[202];

void mcmf(void)
{
    for (int i = 0; i < N + M + 2; i++)
        for (int j = 0; j < N + M + 2; j++)
            flow[i][j] = 0;

    int answer[2] = {0, 0};

    while (true)
    {
        inQ.resize(N + M + 2, false);
        inQ[0] = true;

        for (int i = 0; i < N + M + 2; i++) {
            dist[i] = INF;
            pre[i] = -1;
        }
        dist[0] = 0;

        queue<int> q;
        q.push(0);
        while (!q.empty())
        {
            int here = q.front();
            q.pop();
            inQ[here] = false;

            for (auto &[there, p] : edges[here])
            {
                auto &[capacity, cost] = p;

                if (capacity - flow[here][there] <= 0)
                    continue;
                if (dist[there] <= dist[here] + cost)
                    continue;

                dist[there] = dist[here] + cost;
                pre[there] = here;
                pre_capacity[there] = capacity;

                if (!inQ[there]) {
                    q.push(there);
                    inQ[there] = true;
                }
            }
        }

        if (pre[N + M + 1] == -1)
            break;
        
        int f = INF;
        for (int there = N + M+1; there; there = pre[there]) {
            int here = pre[there] ;
            f = min(f, pre_capacity[there] - flow[here][there]);
        }

        for (int there = N + M+1; there; there = pre[there]) {
            int here = pre[there];
            flow[here][there] += f;
            flow[there][here] -= f;
        }

        answer[0] += f;
        answer[1] += f * dist[N + M + 1];
    }

    cout << answer[0] << '\n';
    cout << answer[1] << '\n';

    return;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        int a;
        cin >> a;
        edges[0].emplace_back(i, make_pair(a, 0));
        edges[i].emplace_back(0, make_pair(0, 0));
    }

    for (int i = 1; i <= M; i++)
    {
        int b;
        cin >> b;
        edges[N + i].emplace_back(N + M + 1, make_pair(b, 0));
        edges[N + M + 1].emplace_back(N + i, make_pair(0, 0));
    }

    for (int i = 1; i <= M; i++)
        for (int j = 1; j <= N; j++)
            cin >> temp[i][j];

    for (int i = 1; i <= M; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            int d;
            cin >> d;
            edges[j].emplace_back(N + i, make_pair(temp[i][j], d));
            edges[N + i].emplace_back(j, make_pair(0, -d));
        }
    }

    mcmf();

    return 0;
}