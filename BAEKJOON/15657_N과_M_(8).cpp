#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> arr;
int selected[8];

void solve(int remain, int idx)
{
    if (remain == 0)
    {
        for (int i = 0; i < M; i++)
            cout << selected[i] << ' ';
        cout << '\n';
        return;
    }

    for (int i = idx; i < N; i++)
    {
        selected[M - remain] = arr[i];
        solve(remain - 1, i);
    }
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        arr.push_back(num);
    }

    sort(arr.begin(), arr.end());
    arr.erase(unique(arr.begin(), arr.end()), arr.end());
    N = arr.size();

    solve(M, 0);

    return 0;
}