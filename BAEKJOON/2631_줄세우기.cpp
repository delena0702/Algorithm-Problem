#include <iostream>

using namespace std;

int N, input[200], dp[200];

int LIS(void)
{
    int retval = 0;
    for (int i = 0; i < N; i++)
    {
        dp[i] = 1;
        for (int j = 0; j < i; j++)
            if (input[i] > input[j])
                dp[i] = (dp[i] > (dp[j] + 1)) ? dp[i] : (dp[j] + 1);
        retval = (retval > dp[i]) ? retval : dp[i];
    }
    return retval;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> input[i];
        input[i]--;
    }

    cout << (N - LIS()) << '\n';

    return 0;
}