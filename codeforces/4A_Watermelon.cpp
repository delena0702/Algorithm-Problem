#include <iostream>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int w;
    cin >> w;
    if (w >= 4 && w % 2 == 0)
        cout << "YES\n";
    else
        cout << "NO\n";

    return 0;
}