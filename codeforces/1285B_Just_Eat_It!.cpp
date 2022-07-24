#include <bits/stdc++.h>
#define SIZE 100000

using namespace std;

long long arr[SIZE + 1];
long long pre_sum[SIZE + 1];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T, N;
    cin >> T;
    while (T--)
    {
        cin >> N;

        long long max_ind = 0, min_ind = 0;

        for (int i = 1; i <= N; i++)
        {
            cin >> arr[i];
            pre_sum[i] = pre_sum[i - 1] + arr[i];
            max_ind = (pre_sum[i] > pre_sum[max_ind]) ? i : max_ind;
            min_ind = (pre_sum[i] <= pre_sum[min_ind]) ? i : min_ind;
        }

        if (pre_sum[max_ind] - pre_sum[min_ind] >= pre_sum[N] &&
            (max_ind != N || min_ind != 0))
            printf("NO\n");
        else
            printf("YES\n");
    }

    return 0;
}