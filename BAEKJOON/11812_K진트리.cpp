#include <iostream>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	unsigned long long n;
	unsigned int k, q;

	cin >> n >> k >> q;

	for (unsigned int i = 0; i < q; i++)
	{
		unsigned int cnt;
		unsigned long long x, y;

		cin >> x >> y;

		if (k == 1)
		{
			if (x > y)
				cout << x - y << '\n';
			else
				cout << y - x << '\n';
			continue;
		}

		for (cnt = 0; x != y; cnt++)
		{
			if (x > y)
				x = (x + k - 2) / k;
			else
				y = (y + k - 2) / k;
		}

		cout << cnt << '\n';
	}

	return 0;
}