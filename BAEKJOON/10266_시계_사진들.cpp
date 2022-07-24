#include <iostream>
#include <vector>
#define LIMIT 360000

using namespace std;

int N;
bool arr[2][LIMIT];
int p[LIMIT];

void makeP(void)
{
    int begin = 1, matched = 0;

    for (int begin = 1, matched = 0; begin + matched < LIMIT;)
    {
        if (arr[0][begin + matched] == arr[0][matched])
        {
            matched++;
            p[begin + matched - 1] = matched;
        }

        else
        {
            if (matched == 0)
                begin++;
            else
            {
                begin += matched - p[matched - 1];
                matched = p[matched - 1];
            }
        }
    }
}

bool KMP()
{
    for (int begin = 0, matched = 0; begin < LIMIT;)
    {
        if (arr[0][matched] == arr[1][(begin + matched) % LIMIT])
        {
            matched++;
            if (matched == LIMIT)
                return true;
        }

        else
        {
            if (matched == 0)
                begin++;

            else
            {
                begin += matched - p[matched - 1];
                matched = p[matched - 1];
            }
        }
    }
    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    int temp;
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> temp;
            arr[i][temp] = true;
        }
    }

    makeP();
    cout << (KMP() ? "possible" : "impossible");

    return 0;
}