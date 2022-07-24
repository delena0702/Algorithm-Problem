#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

long long c[SIZE];

inline long long add(const long long &a, const long long &b)
{
    if (a == -1 || b == -1)
        return -1;
    return a + b;
}

inline long long minimum(const long long &a, const long long &b)
{
    if (a == -1)
        return b;
    if (b == -1)
        return a;
    return min(a, b);
}

int main(void)
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        long long temp;
        cin >> temp;
        c[i] = temp;
    }

    string pre = "", pre_rev = "", now, now_rev;
    long long pre_cost[2] = {0, 0}, now_cost[2] = {0, 0}; // original and reverse

    for (int i = 0; i < n; i++)
    {
        cin >> now;
        now_rev = now;
        reverse(now_rev.begin(), now_rev.end());

        // Always pre_cost[0] <= pre_cost[1]

        if (pre.compare(now) <= 0)
            now_cost[0] = pre_cost[0];
        else if (pre_rev.compare(now) <= 0)
            now_cost[0] = pre_cost[1];
        else
            now_cost[0] = -1;

        if (pre.compare(now_rev) <= 0)
            now_cost[1] = add(pre_cost[0], c[i]);
        else if (pre_rev.compare(now_rev) <= 0)
            now_cost[1] = add(pre_cost[1], c[i]);
        else
            now_cost[1] = -1;

        if (minimum(now_cost[0], now_cost[1]) == now_cost[0])
        {
            pre = now;
            pre_rev = now_rev;
            pre_cost[0] = now_cost[0];
            pre_cost[1] = now_cost[1];
        }

        else
        {
            pre = now_rev;
            pre_rev = now;
            pre_cost[0] = now_cost[1];
            pre_cost[1] = now_cost[0];
        }
    }

    cout << minimum(now_cost[0], now_cost[1]) << '\n';

    return 0;
}