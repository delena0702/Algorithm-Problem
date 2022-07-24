#include <iostream>
#include <queue>
#define LIMIT 400

using namespace std;

int N, P;
int edges[LIMIT + 1][LIMIT + 1], flow[LIMIT + 1][LIMIT + 1];

int max_flow(int s, int e)
{
    int answer = 0;
    while (true)
    {
        int visited[LIMIT + 1] = {
            0,
        };
        queue<int> q;

        q.push(s);
        visited[s] = s;
        while (!q.empty())
        {
            int here = q.front();
            if (here == e)
                break;
            q.pop();

            for (int there = 1; there <= N; there++)
            {
                if (visited[there])
                    continue;
                if (edges[here][there] <= flow[here][there])
                    continue;

                visited[there] = here;
                q.push(there);
            }
        }

        if (q.empty())
            return answer;

        for (int t = e; t != visited[t]; t = visited[t])
        {
            int s = visited[t];
            flow[s][t]++;
            flow[t][s]--;
        }

        answer++;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> P;
    int a, b;
    for (int i = 0; i < P; i++)
    {
        cin >> a >> b;
        edges[a][b] = 1;
    }

    cout << max_flow(1, 2);

    return 0;
}