#include <iostream>

int main(void)
{
	unsigned int n, m, k;
	unsigned int* num;
	unsigned int x = 1, y = 1;
	unsigned int i, j;

	std::cin >> n >> m >> k;

	num = new unsigned int[k];

	for (i = 0; i < k; i++)
		num[i] = (n * m + i) / k;

	for (i = 0; i < k; i++)
	{
		std::cout << num[i];

		for (j = 0; j < num[i]; j++)
		{
			std::cout << " " << y << " " << x;

			if (y & 0x1)
			{
				if (x == m)
					y++;
				else
					x++;
			}

			else
			{
				if (x == 1)
					y++;
				else
					x--;
			}
		}

		std::cout << std::endl;
	}

	delete[] num;

	return 0;
}