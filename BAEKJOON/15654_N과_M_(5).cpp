#include <bits/stdc++.h>

using namespace std;

int N, M;
int arr[8], selected[8];
bool check[8];

void solve(int remain)
{
    if (remain == 0)
    {
        for (int i = 0; i < M; i++)
            cout << selected[i] << ' ';
        cout << '\n';
        return;
    }

    for (int i = 0; i < N; i++)
    {
        if (check[i])
            continue;

        check[i] = true;
        selected[M - remain] = arr[i];
        solve(remain - 1);
        check[i] = false;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    sort(arr, arr + N);

    solve(M);

    return 0;
}