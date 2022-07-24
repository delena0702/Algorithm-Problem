#include <iostream>

int main(void)
{
	unsigned int n, m, i, j, num, cnt = 0, in;

	std::cin >> n >> m;

	if (n >= m)
	{
		std::cout << n - m;
		return 0;
	}

	for (i = 0, num = n; num < m; i++)
		num <<= 1;

	in = num - m;
	for (j = 0; j < i && in; j++)
	{
		if (in & 0x1)
			cnt++;
		in >>= 1;
	}

	std::cout << i + cnt + in;
	return 0;
}