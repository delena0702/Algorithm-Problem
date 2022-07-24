#include <bits/stdc++.h>

#define SIZE 100

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, arr[SIZE], sum = 0;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        arr[i] = temp;
        sum += temp;
    }

    sort(arr, arr + N);

    int sub_sum = 0;
    for (int i = N - 1; i >= 0; i--)
    {
        sub_sum += arr[i];

        if (sub_sum > sum / 2)
        {
            printf("%d\n", N - i);
            break;
        }
    }

    return 0;
}