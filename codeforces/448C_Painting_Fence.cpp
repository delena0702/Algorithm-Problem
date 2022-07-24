#include <bits/stdc++.h>

#define SIZE 5000
#define INF 1000000001

using namespace std;

int N, arr[SIZE];

// Divide and Conquer
// Solve in sub-array [s,e) and height >= base
int solve(int s = 0, int e = N, int base = 0)
{
    if (e - s == 0)
        return 0;
    if (e - s == 1 && arr[s] == base)
        return 0;

    int min_height = INF, min_ind = 0;
    // save minimum height and index
    for (int i = s; i < e; i++)
    {
        if (arr[i] < min_height)
        {
            min_ind = i;
            min_height = min(min_height, arr[i]);
        }
    }

    if (e - s <= min_height - base)
        return e - s;
    return min(e - s, min_height - base + solve(s, min_ind, min_height) + solve(min_ind + 1, e, min_height));
}

int main(void)
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        arr[i] = temp;
    }

    printf("%d\n", solve());

    return 0;
}