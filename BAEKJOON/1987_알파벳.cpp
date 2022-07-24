#include <iostream>
#include <string>

using namespace std;

int R, C;
string input[20];
bool check[26];

const int dx[] = {0, 0, 1, -1};
const int dy[] = {1, -1, 0, 0};

inline int max(int a, int b) { return a > b ? a : b; }

int dfs(int x, int y)
{
    if (x < 0 || x >= C || y < 0 || y >= R)
        return 0;
    int check_val = input[y][x] - 'A';
    if (check[check_val])
        return 0;

    check[check_val] = true;
    int retval = 0;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i], ny = y + dy[i];
        retval = max(retval, dfs(nx, ny) + 1);
    }

    check[check_val] = false;
    return retval;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> R >> C;
    for (int i = 0; i < R; i++)
    {
        string temp;
        cin >> temp;
        input[i] = temp;
    }

    cout << dfs(0, 0);

    return 0;
}