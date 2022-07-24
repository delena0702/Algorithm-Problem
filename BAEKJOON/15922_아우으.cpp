#include <iostream>
#include <map>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	unsigned int n, length = 0;
	int cnt = 0, start;
	map<int, int> data;

	cin >> n;

	for (unsigned int i = 0; i < 2 * n; i++)
	{
		int x;
		cin >> x;

		if (data.find(x) == data.end())
			data[x] = 2 * (i % 2) - 1;
		else
			data[x] += 2 * (i % 2) - 1;
	}

	for (auto& d : data)
	{
		if (!cnt)
			start = d.first;

		cnt += d.second;

		if (!cnt)
			length += d.first - start;
	}

	cout << length;

	return 0;
}