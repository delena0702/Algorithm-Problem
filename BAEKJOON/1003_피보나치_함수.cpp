#include <iostream>

using namespace std;

int T, N;
int dp[42] = {};

int f(int n)
{
    if (n == 0 || n == 1)
        return 1 - n;
    if (dp[n] != -1)
        return dp[n];
    dp[n] = f(n - 1) + f(n - 2);
    return dp[n];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i = 0; i < 42; i++)
        dp[i] = -1;

    cin >> T;
    while (T--)
    {
        cin >> N;
        cout << f(N) << ' ' << f(N + 1) << '\n';
    }

    return 0;
}
