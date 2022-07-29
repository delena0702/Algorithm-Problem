#include <bits/stdc++.h>
#define SIZE 500000

using namespace std;

int N;
int input[SIZE];
int inv[SIZE];
int fenwick[SIZE + 1] = {
    0,
};

void update(int idx)
{
    idx++;
    while (idx <= N)
    {
        fenwick[idx]++;
        idx += -idx & idx;
    }
}

int sum(int idx)
{
    idx++;
    int retval = 0;
    while (idx)
    {
        retval += fenwick[idx];
        idx -= -idx & idx;
    }
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> input[i];
    for (int i = 0; i < N; i++)
        inv[i] = i;
    stable_sort(inv, inv + N, [&](int a, int b) -> bool
         { return input[a] < input[b]; });

    for (int i = 0; i < N; i++)
        input[inv[i]] = i;

    long long answer = 0;
    for (int i = N - 1; i > 0; i--)
    {
        answer += N - inv[i] - sum(N - 1) + sum(inv[i]) - 1;
        update(inv[i]);
    }

    cout << answer << endl;

    return 0;
}