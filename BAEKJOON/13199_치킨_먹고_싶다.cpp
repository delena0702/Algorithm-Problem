#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--)
    {
        int P, M, F, C;
        cin >> P >> M >> F >> C;
        int answer = -(M / P * C / F);
        int coupons = M / P * C;

        if (coupons >= F)
            answer += (coupons - F) / (F - C) + 1;
        cout << answer << '\n';
    }

    return 0;
}
