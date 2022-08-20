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
        string N;
        cin >> N;
        int sum = 0;
        for (const auto &ch : N)
            sum = (sum + (ch - '0')) % 9;
        sum = (9 - sum) % 9;

        for (int i = 0; i <= N.length(); i++)
        {
            if (i == N.length()) {
                cout << "Case #" << test_case << ": ";
                cout << N << sum << endl;
            }

            if ((i || sum) && sum < (N[i] - '0')) {
                cout << "Case #" << test_case << ": ";
                cout << N.substr(0, i) << sum << N.substr(i) << endl;
                break;
            }
        }
    }

    return 0;
}