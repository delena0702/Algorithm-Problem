#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int>> arr;

bool comp(pair<int, int> &a, pair<int, int> &b)
{
    return a.second > b.second;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, t, s;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> t >> s;
        arr.push_back({t, s});
    }

    sort(arr.begin(), arr.end(), comp);

    int start = INT_MAX;
    for (auto &[t, s] : arr)
        start = min(start - t, s - t);
    if (start < 0)
        start = -1;
    cout << start << '\n';

    return 0;
}