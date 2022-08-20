#include <bits/stdc++.h>
#define SIZE 100000

using namespace std;

int N, M;
int pos[SIZE + 1];
int fenwick[2 * SIZE + 1];

void update(int idx)
{
    idx++;
    while (idx <= N + M)
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

    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++)
    {
        cin >> N >> M;

        for (int i = 1; i <= N + M; i++)
            fenwick[i] = 0;

        for (int i = 1; i <= N; i++)
            pos[i] = N - i;

        for (int i = 0; i < M; i++)
        {
            int num;
            cin >> num;
            cout << (N - 1) - (pos[num] - sum(pos[num])) << " ";
            update(pos[num]);
            pos[num] = N + i;
        }
        cout << endl;
    }

    return 0;
}