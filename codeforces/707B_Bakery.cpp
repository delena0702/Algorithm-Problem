#include <bits/stdc++.h>
#define SIZE 100000
#define INF LLONG_MAX

using namespace std;

long long edges[SIZE][3];
bool check[SIZE];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;

    for (int i = 0; i < M; i++)
    {
        long long u, v, l;
        cin >> u >> v >> l;
        edges[i][0] = u - 1;
        edges[i][1] = v - 1;
        edges[i][2] = l;
    }

    for (int i = 0; i < K; i++)
    {
        int v;
        cin >> v;
        check[v - 1] = true;
    }

    long long answer = INF;
    for (int i = 0; i < M; i++)
        if (check[edges[i][0]] != check[edges[i][1]])
            answer = min(answer, edges[i][2]);

    if (answer == INF)
        answer = -1;

    cout << answer << '\n';

    return 0;
}