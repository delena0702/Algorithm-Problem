#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    string str;
    cin >> str;
    for (char ch : str) {
        if (ch >= 'A' && ch <= 'Z')
            ch += 'a' - 'A';    // change ch lowercase
        if (ch == 'a' || ch == 'o' || ch == 'y' || ch == 'e' || ch == 'u' || ch == 'i')
            continue;
        cout << '.' << ch;
    }
    cout << '\n';

    return 0;
}