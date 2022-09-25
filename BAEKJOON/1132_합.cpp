#include <bits/stdc++.h>

using namespace std;

long long arr[10];
bool check[10];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string str;
        cin >> str;

        long long temp = 1;
        for (int j = str.length() - 1; j >= 0; j--)
        {
            arr[str[j] - 'A'] += temp;
            temp *= 10;
            if (j == 0)
                check[str[j] - 'A'] = true;
        }
    }

    for (int i = 0; i < 10; i++)
    {
        if (!check[i])
        {
            swap(check[0], check[i]);
            swap(arr[0], arr[i]);
            break;
        }
    }

    for (int i = 1; i < 10; i++)
        if (!check[i] && arr[0] > arr[i])
            swap(arr[0], arr[i]);

    sort(arr + 1, arr + 10);

    long long answer = 0;
    for (int i = 0; i < 10; i++)
        answer += i * arr[i];
    cout << answer << '\n';

    return 0;
}