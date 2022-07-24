#include <bits/stdc++.h>

#define MOD 1000000007LL

using namespace std;

long long power(long long x, long long p)
{
    if (p == 1)
        return x;
    long long ny = power(x, p / 2);
    ny = (ny * ny) % MOD;
    return (ny * (p % 2 ? x : 1)) % MOD;
}

int main(void)
{
    long long N, R;
    cin >> N >> R;

    long long answer = 1;
    for (long long i = R + 1; i <= N; i++) {
        answer = (answer * i) % MOD;
        answer = (answer * power(i - R, MOD - 2)) % MOD;
    }
    printf("%lld\n", answer);

    return 0;
}