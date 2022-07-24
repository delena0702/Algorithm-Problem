#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

vector<pair<int, long long>> graph[SIZE + 1];

bool visited[SIZE + 1];
long long dp[SIZE + 1];
int pre_node[SIZE + 1];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int a, b;
        long long w;
        cin >> a >> b >> w;

        graph[a].push_back(make_pair(b, w));
        graph[b].push_back(make_pair(a, w));
    }

    priority_queue<pair<long long, int>> pq;
    pq.push(make_pair(0, 1));
    dp[1] = 0;
    for (int i = 2; i <= N; i++)
        dp[i] = -1;
    pre_node[1] = 0;

    while (!pq.empty())
    {
        int here = pq.top().second;
        long long distance = -pq.top().first;

        if (here == N)
            break;
        pq.pop();

        if (visited[here])
            continue;
        visited[here] = true;

        for (pair<int, long long> p : graph[here])
        {
            int there = p.first;
            long long weight = p.second;

            if (visited[there])
                continue;

            if (dp[here] + weight < dp[there] || dp[there] == -1)
            {
                dp[there] = dp[here] + weight;
                pre_node[there] = here;

                pq.push(make_pair(-dp[there], there));
            }
        }
    }

    if (dp[N] == -1)
    {
        printf("-1\n");
        return 0;
    }

    deque<int> dq;
    for (int here = N; here; here = pre_node[here])
        dq.push_front(here);
    for (int v : dq)
        printf("%d ", v);
    printf("\n");

    return 0;
}