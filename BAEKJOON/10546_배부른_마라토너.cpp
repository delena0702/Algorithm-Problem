#include <bits/stdc++.h>

using namespace std;
vector<string> a, b;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    string str;
    for (int i = 0; i < N; i++)
    {
        cin >> str;
        a.push_back(str);
    }
    for (int i = 0; i < N - 1; i++)
    {
        cin >> str;
        b.push_back(str);
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    for (int i = 0; i < N; i++)
    {
        if (i == N - 1 || a[i] != b[i])
        {
            cout << a[i] << '\n';
            break;
        }
    }

    return 0;
}