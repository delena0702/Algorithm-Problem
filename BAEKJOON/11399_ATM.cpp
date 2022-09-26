#include <bits/stdc++.h>

using namespace std;

int arr[1000];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    sort(arr, arr + N);

    int answer = 0, psum = 0;
    for (int i = 0; i < N; i++)
    {
        psum += arr[i];
        answer += psum;
    }
    cout << answer << '\n';

    return 0;
}