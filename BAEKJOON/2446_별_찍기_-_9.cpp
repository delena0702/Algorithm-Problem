#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = N; i > 0; i--)
    {
        for (int j = 0; j < N - i; j++)
            cout << ' ';
        for (int j = 0; j < 2 * i - 1; j++)
            cout << '*';
        cout << '\n';
    }
    
    for (int i = 2; i <= N; i++)
    {
        for (int j = 0; j < N - i; j++)
            cout << ' ';
        for (int j = 0; j < 2 * i - 1; j++)
            cout << '*';
        cout << '\n';
    }

    return 0;
}