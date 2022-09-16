#include <bits/stdc++.h>

#define SIZE 11
#define INF 1000000001

using namespace std;

int N;
int arr[SIZE];
int ops[4];
int answer[2] = {INF, -INF};

void solve(int cnt, int pvalue)
{
    if (cnt == N)
    {
        answer[0] = min(answer[0], pvalue);
        answer[1] = max(answer[1], pvalue);
        return;
    }

    for (int i = 0; i < 4; i++)
    {
        if (ops[i] == 0)
            continue;

        int nvalue = pvalue;
        switch (i)
        {
        case 0:
            nvalue += arr[cnt];
            break;
        case 1:
            nvalue -= arr[cnt];
            break;
        case 2:
            nvalue *= arr[cnt];
            break;
        case 3:
            nvalue /= arr[cnt];
            break;
        }

        ops[i]--;
        solve(cnt + 1, nvalue);
        ops[i]++;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    for (int i = 0; i < 4; i++)
        cin >> ops[i];
    solve(1, arr[0]);
    cout << answer[1] << endl
         << answer[0] << endl;

    return 0;
}