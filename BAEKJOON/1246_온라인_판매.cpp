#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    vector<int> arr;

    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int num;
        cin >> num;
        arr.push_back(num);
    }

    sort(arr.begin(), arr.end());
    int cost = 0, answer = 0;
    for (int i = max(0, M - N); i < M; i++)
    {
        if (answer >= arr[i] * (M - i))
            continue;

        cost = arr[i];
        answer = arr[i] * (M - i);
    }
    cout << cost << ' ' << answer << '\n';

    return 0;
}