#include <bits/stdc++.h>

using namespace std;

int dist[100000], cost[100000];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N - 1; i++)
        cin >> dist[i];
    for (int i = 0; i < N; i++)
        cin >> cost[i];

    long long min_cost = cost[0], answer = 0;
    for (int i = 1; i < N; i++)
    {
        answer += min_cost * dist[i - 1];
        min_cost = min(min_cost, (long long)cost[i]);
    }
    cout << answer << '\n';

    return 0;
}