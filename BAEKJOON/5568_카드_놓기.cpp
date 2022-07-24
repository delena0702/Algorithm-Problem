#include <iostream>
#include <string>
#include <set>

using namespace std;

int N, K;
int input[10];
bool check[10];
set<string> numbers;

void select(int remain, string s)
{
    if (remain == 0)
    {
        numbers.insert(s);
        return;
    }

    for (int i = 0; i < N; i++)
    {
        if (!check[i])
        {
            string temp = s;
            check[i] = true;
            select(remain - 1, temp.append(to_string(input[i])));
            check[i] = false;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> K;
    for (int i = 0; i < N; i++)
        cin >> input[i];

    select(K, "");
    cout << numbers.size() << '\n';

    return 0;
}