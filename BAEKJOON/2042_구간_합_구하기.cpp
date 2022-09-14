#include <bits/stdc++.h>

#define SIZE 1000000

using namespace std;

const int seg = 1 << 20;
long long segtree[1 << 21];

void update(int idx, long long value)
{
    idx |= seg;
    segtree[idx] = value;
    while (idx >>= 1)
        segtree[idx] = segtree[idx << 1] + segtree[idx << 1 | 1];
}

long long query(int l, int r)
{
    long long retval = 0;
    for (l |= seg, r |= seg; l <= r; l >>= 1, r >>= 1)
    {
        if (l & 1)
            retval += segtree[l++];
        if (~r & 1)
            retval += segtree[r--];
    }
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N, M, K;
    cin >> N >> M >> K;
    for (int i = 1; i <= N; i++)
    {
        long long num;
        cin >> num;
        update(i, num);
    }

    for (int i = 0; i < M + K; i++)
    {
        long long op, a, b;
        cin >> op >> a >> b;
        if (op == 1)
            update(a, b);
        else
            cout << query(a, b) << endl;
    }

    return 0;
}