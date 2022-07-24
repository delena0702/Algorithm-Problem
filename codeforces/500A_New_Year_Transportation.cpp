#include <bits/stdc++.h>

#define SIZE 30000

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, T;
    cin >> N >> T;

    int here = 1;
    bool answer = false;
    
    for (int i = 1; i <= N - 1; i++)
    {
        int next;
        cin >> next;

        if (i == here)
            here += next;
        if (here == T)
            answer = true;
    }

    cout << (answer ? "YES\n" : "NO\n");

    return 0;
}