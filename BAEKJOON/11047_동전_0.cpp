#include <bits/stdc++.h>

#define SIZE 10

using namespace std;

int arr[SIZE];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, K;
    cin >> N >> K;
    
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    int answer = 0;
    for (int i = N - 1; i >= 0; i--)
    {
        answer += K / arr[i];
        K -= (K / arr[i]) * arr[i];
    }
    cout << answer << endl;

    return 0;
}