#include <bits/stdc++.h>
#define INF INT_MAX

using namespace std;

int N;
vector<pair<int, int>> edges[1001];

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

    priority_queue<pair<int, int>> pq;
    pq.push({0, s});

    vector<int> dijk(N + 1, INF);
    vector<int> pre(N + 1, 0);
    dijk[s] = 0;

    while (!pq.empty())
    {
        auto [distance, here] = pq.top();
        pq.pop();

        if (here == t)
            break;

        if (distance > dijk[here])
            continue;

        for (auto [there, cost] : edges[here])
        {
            if (dijk[there] <= dijk[here] + cost)
                continue;

            dijk[there] = dijk[here] + cost;
            pre[there] = here;
            pq.push({-dijk[there], there});
        }
    }

    cout << dijk[t] << '\n';

    vector<int> answer;
    for (int there = t; there; there = pre[there])
        answer.push_back(there);

    cout << answer.size() << '\n';
    for (auto it = answer.rbegin(); it != answer.rend(); it++)
        cout << *it << ' ';
    cout << '\n';

    return 0;
}