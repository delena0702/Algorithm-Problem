#include <bits/stdc++.h>

#define SIZE 1000000

using namespace std;

struct node
{
    int inc, dec;
    int four, seven;
    bool update;
};

int N, M;
node tree[4 * SIZE];

void init(int here = 1, int s = 0, int e = N - 1)
{
    tree[here].inc = e - s + 1;
    tree[here].dec = e - s + 1;
    tree[here].four = e - s + 1;

    if (s == e)
        return;

    int m = (s + e) / 2;
    init(2 * here, s, m);
    init(2 * here + 1, m + 1, e);
}

void flip(int here, int s, int e)
{
    if (!tree[here].update)
        return;

    int temp = tree[here].inc;
    tree[here].inc = tree[here].dec;
    tree[here].dec = temp;

    temp = tree[here].four;
    tree[here].four = tree[here].seven;
    tree[here].seven = temp;

    tree[here].update = false;

    if (s != e)
    {
        tree[2 * here].update = !tree[2 * here].update;
        tree[2 * here + 1].update = !tree[2 * here + 1].update;
    }
}

void update(int l, int r, int here = 1, int s = 0, int e = N - 1)
{
    if (r < s || e < l)
        return;
    if (l <= s && e <= r)
    {
        tree[here].update = !tree[here].update;
        return;
    }

    int m = (s + e) / 2;
    update(l, r, 2 * here, s, m);
    update(l, r, 2 * here + 1, m + 1, e);

    flip(2 * here, s, m);
    flip(2 * here + 1, m + 1, e);
    tree[here].inc = max(tree[2 * here].four + tree[2 * here + 1].inc,
                         tree[2 * here].inc + tree[2 * here + 1].seven);
    tree[here].dec = max(tree[2 * here].seven + tree[2 * here + 1].dec,
                         tree[2 * here].dec + tree[2 * here + 1].four);
    tree[here].four = tree[2 * here].four + tree[2 * here + 1].four;
    tree[here].seven = tree[2 * here].seven + tree[2 * here + 1].seven;
}

int count(void)
{
    return tree[1].update ? tree[1].dec : tree[1].inc;
}

int main(void)
{
    string str;
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> M;
    cin >> str;

    init();

    for (int i = 0; i < N; i++)
        if (str[i] == '7')
            update(i, i);

    for (int i = 0; i < M; i++)
    {
        cin >> str;
        if (str[0] == 'c')
        {
            printf("%d\n", count());
        }
        else
        {
            int l, r;
            cin >> l >> r;
            update(l - 1, r - 1);
        }
    }

    return 0;
}