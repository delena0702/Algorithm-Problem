#include <bits/stdc++.h>
#define SZ 20

using namespace std;

struct Segtree
{
    int flag = 1 << SZ;
    int minimum[1 << (SZ + 1)];
    int maximum[1 << (SZ + 1)];

    void update(int idx, int value)
    {
        idx |= flag;
        minimum[idx] = maximum[idx] = value;
        while (idx >>= 1)
        {
            minimum[idx] = min(minimum[idx << 1], minimum[idx << 1 | 1]);
            maximum[idx] = max(maximum[idx << 1], maximum[idx << 1 | 1]);
        }
    }

    int queryMin(int l, int r)
    {
        l |= flag, r |= flag;
        int retval = INT_MAX;
        while (l <= r)
        {
            if (l & 1)
                retval = min(retval, minimum[l++]);
            if (~r & 1)
                retval = min(retval, minimum[r--]);
            l >>= 1, r >>= 1;
        }
        return retval;
    }

    int queryMax(int l, int r)
    {
        l |= flag, r |= flag;
        int retval = INT_MIN;
        while (l <= r)
        {
            if (l & 1)
                retval = max(retval, maximum[l++]);
            if (~r & 1)
                retval = max(retval, maximum[r--]);
            l >>= 1, r >>= 1;
        }
        return retval;
    }
};

Segtree tree;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;
    for (int i = 1; i <= N; i++)
    {
        int num;
        cin >> num;
        tree.update(i, num);
    }

    for (int i = 0; i < M; i++)
    {
        int l, r;
        cin >> l >> r;
        cout << tree.queryMin(l, r) << ' ' << tree.queryMax(l, r) << '\n';
    }

    return 0;
}