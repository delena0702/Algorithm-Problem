#include <bits/stdc++.h>

#define SIZE 200000

using namespace std;

int N, Q;

long long tree[SIZE + 1]; // Fenwick Tree
long long arr[SIZE + 1];
long long result[SIZE + 1];

void update(int ind, int value)
{
    for (; ind <= N; ind += -ind & ind)
        tree[ind] += value;
}

long long query(int ind)
{
    long long result = 0;
    for (; ind; ind -= -ind & ind)
        result += tree[ind];
    return result;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> Q;

    for (int i = 1; i <= N; i++)
    {
        long long temp;
        cin >> temp;
        arr[i] = temp;
    }

    while (Q--)
    {
        int left, right;
        cin >> left >> right;

        update(right + 1, -1);
        update(left, 1);
    }

    for (int i = 1; i <= N; i++)
        result[i] = query(i);

    sort(arr + 1, arr + N + 1);
    sort(result + 1, result + N + 1);

    long long answer = 0;
    for (int i = 1; i <= N; i++)
        answer += arr[i] * result[i];
    
    cout << answer << '\n';
    return 0;
}