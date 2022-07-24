#include <bits/stdc++.h>

#define SIZE 200000

using namespace std;

vector<pair<int, bool>> tree[SIZE + 1];
int result[SIZE + 1];
bool visited[SIZE + 1];

int dfs(int now = 1, int offset = 0)
{
    visited[now] = true;
    result[now] = offset;

    int retval = 0;
    for (const auto &edge : tree[now])
    {
        if (visited[edge.first])
            continue;

        retval += dfs(edge.first, offset + (edge.second ? -1 : 1));
        retval += edge.second ? 1 : 0;
    }

    return retval;
}

int main(void)
{
    int N;
    cin >> N;
    for (int i = 0; i < N - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(make_pair(b, false));
        tree[b].push_back(make_pair(a, true));
    }

    int sum = dfs();
    int answer = result[1];

    for (int i = 1; i <= N; i++)
        answer = min(answer, result[i]);

    printf("%d\n", answer + sum);

    for (int i = 1; i <= N; i++)
        if (result[i] == answer)
            printf("%d ", i);

    return 0;
}