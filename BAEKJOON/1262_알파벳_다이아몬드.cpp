#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, r1, c1, r2, c2;
    cin >> N >> r1 >> c1 >> r2 >> c2;

    for (int i = r1; i <= r2; i++)
    {
        for (int j = c1; j <= c2; j++)
        {
            int x = j % (2 * N - 1), y = i % (2 * N - 1);
            int value = abs(N - 1 - x) + abs(N - 1 - y);

            if (value >= N)
            {
                cout << '.';
                continue;
            }

            cout << (char)('a' + (value % 26));
        }

        cout << '\n';
    }

    return 0;
}