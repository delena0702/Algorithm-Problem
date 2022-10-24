#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int NA, NB;
    vector<int> a, b;
    int num;

    cin >> NA >> NB;
    for (int i = 0; i < NA; i++)
    {
        cin >> num;
        a.push_back(num);
    }
    for (int i = 0; i < NB; i++)
    {
        cin >> num;
        b.push_back(num);
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0;
    int answer = NA + NB;
    while (i < NA && j < NB)
    {
        if (a[i] < b[j])
            i++;
        else if (a[i] > b[j])
            j++;
        else
        {
            answer -= 2;
            i++, j++;
        }
    }

    cout << answer << '\n';

    return 0;
}