#include <bits/stdc++.h>

using namespace std;

int arr[2200][2200];
int answer[3];

int calc(int a, int b) {
    if (a == -2) return b;
    if (a == b) return a;
    return 2;
}

int solve(int n, int x, int y)
{
    if (n == 1) {
        answer[arr[y][x] + 1]++;
        return arr[y][x];
    }

    int nn = n / 3;
    int retval = -2;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            int inner = solve(nn, x + nn * j, y + nn * i);
            retval = calc(retval, inner);
        }
    }

    if (retval < 2)
        answer[retval + 1] -= 8;
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> arr[i][j];

    solve(N, 0, 0);
    for (int i = 0; i < 3; i++)
        cout << answer[i] << '\n';

    return 0;
}