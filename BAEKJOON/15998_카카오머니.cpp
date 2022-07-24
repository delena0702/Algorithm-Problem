#include <iostream>

using namespace std;

long long gcd(long long a, long long b) {
	if (b == 0) return a;
	if (b > a) return gcd(b, a);
	return gcd(b, a%b);
}

int main(void) {
	int n;
	long long a = 0, b, c;
	long long d = 0, e = 0;

	cin.sync_with_stdio(false);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> b >> c;

		if (b < 0) {
			if (a + b >= 0 && a + b != c) {
				cout << -1;
				return 0;
			}

			if (a + b < 0) {
				if (d == 0) d = c - a - b;
				else d = gcd(d, c - a - b);
				e = (e > c) ? e : c;
			}
		}
		else if (a + b != c) {
			cout << -1;
			return 0;
		}

		a = c;
	}

	if (d == 0) cout << 1;
	else if (d > e) cout << d;
	else cout << -1;

	return 0;
}