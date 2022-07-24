#include <iostream>
#include <vector>

std::vector<unsigned int> data[200];
unsigned int check[200] = { 0, };
bool visited[200] = { 0, };
unsigned int n, m;

bool dfs(unsigned int x)
{
	unsigned int temp;

	if (visited[x])
		return false;
	visited[x] = true;

	for (unsigned int ind : data[x])
	{
		temp = check[ind];

		if (!temp || dfs(temp - 1))
		{
			check[ind] = x + 1;
			return true;
		}
	}

	return false;
}

int main(void)
{
	unsigned int k, inp, i, j, cnt = 0;

	std::cin >> n >> m;

	for (i = 0; i < n; i++)
	{
		std::cin >> k;

		for (j = 0; j < k; j++)
		{
			std::cin >> inp;
			data[i].push_back(inp - 1);
		}
	}

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
			visited[j] = false;
		if (dfs(i))
			cnt++;
	}

	std::cout << cnt;

	return 0;
}