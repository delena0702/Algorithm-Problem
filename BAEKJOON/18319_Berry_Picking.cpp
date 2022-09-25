#include <bits/stdc++.h>

using namespace std;

int arr[1000], MOD = 1;

bool comp(int &a, int &b)
{
    return a % MOD > b % MOD;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, K, maximum = -1;
    cin >> N >> K;
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
        maximum = max(maximum, arr[i]);
    }

    int answer = 0;
    for (int i = 1; i <= maximum; i++)
    {
        int cnt = 0;
        for (int j = 0; j < N; j++)
            cnt += arr[j] / i;

        if (cnt <= K / 2)
            break;

        if (cnt >= K)
        {
            answer = max(answer, i * K / 2);
            continue;
        }

        MOD = i;
        sort(arr, arr + N, comp);

        int temp = (cnt - K / 2) * i;
        for (int j = 0; j < N && j + cnt < K; j++)
            temp += arr[j] % i;
        answer = max(answer, temp);
    }
    cout << answer << '\n';

    return 0;
}