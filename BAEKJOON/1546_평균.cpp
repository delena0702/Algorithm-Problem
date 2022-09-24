#include <bits/stdc++.h>

using namespace std;

int N, arr[1000];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    int sum = 0, maximum = 0;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        sum += arr[i];
        maximum = max(maximum, arr[i]);
    }
    double answer = (double)(sum * 100) / (N * maximum);
    cout << answer << '\n';

    return 0;
}