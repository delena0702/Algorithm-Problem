#include <bits/stdc++.h>

using namespace std;

int N, arr[50];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[i] = a - b;
    }

    if (N % 2)
        cout << 1 << '\n';
    else
    {
        sort(arr, arr + N);
        cout << arr[N / 2] - arr[N / 2 - 1] + 1 << '\n';
    }

    return 0;
}