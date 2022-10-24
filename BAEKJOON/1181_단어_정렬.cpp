// 질문 답변을 위한 소스코드 테스트
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(const string a, const string b)
{
    if (a.length() == b.length())
        return a < b;
    return a.length() < b.length();
}

int main()
{
    int n;
    cin >> n;
    vector<string> v;
    string str;
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> str;
        if (find(v.begin(), v.end(), str) == v.end()) {
            v.push_back(str);
        }
    }
    sort(v.begin(), v.end(), compare);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << "\n";
    }
}