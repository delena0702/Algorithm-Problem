#include <bits/stdc++.h>

using namespace std;

struct Score
{
    string s;
    int kor, eng, mat;
};

vector<Score> arr;

bool comp(Score &a, Score &b)
{
    if (a.kor != b.kor)
        return a.kor > b.kor;
    if (a.eng != b.eng)
        return a.eng < b.eng;
    if (a.mat != b.mat)
        return a.mat > b.mat;
    return a.s < b.s;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string s;
        int a, b, c;
        cin >> s >> a >> b >> c;
        arr.push_back({s, a, b, c});
    }

    sort(arr.begin(), arr.end(), comp);

    for (int i = 0; i < N; i++)
        cout << arr[i].s << '\n';

    return 0;
}