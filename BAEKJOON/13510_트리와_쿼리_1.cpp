#include <bits/stdc++.h>

#define SIZE 100010

using namespace std;

struct Edge {
    int a, b, w;
};

vector<int> edges[SIZE + 1];
int edge_raw[SIZE + 1][3];
int edge_idx[SIZE + 1];
int N;

const int seg = 1 << 18;
int segtree[1 << 19];

void update(int idx, int value)
{
    idx |= seg;
    segtree[idx] = value;
    while (idx >>= 1)
        segtree[idx] = max(segtree[idx << 1], segtree[idx << 1 | 1]);
}

int query(int l, int r)
{
    int retval = 0;
    for (l |= seg, r |= seg; l <= r; l >>= 1, r >>= 1)
    {
        if (l & 1)
            retval = max(retval, segtree[l++]);
        if (~r & 1)
            retval = max(retval, segtree[r--]);
    }
    return retval;
}

vector<int> tree[SIZE + 1];
vector<bool> check;
int depth[SIZE + 1], parent[SIZE + 1], sz[SIZE + 1];
int order[SIZE + 1], top[SIZE + 1];

void dfs(int here)
{
    check[here] = true;
    for (auto & there : edges[here]) {
        if (check[there])
            continue;
        tree[here].push_back(there);
        dfs(there);
    }
}

void dfs1(int here)
{
    sz[here] = 1;
    for (auto & there : tree[here]) {
        depth[there] = depth[here] + 1;
        parent[there] = here;
        dfs1(there);

        sz[here] += sz[there];
        if (sz[there] > sz[tree[here][0]])
            swap(there, tree[here][0]);
    }
}

int counter = 0;
void dfs2(int here)
{
    order[here] = ++counter;
    for (auto &there : tree[here])
    {
        top[there] = ((there == tree[here][0]) ? top[here] : there);
        dfs2(there);
    }
}

void hld_update(int idx, int value)
{
    update(order[idx], value);
}

int hld_query(int a, int b)
{
    int retval = 0;
    while (top[a] != top[b])
    {
        if (depth[top[a]] < depth[top[b]])
            swap(a, b);

        retval = max(retval, query(order[top[a]], order[a]));
        a = parent[top[a]];
    }
    if (depth[a] > depth[b])
        swap(a, b);
    retval = max(retval, query(order[a] + 1, order[b]));
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N - 1; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        edges[u].push_back(v);
        edges[v].push_back(u);

        edge_raw[i][0] = u;
        edge_raw[i][1] = v;
        edge_raw[i][2] = w;
    }

    check.resize(N + 1);
    dfs(1);
    depth[1] = 1;
    dfs1(1);
    top[1] = 1;
    dfs2(1);

    for (int i = 0; i < N - 1; i++)
    {
        auto &[a, b, w] = edge_raw[i];
        edge_idx[i + 1] = (depth[a] > depth[b]) ? a : b;
        hld_update(edge_idx[i + 1], w);
    }

    int M;
    cin >> M;
    for (int i = 0; i < M; i++)
    {
        int o, a, b;
        cin >> o >> a >> b;

        switch (o)
        {
        case 1:
            hld_update(edge_idx[a], b);
            break;

        case 2:
            cout << hld_query(a, b) << '\n';
            break;
        }
    }

    return 0;
}