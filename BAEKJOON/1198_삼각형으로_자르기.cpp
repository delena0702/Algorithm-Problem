#include <bits/stdc++.h>

using namespace std;

int N;
pair<int, int> arr[35];
int selected[3];

int dfs(int idx, int start)
{
    if (idx == 3)
    {
        int x1 = arr[selected[1]].first - arr[selected[0]].first;
        int x2 = arr[selected[2]].first - arr[selected[0]].first;
        int y1 = arr[selected[1]].second - arr[selected[0]].second;
        int y2 = arr[selected[2]].second - arr[selected[0]].second;

        return abs(x1 * y2 - x2 * y1);
    }

    int retval = 0;
    for (int i = start; i < N; i++)
    {
        selected[idx] = i;
        retval = max(retval, dfs(idx + 1, i + 1));
    }
    return retval;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[i] = {a, b};
    }

    printf("%.1lf\n", (double)dfs(0, 0) / 2);

    return 0;
}