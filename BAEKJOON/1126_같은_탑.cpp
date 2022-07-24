#include <iostream>
#define MIN_INF -987654321

using namespace std;

int N;
int input[50];
int dp[50][500000 / 2 + 1];

int max(int a, int b)
{
    return a > b ? a : b;
}

int solve(int ind, int diff)
{
    if (diff > 500000 / 2)
        return MIN_INF;
    if (ind == N && diff)
        return MIN_INF;
    if (ind == N)
        return 0;

    int &retval = dp[ind][diff];
    if (retval != -1) return retval;

    retval = MIN_INF;
    retval = max(retval, solve(ind + 1, diff));
    retval = max(retval, solve(ind + 1, diff + input[ind]) + input[ind]);
    if (input[ind] > diff)
        retval = max(retval, solve(ind + 1, input[ind] - diff) + input[ind] - diff);
    else
        retval = max(retval, solve(ind + 1, diff - input[ind]));
    return retval;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int temp;
    cin >> N;

    for (int i=0; i<N; i++)
        for (int j=0;j<500000 / 2 + 1;j++)
            dp[i][j] = -1;

    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input[i] = temp;
    }

    int answer = solve(0, 0);
    if (answer) cout << answer;
    else cout << -1;

    return 0;
}