#include <bits/stdc++.h>

using namespace std;

long long arr[100000];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T, N;
    cin >> T;
    while (T--)
    {
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> arr[i];
        sort(arr, arr + N);

        int temp = 1;
        for (int i = 1; i <= N; i++)
        {
            if (i < N && arr[i - 1] == arr[i])
            {
                temp++;
                continue;
            }

            if (temp > N / 2)
            {
                cout << arr[i - 1] << '\n';
                break;
            }

            temp = 1;

            if (i == N)
                cout << "SYJKGW\n";
        }
    }

    return 0;
}