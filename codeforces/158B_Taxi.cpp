#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, arr[5] = {0, 0, 0, 0, 0}, answer = 0;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        arr[temp]++;
    }

    // 4
    answer = arr[4];

    // 3
    answer += arr[3];
    arr[1] = max(0, arr[1] - arr[3]);

    // 2
    answer += (arr[2] + 1) / 2;
    if (arr[2] % 2)
        arr[1] = max(0, arr[1] - 2);

    // 1
    answer += (arr[1] + 3) / 4;

    printf("%d\n", answer);

    return 0;
}