#include <bits/stdc++.h>

using namespace std;

struct Position
{
    int i;
    char j;
    int k;

    bool operator<(Position &a)
    {
        return this->i < a.i;
    }
};

vector<Position> arr;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int ii, k;
        char j;
        cin >> ii >> j >> k;
        arr.push_back({ii, j, k});
    }

    sort(arr.begin(), arr.end());

    int here;
    cin >> here;
    here = 0;
    
    while (true)
    {
        int s = 0, e = N - 1;
        int value = arr[here].i + arr[here].k;
        if (arr[here].j == 'L')
            value = arr[here].i - arr[here].k;

        int next = -1;
        while (s <= e)
        {
            int m = (s + e) / 2;
            if (value < arr[m].i)
                e = m - 1;
            else if (value > arr[m].i)
                s = m + 1;
            else
            {
                next = m;
                break;
            }
        }

        if (next == -1)
        {
            cout << value << '\n';
            break;
        }

        here = next;
    }

    return 0;
}