#include <iostream>
#define LIMIT 50

using namespace std;
typedef long long LL;
int N;
LL arr[LIMIT][3];
int matching[LIMIT];
bool visited[LIMIT];

LL comp(int a, int b)
{
    LL retval = 0;
    for (int i = 0; i < 3; i++)
    {
        if (!retval)
            retval = arr[a][i] - arr[b][i];
        else if ((arr[a][i] - arr[b][i]) * retval < 0)
            return 0;
    }
    if (retval == 0)
        return a - b;
    return retval;
}

int dfs(int here)
{
    if (visited[here]) return 0;
    visited[here] = true;

    for (int there = 0; there < N; there++)
    {
        if (comp(here, there) <= 0LL)
            continue;
        if (matching[there] == -1 || dfs(matching[there]))
        {
            matching[there] = here;
            return 1;
        }
    }

    return 0;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    LL temp;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> temp;
            arr[i][j] = temp;
        }
    }

    int answer = 0;
    for (int i = 0; i < N; i++)
        matching[i] = -1;

    for (int i = 0; i < 2 * N; i++)
    {
        for (int j = 0; j < N; j++)
            visited[j] = false;
        answer += dfs(i / 2);
    }

    cout << (N - answer);

    return 0;
}