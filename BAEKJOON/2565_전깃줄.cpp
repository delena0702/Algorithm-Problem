#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int>> arr;
int dp[100];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        arr.emplace_back(a, b);
    }

    sort(arr.begin(), arr.end());

    int answer = 0;
    for (int i = 0; i < N; i++)
    {
        dp[i] = 1;
        for (int j = 0; j < i; j++)
            if (arr[j].second < arr[i].second)
                dp[i] = max(dp[i], dp[j] + 1);
        answer = max(answer, dp[i]);
    }

    cout << N - answer << '\n';

    return 0;
}