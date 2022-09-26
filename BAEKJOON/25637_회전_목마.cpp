#include <bits/stdc++.h>

using namespace std;

int arr[2000];
int answer[2000];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    int idx = 0;
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;

        for (int j = 0; j < num; j++)
            arr[idx++] = i;
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int num = abs((i + j) % N - arr[i]);
            answer[j] += min(num, N - num);
        }
    }

    int result = 987654321;
    for (int i = 0; i < N; i++)
        result = min(result, answer[i]);
    cout << result << '\n';

    return 0;
}