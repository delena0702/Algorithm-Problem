#include <bits/stdc++.h>

using namespace std;

vector<string> arr;

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
        arr.push_back(str);
    }

    sort(arr.begin(), arr.end());

    int answer = N;
    for (int i = 0; i + 1 < N; i++)
    {
        if (arr[i].length() > arr[i + 1].length())
            continue;

        for (int j = 0; j <= arr[i].length(); j++)
        {
            if (j == arr[i].length())
            {
                answer--;
                break;
            }
            if (arr[i][j] != arr[i + 1][j])
                break;
        }
    }

    cout << answer << '\n';

    return 0;
}