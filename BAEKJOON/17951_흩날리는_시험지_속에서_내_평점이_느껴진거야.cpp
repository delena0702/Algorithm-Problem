#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

int N, K;
int input[SIZE];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> K;

    for (int i = 0; i < N; i++)
        cin >> input[i];

    int s = 0, e = 2000000, m;
    while (s < e)
    {
        m = (s + e) / 2;

        int count = 0, sum = 0;
        for (int i = 0; i < N; i++)
        {
            sum += input[i];
            if (sum >= m)
                sum = 0, count++;
        }

        if (count >= K)
            s = m + 1;
        else
            e = m;
    }
    cout << e - 1 << endl;

    return 0;
}