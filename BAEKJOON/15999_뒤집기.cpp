#include <iostream>
#include <string>

using namespace std;

const int MOD = 1000000007;
const int MOVE[4][2] = { { 1,0 },{ 0,1 },{ -1,0 },{ 0,-1 } };

int n, m;

int pow2(int n) {
	if (n == 0) return 1;
	if (n == 1) return 2;
	if (n % 2) return ((long long)pow2(n / 2)*pow2(n / 2 + 1))%MOD;
	return ((long long)pow2(n / 2)*pow2(n / 2)) % MOD;
}

int main(void) {
	cin.sync_with_stdio(false);

	cin >> n >> m;

	string *s = new string[n];

	cin.ignore();
	for (int i = 0; i < n; i++)
		getline(cin, s[i]);

	int count = n*m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			char ch = s[i][j];

			for (int k = 0; k < 4; k++) {
				int nx = j + MOVE[k][0], ny = i + MOVE[k][1];
				if ((nx < 0) || (ny < 0) || (nx >= m) || (ny >= n)) continue;
				if (ch != s[ny][nx]) {
					count--;
					break;
				}
			}
		}
	}

	cout << pow2(count);
	delete[] s;

	return 0;
}