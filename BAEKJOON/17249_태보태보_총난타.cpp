#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string input;
    cin >> input;

    int answer[2] = {0, 0}, ind = 0;
    for (const auto &c : input)
    {
        if (c == '0') ind = 1;
        else if (c == '@') answer[ind]++;
    }

    cout << answer[0] << ' ' << answer[1] << "\n";

    return 0;
}
