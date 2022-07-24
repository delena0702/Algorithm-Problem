#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

long long cnt[SIZE + 1], dp[SIZE + 1];

int main(void)
{
    int n, max_value = 0;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;

        cnt[temp]++;
        max_value = max(max_value, temp);
    }
    
    for (int i = 1; i <= max_value; i++)
    {
        if (i <= 2)
            dp[i] = i * cnt[i];
        else if (i <= 3)
            dp[i] = i * cnt[i] + dp[i - 2];
        else
            dp[i] = i * cnt[i] + max(dp[i - 2], dp[i - 3]);
    }

    printf("%lld\n", max(dp[max_value - 1], dp[max_value]));

    return 0;
}