#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int k[4], answer[2] = {0, 0};

    for (int i = 0; i < 4; i++)
    {
        int temp;
        cin >> temp;
        k[i] = temp;
    }

    answer[0] = min(min(k[0], k[2]), k[3]);
    answer[1] = min(k[0] - answer[0], k[1]);

    printf("%d\n", 256 * answer[0] + 32 * answer[1]);

    return 0;
}