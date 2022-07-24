#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

int arr[SIZE];

int main(void)
{
    int n;
    cin >> n;

    int dp[2] = {1, 1}, answer = 1;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr[i] = temp;

        if (i == 0)
            continue;

        if (arr[i - 1] == arr[i])
        {
            dp[0]++;
            dp[1]++;
        }

        else if (arr[i - 1] < arr[i])
        {
            dp[0] = dp[1] + 1;
            dp[1] = 1;
        }

        else
        {
            dp[1] = dp[0] + 1;
            dp[0] = 1;
        }

        answer = max(answer, dp[0]);
        answer = max(answer, dp[1]);
    }

    cout << answer << '\n';
    return 0;
}