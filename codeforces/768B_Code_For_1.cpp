#include <bits/stdc++.h>

using namespace std;

long long solve(long long n, long long l, long long r)
{
    long long length = 1, nn = n / 2, m;
    while (nn)
    {
        length = length * 2 + 1;
        nn /= 2;
    }
    m = (length + 1) / 2;

    if (r < l || l <= 0 || r > length)
        return 0;
    if (l == 1 && r == length)
        return n;
    if (r < m)
        return solve(n / 2, l, r);
    if (m < l)
        return solve(n / 2, l - m, r - m);
    return solve(n / 2, l, m - 1) + solve(n / 2, 1, r - m) + n % 2;
}

int main(void)
{
    long long n, l, r;
    cin >> n >> l >> r;
    printf("%lld\n", solve(n, l, r));
    return 0;
}