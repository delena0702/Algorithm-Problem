#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, score, P;
    cin >> N >> score >> P;

    vector<int> arr;
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        arr.push_back(num);
    }

    int s = 0, e = N;
    while (s < e)
    {
        int m = (s + e) / 2;
        if (score >= arr[m])
            e = m;
        else
            s = m + 1;
    }
    s++;

    if (s > P || (arr.size() == P && score == arr[P - 1]))
        s = -1;

    cout << s << '\n';

    return 0;
}