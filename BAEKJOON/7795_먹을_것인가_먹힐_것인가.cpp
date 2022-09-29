#include <bits/stdc++.h>

using namespace std;

vector<int> a, b;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        cin >> N >> M;
        a.clear(), b.clear();

        int num;
        for (int i = 0; i < N; i++)
        {
            cin >> num;
            a.push_back(num);
        }

        for (int i = 0; i < M; i++)
        {
            cin >> num;
            b.push_back(num);
        }

        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        int i = 0, j = 0, answer = 0;
        while (i < N)
        {
            if (j < M && a[i] > b[j])
            {
                j++;
                continue;
            }

            answer += j;
            i++;
        }

        cout << answer << '\n';
    }

    return 0;
}