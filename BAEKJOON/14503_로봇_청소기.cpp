#include <bits/stdc++.h>

using namespace std;

int N, M, arr[55][55];

int darr[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int r, c, d;

    cin >> N >> M;
    cin >> r >> c >> d;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> arr[i][j];

    int answer = 0;
    while (true)
    {
        bool check = false;

        arr[r][c] = 2;
        answer++;

        while (true)
        {
            bool check2 = false;
            for (int i = 3; i >= 0; i--)
            {
                int nd = (d + i) % 4;
                auto &[dr, dc] = darr[nd];
                int nr = r + dr, nc = c + dc;

                if (nr < 0 || nr >= N || nc < 0 || nc >= M)
                    continue;
                if (arr[nr][nc])
                    continue;

                r = nr;
                c = nc;
                d = nd;
                check2 = true;
                break;
            }

            if (check2)
                break;
            
            int nd = (d + 2) % 4;
            auto &[dr, dc] = darr[nd];
            int nr = r + dr, nc = c + dc;

            if (nr < 0 || nr >= N || nc < 0 || nc >= M)
                check = true;
            if (check || arr[nr][nc] == 1)
                check = true;
            
            if (check)
                break;

            r = nr;
            c = nc;
        }

        if (check)
            break;
    }

    cout << answer << '\n';

    return 0;
}