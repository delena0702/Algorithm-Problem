#include <bits/stdc++.h>

using namespace std;

int is_prime[100001];
int prime_cnt[100001];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int A, B;
    cin >> A >> B;

    is_prime[1] = 1;
    for (int i = 2; i <= B; i++)
    {
        if (is_prime[i])
            continue;

        prime_cnt[i] = 1;

        for (int j = 2 * i; j <= B; j += i)
        {
            is_prime[j] = i;
            prime_cnt[j] = prime_cnt[j / i] + 1;
        }
    }

    int answer = 0;
    for (int i = A; i <= B; i++)
        if (is_prime[prime_cnt[i]] == 0)
            answer++;
        
    cout << answer << '\n';

    return 0;
}