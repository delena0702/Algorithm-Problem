#include <bits/stdc++.h>
#define SIZE 30000

using namespace std;

int N;

struct Query
{
    char op;
    int a, b;
};

struct UnionFind
{
    int arr[SIZE + 1];

    UnionFind()
    {
        clear();
    }

    int get(int idx)
    {
        if (idx == arr[idx])
            return idx;
        return arr[idx] = get(arr[idx]);
    }

    void clear()
    {
        for (int i = 1; i <= SIZE; i++)
            arr[i] = i;
    }
};

struct FenwickTree
{
    int arr[SIZE + 1];

    void update(int idx, int value)
    {
        while (idx <= N)
        {
            arr[idx] += value;
            idx += -idx & idx;
        }
    }

    int sum(int idx)
    {
        int retval = 0;
        while (idx)
        {
            retval += arr[idx];
            idx -= -idx & idx;
        }
        return retval;
    }
};

vector<Query> queries;
UnionFind uf;
vector<int> edges[SIZE + 1];
vector<int> tree[SIZE + 1];
vector<bool> visited;
FenwickTree fwtree;
int nodes[SIZE + 1];

void dfs1(int here)
{
    if (here == 1)
    {
        visited.resize(N + 1, false);
        visited[here] = true;
    }

    for (int there : edges[here])
    {
        if (visited[there])
            continue;
        visited[there] = true;
        tree[here].push_back(there);
        dfs1(there);
    }
}

int sz[SIZE + 1], depth[SIZE + 1], parent[SIZE + 1];
void dfs2(int here)
{
    sz[here] = 1;
    for (int &there : tree[here])
    {
        depth[there] = depth[here] + 1;
        parent[there] = here;

        dfs2(there);

        sz[here] += sz[there];
        if (sz[there] > sz[tree[here][0]])
            swap(there, tree[here][0]);
    }
}

int top[SIZE + 1], in[SIZE + 1], out[SIZE + 1], cnt;
void dfs3(int here)
{
    if (here == 1)
    {
        top[here] = 1;
    }

    in[here] = ++cnt;
    for (int there : tree[here])
    {
        top[there] = (there == tree[here][0]) ? top[here] : there;
        dfs3(there);
    }
    out[here] = cnt;
}

int hld_query(int a, int b) {
    int retval = 0;
    while (top[a] != top[b])
    {
        if (depth[top[a]] < depth[top[b]])
            swap(a, b);
        retval += fwtree.sum(in[a]) - fwtree.sum(in[top[a]] - 1);
        a = parent[top[a]];
    }

    if (depth[a] < depth[b])
        swap(a, b);
    retval += fwtree.sum(in[a]) - fwtree.sum(in[b] - 1);
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> nodes[i];

    int Q, a, b;
    string str;
    cin >> Q;
    for (int i = 0; i < Q; i++)
    {
        cin >> str >> a >> b;
        queries.push_back({str[0], a, b});

        if (str[0] == 'b' && uf.get(a) != uf.get(b))
        {
            edges[a].push_back(b);
            edges[b].push_back(a);
            uf.arr[uf.get(a)] = uf.get(b);
        }
    }

    for (int i = 2; i <= N; i++)
    {
        if (uf.get(1) != uf.get(i))
        {
            edges[1].push_back(i);
            edges[i].push_back(1);
            uf.arr[uf.get(1)] = uf.get(i);
        }
    }

    dfs1(1);
    dfs2(1);
    dfs3(1);

    for (int i = 1; i <= N; i++)
        fwtree.update(in[i], nodes[i]);
    uf.clear();

    for (int i = 0; i < Q; i++)
    {
        auto [ch, a, b] = queries[i];

        switch (ch)
        {
        case 'b':
            if (uf.get(a) == uf.get(b))
                cout << "no\n";
            else
            {
                uf.arr[uf.get(a)] = uf.get(b);
                cout << "yes\n";
            }
            break;

        case 'p':
        {
            int pre = fwtree.sum(in[a]) - fwtree.sum(in[a] - 1);
            fwtree.update(in[a], b - pre);
            break;
        }

        case 'e':
            if (uf.get(a) == uf.get(b))
                cout << hld_query(a, b) << '\n';
            else
                cout << "impossible\n";
            break;
        }
    }

    return 0;
}