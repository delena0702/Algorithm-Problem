#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b)
{
    if (a < b)
        swap(a, b);
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    while (T--)
    {
        int a, b;
        cin >> a >> b;
        cout << a * b / gcd(a, b) << '\n';
    }

    return 0;
}