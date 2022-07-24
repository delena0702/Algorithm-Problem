#include <bits/stdc++.h>
#define SIZE 200000

using namespace std;

struct Node
{
    Node() : count(0), lazy(-1) {}
    int count; // 개수
    int lazy;  // 전부 0 또는 1 -> 0, 1 // 없으면 -1
};

int N, Q;
Node tree[26][4 * SIZE];

void pushDown(int ch, int here, int s, int e)
{
    int value = tree[ch][here].lazy;

    if (value == -1) return;

    int m = (s + e) / 2;
    tree[ch][2 * here].count = value * (m - s + 1);
    tree[ch][2 * here].lazy = value;

    tree[ch][2 * here + 1].count = value * (e - m);
    tree[ch][2 * here + 1].lazy = value;

    tree[ch][here].lazy = -1;
}

void update(int ch, int left, int right, int value, int here = 1, int s = 0, int e = N - 1)
{
    if (right < left || right < s || e < left)
        return;

    if (left <= s && e <= right)
    {
        tree[ch][here].count = value * (e - s + 1);
        tree[ch][here].lazy = value;
        return;
    }

    pushDown(ch, here, s, e);

    int m = (s + e) / 2;
    update(ch, left, right, value, 2 * here, s, m);
    update(ch, left, right, value, 2 * here + 1, m + 1, e);

    tree[ch][here].count = tree[ch][2 * here].count + tree[ch][2 * here + 1].count;

    return;
}

int query(int ch, int left, int right, int here = 1, int s = 0, int e = N - 1)
{
    if (right < s || e < left)
        return 0;

    if (left <= s && e <= right)
        return tree[ch][here].count;
    
    pushDown(ch, here, s, e);

    int m = (s + e) / 2;
    int result = query(ch, left, right, 2 * here, s, m) + query(ch, left, right, 2 * here + 1, m + 1, e);
    return result;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> Q;

    for (int i = 0; i < N; i++)
    {
        char ch;
        cin >> ch;
        update(ch - 'a', i, i, 1);
    }

    while (Q--)
    {
        int left, right, k;
        int cnt[26] = {0,};

        cin >> left >> right >> k;
        left--; right--;

        for (int i = 0; i < 26; i++)
        {
            cnt[i] = query(i, left, right);
            update(i, left, right, 0);
        }

        if (k)
        {
            for (int i = 0; i < 26; i++)
            {
                update(i, left, left + cnt[i] - 1, 1);
                left += cnt[i];
            }
        }

        else
        {
            for (int i = 25; i >= 0; i--)
            {
                update(i, left, left + cnt[i] - 1, 1);
                left += cnt[i];
            }
        }
    }

    for (int i = 0; i < N; i++)
        for (int j = 0; j < 26; j++)
            if (query(j, i, i))
                printf("%c", 'a' + j);

    return 0;
}