#include <bits/stdc++.h>

#define INF 987654321
#define SIZE 4000

using namespace std;

int a, b, c, dp[SIZE + 1];

int solve(int n)
{
    if (n < 0)
        return -INF;
    if (dp[n] != -1)
        return dp[n];

    int &retval = dp[n];

    retval = -INF;
    retval = max(retval, solve(n - a) + 1);
    retval = max(retval, solve(n - b) + 1);
    retval = max(retval, solve(n - c) + 1);

    return retval;
}

int main(void)
{
    int n;
    cin >> n >> a >> b >> c;

    for (int i = 1; i <= n; i++)
        dp[i] = -1;

    printf("%d\n", solve(n));
}