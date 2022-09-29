#include <bits/stdc++.h>

using namespace std;

int N;
vector<pair<int, int>> edges[10001];
bool visited[10001];
int answer = 0;

int dfs(int here)
{
    vector<int> result;

    for (auto &[there, cost] : edges[here])
    {
        if (visited[there])
            continue;
        visited[there] = true;

        result.push_back(dfs(there) + cost);
    }

    sort(result.begin(), result.end(), [](int a, int b) -> bool
         { return a > b; });

    if (result.size() == 0)
        return 0;
    if (result.size() == 1)
        return result[0];

    answer = max(answer, result[0] + result[1]);
    return result[0];
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N - 1; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        edges[a].emplace_back(b, c);
        edges[b].emplace_back(a, c);
    }

    visited[1] = true;
    answer = max(answer, dfs(1));
    cout << answer << '\n';

    return 0;
}