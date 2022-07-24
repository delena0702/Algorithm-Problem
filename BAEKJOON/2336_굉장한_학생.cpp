#include <iostream>
#include <climits>

#define INF INT_MAX

using namespace std;

int N;
int sort_temp[5000001];
int arr[2][500001];
int seg_tree[4 * 500000];

void init(int node, int s, int e)
{
    seg_tree[node] = INF;
    if (s == e) return;

    init(2 * node, s, (s + e) / 2);
    init(2 * node + 1, (s + e) / 2 + 1, e);
    return;
}

int getMin(int x, int y, int node, int s, int e)
{
    if (e < x || y < s)
        return INF;
    if (x <= s && e <= y)
        return seg_tree[node];
    int a, b;
    a = getMin(x, y, 2 * node, s, (s + e) / 2);
    b = getMin(x, y, 2 * node+1, (s + e) / 2 + 1, e);
    return a < b ? a : b;
}

void updateMin(int ind, int val, int node, int s, int e)
{
    if (ind < s || e < ind)
        return;
    seg_tree[node] = seg_tree[node] < val ? seg_tree[node] : val;
    if (s != e)
    {
        updateMin(ind, val, 2 * node, s, (s + e) / 2);
        updateMin(ind, val, 2 * node + 1, (s + e) / 2 + 1, e);
    }
}

int main()
{
    int temp;
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        cin >> temp;
        sort_temp[temp] = i;
    }

    for (int i = 0; i < 2; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin >> temp;
            arr[i][sort_temp[temp]] = j;
        }
    }

    init(1, 1, N);
    int answer = 0;
    for (int i=1; i<=N; i++) {
        if (getMin(1, arr[0][i], 1, 1, N) > arr[1][i])
            answer++;
        updateMin(arr[0][i], arr[1][i], 1, 1, N);
    }

    cout << answer;

    return 0;
}