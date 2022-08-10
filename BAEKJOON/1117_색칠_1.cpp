#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long  W, H, f, c, x1, y1, x2, y2, mx;
    cin >> W >> H >> f >> c >> x1 >> y1 >> x2 >> y2;
    mx = min(f, W - f);

    long long answer = W * H;
    answer -= (min(mx, x2) - min(mx, x1)) * (y2 - y1) * (c + 1) * 2;
    answer -= (max(mx, x2) - max(mx, x1)) * (y2 - y1) * (c + 1);

    cout << answer << endl;

    return 0;
}