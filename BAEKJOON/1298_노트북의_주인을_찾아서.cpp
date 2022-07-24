#include <iostream>
#include <vector>

#define MAX 100

using namespace std;

int N, M;
vector<int> edges[MAX + 1];
bool visited[MAX + 1];
int matching[MAX + 1];

int dfs(int here) {
    if (visited[here]) return 0;
    visited[here] = true;

    for (int there : edges[here]) {
        if (!matching[there] || dfs(matching[there])) {
            matching[there] = here;
            return 1;
        }
    }
    return 0;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >>N>>M;
    int a, b;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        edges[a].push_back(b);
    }

    int answer = 0;
    for (int i = 1; i <= N; i++)
    {
        for (int j=1;j<N;j++)
            visited[j] = false;
        answer += dfs(i);
    }
    cout << answer;

    return 0;
}