#include <bits/stdc++.h>
#define SIZE 100

using namespace std;

vector<int> tree[SIZE];
bool visited[SIZE];

bool dfs(int here)
{
    if (visited[here]) return false;
    visited[here] = true;

    for (int there : tree[here])
        dfs(there);

    return true;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    int x[SIZE], y[SIZE];
    for (int i = 0; i < N; i++)
    {
        int tempx, tempy;
        cin >> tempx >> tempy;

        x[i] = tempx;
        y[i] = tempy;
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (x[i] == x[j] || y[i] == y[j])
            {
                tree[i].push_back(j);
                tree[j].push_back(i);
            }
        }
    }

    int answer = -1;
    for (int i = 0; i < N; i++)
        if (dfs(i))
            answer++;

    printf("%d\n", answer);

    return 0;
}