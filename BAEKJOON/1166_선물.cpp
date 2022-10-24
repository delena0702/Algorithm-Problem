#include <bits/stdc++.h>

using namespace std;

long long N, L, W, H;
long long calc(double l)
{
    return (long long)(L / l) * (long long)(W / l) * (long long)(H / l);
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> L >> W >> H;

    double s = 0, e = max(max(L, W), H);
    for (int i = 0; i < 100000; i++)
    {
        double m = (s + e) / 2;
        if (N > calc(m))
            e = m;
        else
            s = m;
    }
    printf("%.10lf\n", s);

    return 0;
}