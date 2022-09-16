#include <bits/stdc++.h>

using namespace std;

int N;

void solve(int cnt, int a, int b, int c)
{
    if (cnt == 1)
    {
        cout << a << ' ' << b << '\n';
        return;
    }
    solve(cnt - 1, a, c, b);
    cout << a << ' ' << b << '\n';
    solve(cnt - 1, c, b, a);
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> N;

    cout << (1 << N) - 1 << '\n';
    solve(N, 1, 3, 2);

    return 0;
}