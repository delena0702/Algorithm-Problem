#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int T, N, M;
vector<pair<int, int>> v;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> T;
    int a, b, answer;
    while (T--)
    {
        cin >> N >> M;

        v = vector<pair<int, int>>();
        v.reserve(M);
        for (int i = 0; i < M; i++)
        {
            cin >> a >> b;
            v.push_back(make_pair(a, b));
        }

        sort(v.begin(), v.end());

        priority_queue<int> q;

        answer = 0;
        for (int i = 0, cnt = v[i].first;;)
        {
            while (i < M && v[i].first <= cnt)
                q.push(-v[i++].second);
            while (!q.empty() && -q.top() < cnt)
                q.pop();
            if (!q.empty()) {
                cnt++;
                answer++;
                q.pop();
            }
            else if (i < M)
                cnt = v[i].first;
            else
                break;
        }

        cout << answer << '\n';
    }

    return 0;
}