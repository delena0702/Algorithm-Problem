#include <bits/stdc++.h>
#define SZ 20

using namespace std;

struct Segtree
{
    int flag = 1 << SZ;
    int arr[1 << (SZ + 1)];

    void update(int idx, int value)
    {
        idx |= flag;
        arr[idx] = value;
        while (idx >>= 1)
            arr[idx] = max(arr[idx << 1], arr[idx << 1 | 1]);
    }

    int query(int l, int r)
    {
        l |= flag, r |= flag;
        int retval = 0;
        while (l <= r)
        {
            if (l & 1)
                retval = max(retval, arr[l++]);
            if (~r & 1)
                retval = max(retval, arr[r--]);
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

    for (int i = 1; i + 2 * M - 2 <= N; i++)
        cout << tree.query(i, i + 2 * M - 2) << ' ';
    cout << '\n';

    return 0;
}