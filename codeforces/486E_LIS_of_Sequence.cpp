#include <bits/stdc++.h>

#define SIZE 100000

using namespace std;

int N, arr[SIZE];
int checkLIS[SIZE];
bool checkMust[SIZE];
vector<int> last, dlast;

int main(void)
{
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        arr[i] = temp;
    }

    for (int i = 0; i < N; i++)
    {
        int ind = lower_bound(last.begin(), last.end(), arr[i]) - last.begin();
        if (ind == last.size())
            last.push_back(arr[i]);
        else
            last[ind] = arr[i];
        checkLIS[i] += ind + 1;

        ind = lower_bound(dlast.begin(), dlast.end(), -arr[N - i - 1]) - dlast.begin();
        if (ind == dlast.size())
            dlast.push_back(-arr[N - i - 1]);
        else
            dlast[ind] = -arr[N - i - 1];
        checkLIS[N - i - 1] += ind + 1;
    }

    int lmax = last.size() + 1;

    int max_value = 0;
    for (int i = 0; i < N; i++)
    {
        if (checkLIS[i] != lmax)
            continue;
        if (arr[i] <= max_value)
            continue;
        checkMust[i] = true;
        max_value = arr[i];
    }

    int min_value = 654321;
    for (int i = N - 1; i >= 0; i--)
    {
        if (checkLIS[i] != lmax)
            continue;
        if (arr[i] < min_value)
            min_value = arr[i];
        else
            checkMust[i] = false;
    }

    for (int i = 0; i < N; i++)
    {
        if (checkLIS[i] != lmax)
            printf("1");
        else if (!checkMust[i])
            printf("2");
        else
            printf("3");
    }

    return 0;
}