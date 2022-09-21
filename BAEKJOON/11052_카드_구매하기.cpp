#include <bits/stdc++.h>

using namespace std;

int arr[1001], dp[1001];

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i=1; i<=N; i++)
        cin >> arr[i];
    for (int i = 1; i <= N; i++)
        for (int j = 0; j < i; j++)
            dp[i] = max(dp[i], dp[j] + arr[i - j]);
    
    cout << dp[N] << '\n';

    return 0;
}