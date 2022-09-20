#include <bits/stdc++.h>
#define INF 987654321

using namespace std;

int N;
int nodes[501];
int floyd[501][501];
vector<pair<int, pair<int, int>>> edges[1002];

int flow[1002][1002];
vector<bool> inQ;
int dist[1002];
int pre[1002];

int mcmf(void)
{
    int answer = 0;

    for (int i = 0; i < 2 * N + 2; i++)
        for (int j = 0; j < 2 * N + 2; j++)
            flow[i][j] = 0;

    while (true)
    {
        queue<int> q;
        q.push(0);

        for (int i = 0; i < 2 * N + 2; i++)
        {
            dist[i] = INF;
            pre[i] = -1;
        }
        dist[0] = 0;

        inQ.resize(2 * N + 2, false);
        inQ[0] = true;

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

                if (!inQ[there])
                {
                    q.push(there);
                    inQ[there] = true;
                }
            }
        }

        if (pre[2 * N + 1] == -1)
            break;

        for (int there = 2 * N + 1; there; there = pre[there])
        {
            int here = pre[there];
            flow[here][there]++;
            flow[there][here]--;
        }

        answer += dist[2 * N + 1];
    }

    return answer;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    while (T--)
    {
        int M;
        cin >> N >> M;

        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                floyd[i][j] = ((i == j) ? 0 : INF);

        for (int i = 0; i < 2 * N + 2; i++)
            edges[i].clear();

        for (int i = 0; i < M; i++)
        {
            int x, y;
            cin >> x >> y;
            floyd[x][y] = floyd[y][x] = 1;
        }

        for (int i = 1; i <= N; i++)
            cin >> nodes[i];

        for (int i = 1; i <= N; i++)
        {
            int num;
            cin >> num;
            if (nodes[i] - num == -1)
            {
                edges[0].emplace_back(i, make_pair(1, 0));
                edges[i].emplace_back(0, make_pair(0, 0));
            }

            if (nodes[i] - num == 1)
            {
                edges[N + i].emplace_back(2 * N + 1, make_pair(1, 0));
                edges[2 * N + 1].emplace_back(N + i, make_pair(0, 0));
            }
        }

        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                for (int k = 1; k <= N; k++)
                    floyd[j][k] = min(floyd[j][k], floyd[j][i] + floyd[i][k]);

        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                edges[i].emplace_back(N + j, make_pair(INF, floyd[i][j]));
                edges[N + j].emplace_back(i, make_pair(0, -floyd[i][j]));
            }
        }

        cout << mcmf() << '\n';
    }

    return 0;
}