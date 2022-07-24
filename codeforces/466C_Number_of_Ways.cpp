#include <bits/stdc++.h>
#define SIZE 500000

using namespace std;

long long arr[SIZE + 1];
long long pre_sum[SIZE + 1];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        cin >> arr[i];
        pre_sum[i] = pre_sum[i - 1] + arr[i];
    }

    long long total = pre_sum[N];

    if (total % 3)
    {
        printf("0\n");
        return 0;
    }

    long long cnt = 0, cnt1 = 0;
    for (int i = 1; i < N; i++)
    {
        if (pre_sum[i] == total / 3 * 2)
            cnt += cnt1;
        if (pre_sum[i] == total / 3)
            cnt1++;
    }
    printf("%lld\n", cnt);

    return 0;
}