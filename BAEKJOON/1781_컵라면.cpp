#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int>a, pair<int, int>b) {
    return a.first > b.first;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<pair<int, int>> data;

    for (int i=0; i<N; i++) {
        int a, b;
        cin >> a >> b;
        data.push_back(make_pair(a, b));
    }

    sort(data.begin(), data.end(), compare);

    int ind = 0, sum = 0;
    priority_queue<int> pq;

    for (int i=N; i>=1; i--) {
        while (ind < data.size() && i == data[ind].first)
            pq.push(data[ind++].second);
        
        if (!pq.empty()) {
            sum += pq.top();
            pq.pop();
        }
    }

    cout << sum;
    return 0;
}
