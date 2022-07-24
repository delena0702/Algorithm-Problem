#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string input;
    cin >> input;
    int ac = 0, answer = 0;
    bool after_minus = false;

    for (int i = 0; i <= input.length(); i++)
    {
        char ch = input[i];

        if (ch >= '0' && ch <= '9')
        {
            ac = 10 * ac + ch - '0';
            if (i < input.length() - 1)
                continue;
        }

        if (after_minus)
            answer -= ac;
        else
            answer += ac;
        ac = 0;

        if (ch == '-')
            after_minus = true;
    }
    cout << answer << endl;

    return 0;
}