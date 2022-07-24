#include <iostream>

using namespace std;

int N, S;

bool partition(int index, int remain, int max, int val)
{
    if (remain - N + index < 0)
        return false;
    if (remain - (N - index) * max > 0)
        return false;
    if (index == N)
        return val == S;

    for (int i = max; i >= 1; i--)
        if (partition(index + 1, remain - i, i, val + (i * (i - 1) / 2)))
            return true;
    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> S;

    cout << partition(0, 2 * N - 2, N - 1, 0);

    return 0;
}
