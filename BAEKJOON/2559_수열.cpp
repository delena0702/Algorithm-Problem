#include <iostream>

#define LIMIT 100000
#define INF 987654321

using namespace std;

int input[LIMIT], N, K;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> K;

    int temp, sum = 0, answer = -INF;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input[i] = temp;

        if (i - K < 0)
            sum += input[i];
        else
            sum += input[i] - input[i - K];
        if (i >= K - 1)
            answer = max(answer, sum);
    }

    cout << answer;
    return 0;
}