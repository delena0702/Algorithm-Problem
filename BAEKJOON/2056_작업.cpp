#include <bits/stdc++.h>

using namespace std;

int N;
vector<int> edges[10001], dijk;
int times[10001];

int dfs(int here)
{
    if (dijk[here] != -1)
        return dijk[here];

    dijk[here] = 0;
    for (int there : edges[here])
        dijk[here] = max(dijk[here], dfs(there));
    dijk[here] += times[here];
    return dijk[here];
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        cin >> times[i];

        int n;
        cin >> n;
        for (int j = 0; j < n; j++)
        {
            int num;
            cin >> num;
            edges[i].push_back(num);
        }
    }

    dijk.resize(N + 1, -1);
    for (int i = 1; i <= N; i++)
        dfs(i);

    int answer = 0;
    for (int i = 1; i <= N; i++)
        answer = max(answer, dijk[i]);
    cout << answer << '\n';

    return 0;
}