#include <bits/stdc++.h>

using namespace std;

int N, arr[50];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    sort(arr + 1, arr + N, [](int a, int b) -> bool
         { return a > b; });

    int answer;
    for (answer = arr[0];; answer++)
    {
        if (answer > arr[1])
            break;

        for (int i = 1; i < N; i++)
        {
            if (i != N - 1 && arr[i] == arr[i + 1])
                continue;

            arr[i]--;
            break;
        }
    }

    cout << answer - arr[0] << '\n';

    return 0;
}