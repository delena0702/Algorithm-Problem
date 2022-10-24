#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string str;
    cin >> str;
    int N = str.length();

    for (int i = N; i > 0; i--)
    {
        bool check = true;
        for (int j = 0; N - i + j < N - 1 - j; j++)
        {
            if (str[N - i + j] != str[N - 1 - j])
            {
                check = false;
                break;
            }
        }

        if (check)
        {
            cout << 2 * N - i << '\n';
            break;
        }
    }

    return 0;
}