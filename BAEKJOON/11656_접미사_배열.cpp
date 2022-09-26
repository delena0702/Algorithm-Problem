#include <bits/stdc++.h>

using namespace std;

vector<string> arr;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string str;
    cin >> str;

    for (int i = 0; i < str.length(); i++)
        arr.push_back(str.substr(i));
    sort(arr.begin(), arr.end());

    for (auto &s : arr)
        cout << s << '\n';

    return 0;
}