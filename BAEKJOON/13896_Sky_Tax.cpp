#include <bits/stdc++.h>

using namespace std;

vector<int> edges[100001];

vector<bool> visited;
vector<int> tree[100001];
void dfs1(int here)
{
    visited[here] = true;

    for (int there : edges[here])
    {
        if (visited[there])
            continue;
        visited[there] = true;

        tree[here].push_back(there);
        dfs1(there);
    }
}

int order[100001], in[100001], out[100001], cnt;
void dfs2(int here)
{
    in[here] = ++cnt;
    for (int there : tree[here])
        dfs2(there);
    out[in[here]] = cnt;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    int N, Q, R;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> Q >> R;

        for (int i = 1; i <= N; i++)
            edges[i].clear();

        int a, b;
        for (int i = 0; i < N - 1; i++)
        {
            cin >> a >> b;
            edges[a].push_back(b);
            edges[b].push_back(a);
        }

        visited.clear();
        visited.resize(N + 1, false);
        for (int i = 1; i <= N; i++)
            tree[i].clear();
        dfs1(1);
        cnt = 0;
        dfs2(1);

        cout << "Case #" << t << ":\n";

        for (int i = 0; i < Q; i++)
        {
            cin >> a >> b;
            if (a == 0)
            {
                R = b;
                continue;
            }

            if (in[b] > in[R] || in[R] > out[in[b]])
            {
                cout << out[in[b]] - in[b] + 1 << '\n';
                continue;
            }

            if (b == R)
            {
                cout << N << '\n';
                continue;
            }

            int idx = in[b] + 1;
            while (true)
            {
                if (idx <= in[R] && in[R] <= out[idx])
                    break;
                idx = out[idx] + 1;
            }

            cout << N - (out[idx] - idx + 1) << '\n';
        }
    }

    return 0;
}