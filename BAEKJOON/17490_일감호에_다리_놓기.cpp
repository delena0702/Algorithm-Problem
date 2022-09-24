#include <bits/stdc++.h>
#define INF 987654321

using namespace std;

int arr[1000001];
vector<bool> check;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    long long K;

    cin >> N >> M >> K;

    for (int i = 1; i <= N; i++)
        cin >> arr[i];

    check.resize(N + 1, false);
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        if (abs(a - b) == 1)
            check[min(a, b)] = true;
        else
            check[max(a, b)] = true;
    }

    if (M <= 1) {
        cout << "YES" << '\n';
        return 0;
    }
    
    int s;
    for (s = 1; s <= N; s++)
        if (check[(s + N - 2) % N + 1])
            break;
    
    long long answer = 0;
    int temp = INF;
    for (int i = 0; i < N; i++)
    {
        int idx = (s + i + N - 1) % N + 1;
        temp = min(temp, arr[idx]);

        if (check[idx]) {
            answer += temp;
            temp = INF;
        }
    }
    
    cout << (answer <= K ? "YES" : "NO") << '\n';

    return 0;
}