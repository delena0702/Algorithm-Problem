#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++)
    {
        string I, P;
        cin >> I >> P;

        int idx = 0;
        for (int i = 0; i <= P.length(); i++)
        {
            if (idx == I.length())
            {
                cout << "Case #" << test_case << ": " << P.length() - I.length() << endl;
                break;
            }

            if (i == P.length())
            {
                cout << "Case #" << test_case << ": IMPOSSIBLE" << endl;
                break;
            }

            if (P[i] == I[idx])
                idx++;
        }
    }

    return 0;
}