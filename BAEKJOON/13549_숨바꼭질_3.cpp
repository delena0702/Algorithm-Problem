#include <bits/stdc++.h>
#define INF INT_MAX

using namespace std;

int bfs(int s, int t)
{
    deque<int> q;
    q.push_back(s);

    vector<int> dijk(200001, INF);
    dijk[s] = 0;

    while (!q.empty())
    {
        int here = q.front();
        q.pop_front();

        if (here == t)
            break;

        if (here)
            for (int there = here << 1; there <= 200000; there <<= 1)
            {
                if (dijk[there] <= dijk[here])
                    continue;

                dijk[there] = dijk[here];
                q.push_front(there);
            }

        for (int there : {here - 1, here + 1})
        {
            if (there < 0 || there > 200000)
                continue;
            if (dijk[there] <= dijk[here] + 1)
                continue;

            dijk[there] = dijk[here] + 1;
            q.push_back(there);
        }
    }

    return dijk[t];
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, K;
    cin >> N >> K;
    cout << bfs(N, K) << '\n';

    return 0;
}