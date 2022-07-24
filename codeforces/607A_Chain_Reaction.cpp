#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

pair<int, int> arr[SIZE];
int dp[SIZE];

int search(int target, int n)
{
    int s = 0, e = n, m;
    while (s < e)
    {
        m = (s + e) / 2;
        if (target <= arr[m].first)
            e = m;
        else
            s = m + 1;
    }
    return s;
}

int main(void)
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[i] = make_pair(a, b);
    }

    sort(arr, arr + n);
    
    dp[0] = 1;
    int answer = 1;
    for (int i = 1; i < n; i++)
    {
        int index = search(arr[i].first - arr[i].second, i);
        dp[i] = (index == 0) ? 1 : dp[index - 1] + 1;
        answer = max(answer, dp[i]);
    }
    cout << (n - answer) << '\n';

    return 0;
}