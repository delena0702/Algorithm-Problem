#include <bits/stdc++.h>

#define SIZE 200001

using namespace std;

vector<int> tree[SIZE];
bool visited[SIZE];
long long priority[SIZE];

long long setPriority(const int &here, const int &depth)
{
    visited[here] = true;
    long long cnt = 0;
    for (int there : tree[here])
    {
        if (visited[there])
            continue;
        cnt += setPriority(there, depth + 1);
    }

    priority[here] = depth - cnt;

    return cnt + 1;
}

int main(void)
{
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    setPriority(1, 0);
    sort(priority + 1, priority + n + 1);

    long long answer = 0;
    for (int i = n - k + 1; i <= n; i++)
        answer += priority[i];
    printf("%lld\n", answer);

    return 0;
}