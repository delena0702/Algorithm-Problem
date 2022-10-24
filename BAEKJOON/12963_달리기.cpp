#include <bits/stdc++.h>
#define MOD 1000000007L
using namespace std;

vector<pair<int, int>> edges;

long long pow_mod(long long x, long long k)
{
    if (k == 0)
        return 1L;
    long long ret = pow_mod(x, k / 2);
    return (ret * ret * ((k % 2) ? x : 1)) % MOD;
}

int uf[2000];
int get(int idx)
{
    if (uf[idx] == idx)
        return idx;
    return uf[idx] = get(uf[idx]);
}

int main(void)
{
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        edges.emplace_back(a, b);
    }

    for (int i = 0; i < N; i++)
        uf[i] = i;

    long long answer = 0;
    for (int i = M - 1; i >= 0; i--)
    {
        auto [a, b] = edges[i];
        if (get(0) == get(a) && get(b) == get(N - 1))
        {
            answer = (answer + pow_mod(3, i)) % MOD;
            continue;
        }

        if (get(0) == get(b) && get(a) == get(N - 1))
        {
            answer = (answer + pow_mod(3, i)) % MOD;
            continue;
        }

        uf[get(a)] = get(b);
    }
    
    cout << answer << '\n';

    return 0;
}