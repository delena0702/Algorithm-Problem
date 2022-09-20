#include <bits/stdc++.h>

using namespace std;

int H, V;

struct Words
{
    int x, y;
    string str;
};

vector<Words> rights, downs;
vector<int> edges[1000];

vector<bool> visited;
int matched[1000];

int dfs(int here)
{
    if (visited[here])
        return 0;
    visited[here] = true;

    for (int &there : edges[here])
    {
        if (matched[there] == -1 || dfs(matched[there]))
        {
            matched[there] = here;
            return 1;
        }
    }
    return 0;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    while (T--)
    {
        rights.clear();
        downs.clear();

        cin >> H >> V;
        for (int i = 0; i < H; i++)
        {
            int x, y;
            string s;
            cin >> x >> y >> s;
            rights.push_back({x, y, s});
        }

        for (int i = 0; i < V; i++)
        {
            int x, y;
            string s;
            cin >> x >> y >> s;
            downs.push_back({x, y, s});
        }

        for (int i = 0; i < H; i++)
        {
            edges[i].clear();

            for (int j = 0; j < V; j++)
            {
                auto &r = rights[i];
                auto &d = downs[j];

                bool check = true;

                if (d.x - r.x < 0 || d.x - r.x >= r.str.length())
                    check = false;
                else if (r.y - d.y < 0 || r.y - d.y >= d.str.length())
                    check = false;
                else if (r.str[d.x - r.x] == d.str[r.y - d.y])
                    check = false;

                if (check)
                    edges[i].push_back(j);
            }
        }

        for (int i = 0; i < V; i++)
            matched[i] = -1;

        int answer = H + V;
        for (int i = 0; i < H; i++)
        {
            visited.clear();
            visited.resize(H, false);
            answer -= dfs(i);
        }

        cout << answer << '\n';
    }

    return 0;
}