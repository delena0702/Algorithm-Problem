#include <bits/stdc++.h>

using namespace std;

int N, M;
int uf[1005];
vector<pair<int, pair<int, int>>> edges;

int group(int here)
{
    return (here == uf[here]) ? here : group(uf[here]);
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
        uf[i] = i;

    for (int i = 0; i < M; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        edges.emplace_back(c, make_pair(a, b));
    }

    sort(edges.begin(), edges.end());

    int answer = 0, cnt = 0;
    for (auto &[cost, pairs] : edges)
    {
        auto &[a, b] = pairs;
        if (group(a) == group(b))
            continue;
        uf[group(a)] = group(b);
        answer += cost;
        cnt++;
    }

    cout << answer << '\n';

    return 0;
}