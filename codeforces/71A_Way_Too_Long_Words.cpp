#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    while (N--)
    {
        string str;
        cin >> str;
        if (str.length() <= 10)
            cout << str << '\n';
        else
            cout << str[0] << (str.length() - 2) << str[str.length() - 1] << '\n';
    }

    return 0;
}