#include <bits/stdc++.h>

using namespace std;

int height[10001];

struct Data
{
    int y, x1, x2;
};

vector<Data> arr;

bool comp(Data &a, Data &b)
{
    return a.y < b.y;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int y, x1, x2;
        cin >> y >> x1 >> x2;
        arr.push_back({y, x1, x2});
    }

    sort(arr.begin(), arr.end(), comp);

    int answer = 0;
    for (auto &[y, x1, x2] : arr)
    {
        answer += y - height[x1];
        answer += y - height[x2 - 1];
        for (int i = x1; i < x2; i++)
            height[i] = y;
    }
    cout << answer << '\n';

    return 0;
}