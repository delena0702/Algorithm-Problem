#include <bits/stdc++.h>

using namespace std;

int arr[10], answer[10];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    for (int i = 0; i < N; i++)
    {
        int cnt = 0;
        for (int j = 0; j < N; j++)
            if (answer[j] == 0 && cnt++ == arr[i])
                answer[j] = i + 1;
    }

    for (int i = 0; i < N; i++)
        cout << answer[i] << ' ';
    cout << '\n';

    return 0;
}