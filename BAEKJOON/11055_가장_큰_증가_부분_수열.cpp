#include <bits/stdc++.h>

using namespace std;

int N;
int arr[1000], dp[1000];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    int answer = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < i; j++)
            if (arr[j] < arr[i])
                dp[i] = max(dp[i], dp[j]);

        dp[i] += arr[i];
        answer = max(answer, dp[i]);
    }
    
    cout << answer << '\n';

    return 0;
}