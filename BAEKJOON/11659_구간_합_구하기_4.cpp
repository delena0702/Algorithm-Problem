#include <bits/stdc++.h>

using namespace std;

int psum[100001];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        int num;
        cin >> num;
        psum[i] = psum[i - 1] + num;
    }

    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        cout << psum[b] - psum[a - 1] << '\n';
    }

    return 0;
}