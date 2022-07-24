#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int N, M, K;
vector<pair<int, int>> blue, red;
int check[1001];

int kruskal(bool isMax)
{
    int retval = 0, cnt = 0;
    vector<pair<int, int>> queue(isMax ? blue : red);
    if (isMax)
        queue.insert(queue.end(), red.begin(), red.end());
    else
        queue.insert(queue.end(), blue.begin(), blue.end());

    for (int i = 1; i <= N; i++)
        check[i] = i;

    for (int i = 0; i < M; i++)
    {
        pair<int, int> &p = queue[i];
        int a = p.first, b = p.second;

        for (; check[a] != a; a = check[a])
            ;
        for (; check[b] != b; b = check[b])
            ;

        if (a == b)
            continue;

        check[b] = a;
        cnt++;
        if (isMax && i < blue.size() || !isMax && i >= red.size())
            retval++;
        
        if (cnt == N - 1)
            return retval;
    }

    return -1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    while (true)
    {
        cin >> N >> M >> K;
        if (N == 0)
            break;

        blue = vector<pair<int, int>>();
        red = vector<pair<int, int>>();

        for (int i = 0; i < M; i++)
        {
            char ch;
            int a, b;

            cin >> ch >> a >> b;
            if (ch == 'B')
                blue.push_back(make_pair(a, b));
            else
                red.push_back(make_pair(a, b));
        }

        if (K >= kruskal(false) && K <= kruskal(true))
            cout << "1\n";
        else
            cout << "0\n";
    }
    return 0;
}
