#include <bits/stdc++.h>
#define SIZE 100000

using namespace std;

vector<int> edges[SIZE + 1], trees[SIZE + 1], parents[SIZE + 1];
vector<bool> visited;
int depth[SIZE + 1];

int lca(int a, int b)
{
    if (depth[a] < depth[b])
        swap(a, b);

    int d = depth[a] - depth[b];
    for (int i = 0; d; i++)
    {
        if (d & (1 << i))
        {
            a = parents[a][i];
            d -= 1 << i;
        }
    }

    while (a != b)
    {
        int s = 0, e = parents[a].size();
        while (s < e)
        {
            int m = (s + e) / 2;
            if (parents[a][m] == parents[b][m])
                e = m;
            else
                s = m + 1;
        }

        if (s == 0)
        {
            a = b = parents[a][0];
            continue;
        }

        a = parents[a][e - 1];
        b = parents[b][e - 1];
    }

    return a;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, a, b;
    cin >> N;
    for (int i = 0; i < N - 1; i++)
    {
        cin >> a >> b;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }

    queue<int> q;
    q.push(1);
    visited.resize(N + 1, false);
    visited[1] = true;

    while (!q.empty())
    {
        int here = q.front();
        q.pop();

        for (int there : edges[here])
        {
            if (visited[there])
                continue;
            visited[there] = true;

            trees[here].push_back(there);
            parents[there].push_back(here);
            depth[there] = depth[here] + 1;
            q.push(there);

            int d = 0, node = here;
            while (true)
            {
                if (d >= parents[node].size())
                    break;
                node = parents[node][d];
                parents[there].push_back(node);
                d++;
            }
        }
    }

    int Q, c;
    cin >> Q;
    for (int i = 0; i < Q; i++)
    {
        cin >> a >> b >> c;
        pair<int, int> arr[3] = {{a, b}, {a, c}, {b, c}};
        int answer[3];
        bool check = false;

        for (int j = 0; j < 3; j++)
        {
            auto [x, y] = arr[j];
            int p = lca(x, y);
            int d = depth[x] + depth[y] - 2 * depth[p];

            if (d % 2)
            {
                check = true;
                break;
            }

            if (depth[x] < depth[y])
                swap(x, y);

            d /= 2;
            for (int k = 0; d; k++)
            {
                if (d & (1 << k))
                {
                    x = parents[x][k];
                    d -= 1 << k;
                }
            }

            answer[j] = x;
        }

        if (check)
        {
            cout << -1 << '\n';
            continue;
        }

        if (answer[0] == answer[1] || answer[0] == answer[2])
            cout << answer[0] << '\n';
        else if (answer[1] == answer[2])
            cout << answer[1] << '\n';
        else
            cout << -1 << '\n';
    }

    return 0;
}