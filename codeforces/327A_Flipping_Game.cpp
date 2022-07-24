#include <bits/stdc++.h>

#define SIZE 100
using namespace std;

int sub_sum[SIZE + 1];

int main(void)
{
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        int temp;
        cin >> temp;
        sub_sum[i] = sub_sum[i - 1] + temp;
    }

    int max_value = -1;
    for (int s = 1; s <= n; s++)
        for (int e = s; e <= n; e++)
            max_value = max(max_value, sub_sum[n] - 2 * (sub_sum[e] - sub_sum[s - 1]) + (e - s + 1));

    printf("%d\n", max_value);

    return 0;
}