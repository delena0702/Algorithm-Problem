#include <bits/stdc++.h>
#define SIZE 5000

using namespace std;

int arr[SIZE];
int pre_sum[SIZE + 1];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, k;
    cin >> N >> k;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
        pre_sum[i + 1] = pre_sum[i] + arr[i];
    }

    double answer = 0.0;

    for (int s = 0; s < N - k + 1; s++)
        for (int e = s + k - 1; e < N; e++)
            answer = max(answer, (double)(pre_sum[e + 1] - pre_sum[s]) / (double)(e - s + 1));

    printf("%lf\n", answer);

    return 0;
}