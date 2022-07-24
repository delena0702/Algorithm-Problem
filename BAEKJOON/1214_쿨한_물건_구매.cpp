#include <iostream>
#define INF 99876543210LL

using namespace std;

typedef long long TYPE;

TYPE D, P, Q;

TYPE min(const TYPE &a, const TYPE &b)
{
    return a < b ? a : b;
}

TYPE gcd(const TYPE &a, const TYPE &b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> D >> P >> Q;

    if (P < Q)
    {
        TYPE temp = P;
        P = Q;
        Q = temp;
    }

    TYPE g = gcd(P, Q);

    D = (D - 1) / g + 1;
    P /= g;
    Q /= g;

    if (D >= P * Q)
    {
        cout << g * D;
        return 0;
    }

    TYPE answer = INF;
    for (TYPE i = 0; i < D; i += P)
    {
        if ((D - i) % Q == 0)
            answer = D;
        else
            answer = min(answer, D + Q - (D - i) % Q);
        if (answer == D)
            break;
    }
    answer = min(answer, ((D - 1) / P + 1) * P);

    cout << g * answer;
    
    return 0;
}
