#include <bits/stdc++.h>

using namespace std;

int N;
int arr[201][201];
int selected[3];

int dfs(int idx, int start)
{
    if (idx == 3)
        return 1;

    int retval = 0;
    for (int i = start; i <= N; i++)
    {
        bool check = false;
        for (int j = 0; j < 3; j++)
            if (arr[i][selected[j]])
                check = true;

        if (check)
            continue;

        selected[idx] = i;
        retval += dfs(idx + 1, i + 1);
        selected[idx] = 0;
    }

    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int M;
    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[a][b] = arr[b][a] = 1;
    }

    cout << dfs(0, 1) << '\n';

    return 0;
}