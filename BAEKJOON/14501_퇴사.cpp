#include <bits/stdc++.h>

using namespace std;

int N, T[15], P[15], dp[15];

int dfs(int here)
{
    if (here > N)
        return INT_MIN;
    if (here == N)
        return 0;

    int &retval = dp[here];
    retval = max(dfs(here + 1), dfs(here + T[here]) + P[here]);
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> T[i] >> P[i];

    cout << dfs(0) << '\n';
    return 0;
}