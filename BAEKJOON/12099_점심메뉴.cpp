#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int N, Q;
vector<pair<int, int>> input;

bool comp(const pair<int, int> &a, const pair<int, int> &b)
{
    return a.first < b.first;
}

int lower_bound(int x)
{
    int s = 0, e = N, m;
    while (s < e)
    {
        m = (s + e) / 2;
        if (x <= input[m].first)
            e = m;
        else
            s = m + 1;
    }
    return e;
}

int upper_bound(int x)
{
    int s = 0, e = N, m;
    while (s < e)
    {
        m = (s + e) / 2;
        if (x < input[m].first)
            e = m;
        else
            s = m + 1;
    }
    return e;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> Q;

    input.reserve(N);
    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        input.push_back(make_pair(a, b));
    }

    sort(input.begin(), input.end(), comp);

    for (int i = 0; i < Q; i++)
    {
        int u, v, x, y, sum = 0;
        cin >> u >> v >> x >> y;

        u = lower_bound(u);
        v = upper_bound(v);

        for (int j = u; j < v; j++)
            if ((x <= input[j].second) && (input[j].second <= y))
                sum++;

        cout << sum << '\n';
    }

    return 0;
}