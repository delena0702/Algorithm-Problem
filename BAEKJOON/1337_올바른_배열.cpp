#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, arr[50];
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    sort(arr, arr + N);

    int answer = 1;
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j <= N; j++) {
            if (j != N && arr[j] < arr[i] + 5)
                continue;
            answer = max(answer, j - i);
            break;
        }
    }

    cout << max(0, 5 - answer) << '\n';

    return 0;
}