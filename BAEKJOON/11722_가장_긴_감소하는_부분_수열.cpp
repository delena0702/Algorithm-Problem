#include <bits/stdc++.h>

#define SIZE 1000

using namespace std;

int arr[SIZE], dp[SIZE];

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    int answer = 1;
    dp[0] = 1;
    for (int i = 1; i < N; i++)
    {
        dp[i] = 1;
        for (int j = 0; j < i; j++)
            if (arr[j] > arr[i])
                dp[i] = max(dp[i], dp[j] + 1);
        answer = max(answer, dp[i]);
    }
    cout << answer << endl;

    return 0;
}