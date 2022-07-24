#include <bits/stdc++.h>

#define SIZE 200000
#define INF LLONG_MAX

using namespace std;
struct node
{
    long long value;
    long long upd;
};
node tree[4 * SIZE];
int N;

long long update(int l, int r, long long value, int here = 1, int s = 0, int e = N - 1)
{
    if (r < s || e < l)
        return tree[here].value + tree[here].upd;
    if (l <= s && e <= r)
    {
        tree[here].upd += value;
        return tree[here].value + tree[here].upd;
    }
    int m = (s + e) / 2;
    tree[here].value = min(update(l, r, value, 2 * here, s, m), update(l, r, value, 2 * here + 1, m + 1, e));
    return tree[here].value + tree[here].upd;
}

long long minimum(int l, int r, int here = 1, int s = 0, int e = N - 1)
{
    if (r < s || e < l)
        return INF;
    if (l <= s && e <= r)
        return tree[here].value + tree[here].upd;
    int m = (s + e) / 2;

    tree[2 * here].upd += tree[here].upd;
    tree[2 * here + 1].upd += tree[here].upd;
    tree[here].value += tree[here].upd;
    tree[here].upd = 0;

    return min(minimum(l, r, 2 * here, s, m), minimum(l, r, 2 * here + 1, m + 1, e));
}

int main(void)
{
    int M;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        update(i, i, temp);
    }

    cin >> M;
    for (int i = 0; i < M; i++)
    {
        int l, r;
        cin >> l >> r;

        if (getchar() == '\n')
        {
            if (l <= r)
                printf("%lld\n", minimum(l, r));
            else
                printf("%lld\n", min(minimum(0, r), minimum(l, N - 1)));
        }
        
        else
        {
            int v;
            cin >> v;

            if (l <= r)
                update(l, r, v);
            else
            {
                update(0, r, v);
                update(l, N - 1, v);
            }
        }
    }

    return 0;
}