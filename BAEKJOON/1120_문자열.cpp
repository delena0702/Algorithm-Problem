#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string a, b;
    cin >> a >> b;

    int answer = INT_MAX;
    for (int i = 0; i < b.length() - a.length() + 1; i++)
    {
        int temp = 0;
        for (int j = 0; j < a.length(); j++)
            if (a[j] != b[i + j])
                temp++;
        answer = min(answer, temp);
    }

    cout << answer << '\n';

    return 0;
}