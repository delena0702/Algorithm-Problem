#include <bits/stdc++.h>

using namespace std;

int N, arr[101];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> arr[i];

    int M;
    cin >> M;
    for (int i = 0; i < M; i++)
    {
        int t, x;
        cin >> t >> x;
        if (t == 1)
            for (int j = x; j <= N; j += x)
                arr[j] = 1 - arr[j];

        else
        {
            for (int i = 0;; i++)
            {
                if (x - i <= 0 || x + i > N)
                    break;
                if (arr[x - i] != arr[x + i])
                    break;
                arr[x - i] = 1 - arr[x - i];
                if (i)
                    arr[x + i] = 1 - arr[x + i];
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << arr[i] << ' ';
        if (i % 20 == 0)
            cout << '\n';
    }
    cout << '\n';

    return 0;
}