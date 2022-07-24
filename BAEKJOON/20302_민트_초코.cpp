#include <bits/stdc++.h>
#define SIZE 100000

using namespace std;

int cnt[SIZE];

void setVal(int number, int addVal)
{
    number = abs(number);
    for (int i = 2; i * i <= number; i++)
    {
        if (number % i == 0)
        {
            number = number / i;
            cnt[i--] += addVal;
        }
    }

    if (number > 1)
        cnt[number] += addVal;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, temp, ch;
    cin >> N;

    cin >> temp;
    setVal(temp, 1);
    if (temp == 0)
    {
        cout << "mint chocolate";
        return 0;
    }

    for (int i = 1; i < N; i++)
    {
        cin.ignore(1);
        ch = cin.get();
        cin >> temp;
        if (temp == 0)
        {
            cout << "mint chocolate";
            return 0;
        }

        switch (ch)
        {
        case '*':
            setVal(temp, 1);
            break;
        case '/':
            setVal(temp, -1);
            break;
        }
    }

    for (int i = 0; i < SIZE; i++)
    {
        if (cnt[i] < 0)
        {
            cout << "toothpaste";
            break;
        }

        if (i == SIZE - 1)
            cout << "mint chocolate";
    }

    return 0;
}