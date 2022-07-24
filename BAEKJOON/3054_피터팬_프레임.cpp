#include <iostream>
#include <string>

using namespace std;

string input;
int N;

int abs(int x1, int y1, int x2, int y2) {
    if (x1 < x2)
        return abs(x2, y1, x1, y2);
    if (y1 < y2)
        return abs(x1, y2, x2, y1);
    return x1 - x2 + y1 - y2;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> input;
    N = input.length();

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 4 * N + 1; j++)
        {
            if (j%4 == 2 && i == 2)
                cout << input[j / 4];
            else if (j % 12 == 0 && j && i == 2)
                cout << '*';
            else if (j != 4*N && abs(j % 12, i, 10, 2) == 2)
                cout << '*';
            else if (abs(j%4, i, 2, 2) == 2)
                cout << '#';
            else
                cout << '.';
        }
        cout << '\n';
    }

    return 0;
}