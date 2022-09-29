// Test Code

#include <bits/stdc++.h>

using namespace std;

struct Point
{
    int x, y1, y2, value;

    bool operator<(Point &p)
    {
        return this->x < p.x;
    }
};

int cnt[30001];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    vector<Point> arr;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int x1, x2, y1, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        arr.push_back({x1, y1, y2, 1});
        arr.push_back({x2, y1, y2, -1});
    }

    sort(arr.begin(), arr.end());

    int pre_x = arr[0].x;
    int answer = 0;
    int sum = 0;
    for (int i = 0; i < 2 * N; i++)
    {
        auto &[x, y1, y2, value] = arr[i];

        answer += (x - pre_x) * sum;

        for (int j = y1; j < y2; j++)
        {
            if (!cnt[j] && value == 1)
                sum++;
            if (cnt[j] == 1 && value == -1)
                sum--;
            cnt[j] += value;
        }

        pre_x = x;
    }
    cout << answer << '\n';

    return 0;
}