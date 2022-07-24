#include <iostream>
#include <map>

int main(void)
{
	unsigned int  n, * data, * dp, * cnt;
	std::map<unsigned int, unsigned int> tree;
	unsigned int max_ind, max_cnt;

	std::cin >> n;

	data = new unsigned int[n];
	dp = new unsigned int[n];
	cnt = new unsigned int[n];

	for (unsigned int i = 0; i < n; i++)
	{
		std::cin >> data[i];
		cnt[i] = 0;
	}

	max_ind = -1;
	max_cnt = 0;

	for (unsigned int i = n - 1; i != -1; i--)
	{
		if (tree.count(data[i] + 1))
		{
			dp[i] = tree[data[i] + 1];
			cnt[i] = cnt[dp[i]] + 1;
		}
		else
		{
			dp[i] = -1;
			cnt[i] = 1;
		}

		tree[data[i]] = i;

		if (cnt[i] > max_cnt)
		{
			max_ind = i;
			max_cnt = cnt[i];
		}
	}

	std::cout << max_cnt << std::endl;
	for (unsigned int i = max_ind; i != -1; i = dp[i])
		std::cout << i + 1 << " ";

	delete[] data;
	delete[] dp;
	delete[] cnt;

	return 0;
}