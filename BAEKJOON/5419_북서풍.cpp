#include <bits/stdc++.h>
#define SIZE 75000

using namespace std;
typedef pair<int, int> pii;

vector<pii> points;
vector<int> xx, yy;
vector<int> fwtree(SIZE + 1);

void update(int idx) {
	idx++;
	while (idx <= SIZE) {
		fwtree[idx]++;
		idx += -idx & idx;
	}
}

int sum(int idx) {
	idx++;
	int retval = 0;
	while (idx) {
		retval += fwtree[idx];
		idx -= -idx & idx;
	}
	return retval;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T, N, a, b;
	cin >> T;
	while (T--) {
		points.clear();
		xx.clear();
		yy.clear();
		fill(fwtree.begin(), fwtree.end(), 0);

		cin >> N;
		for (int i = 0; i < N; i++)
		{
			cin >> a >> b;
			points.emplace_back(a, b);
			xx.push_back(a);
			yy.push_back(b);
		}

		sort(xx.begin(), xx.end());
		xx.erase(unique(xx.begin(), xx.end()), xx.end());
		sort(yy.begin(), yy.end());
		yy.erase(unique(yy.begin(), yy.end()), yy.end());

		for (auto & p : points) {
			p.first = lower_bound(xx.begin(), xx.end(), p.first) - xx.begin();
			p.second = lower_bound(yy.begin(), yy.end(), p.second) - yy.begin();
		}

		sort(points.begin(), points.end(), [](pii a, pii b) -> bool {
			if (a.first != b.first) return a.first > b.first;
			return a.second < b.second;
		});

		long long answer = 0;
		for (auto & point : points) {
			answer += sum(point.second);
			update(point.second);
		}

		cout << answer << endl;
	}

	return 0;
}