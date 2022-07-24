#include <bits/stdc++.h>

#define SIZE 100001

using namespace std;

vector<int> tree[SIZE];
bool visited[SIZE];

double dfs(const int &here)
{
    visited[here] = true;
    int cnt = 0;
    double sum = 0;

    for (int there : tree[here])
    {
        if (visited[there])
            continue;
        sum += dfs(there) + 1;
        cnt++;
    }

    if (cnt == 0)
        return 0;
    return sum / cnt;
}

int main(void)
{
    int n;
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    printf("%f", dfs(1));

    return 0;
}