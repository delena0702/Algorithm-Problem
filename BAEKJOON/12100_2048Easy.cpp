#include <iostream>

unsigned int n;

struct Board {
	unsigned int data[20][20];

	Board() :data{ 0, } {}

	unsigned int max()
	{
		unsigned int i, j, max = 0;

		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				if (data[i][j] > max)
					max = data[i][j];

		return max;
	}

	void show()
	{
		for (unsigned int i = 0; i < n; i++)
		{
			for (unsigned int j = 0; j < n; j++)
			{
				std::cout << data[i][j] << " ";
			}
			std::cout << std::endl;
		}
		std::cout << std::endl;
	}

	Board up()
	{
		Board retval;
		unsigned int i, j, k;
		bool check;

		for (i = 0; i < n; i++)
		{
			check = false;
			for (j = 0, k = 0; j < n; j++)
			{
				if (data[j][i])
				{
					if (!check && k != 0 && data[j][i] == retval.data[k - 1][i])
					{
						retval.data[k - 1][i] <<= 1;
						check = true;
					}

					else
					{
						retval.data[k++][i] = data[j][i];
						check = false;
					}
				}
			}
		}

		return retval;
	}

	Board down()
	{
		Board retval;
		unsigned int i, j, k;
		bool check;

		for (i = 0; i < n; i++)
		{
			check = false;
			for (j = n - 1, k = n - 1; j != -1; j--)
			{
				if (data[j][i])
				{
					if (!check && k != n - 1 && data[j][i] == retval.data[k + 1][i])
					{
						retval.data[k + 1][i] <<= 1;
						check = true;
					}

					else
					{
						retval.data[k--][i] = data[j][i];
						check = false;
					}
				}
			}
		}

		return retval;
	}

	Board left()
	{
		Board retval;
		unsigned int i, j, k;
		bool check;

		for (i = 0; i < n; i++)
		{
			check = false;
			for (j = 0, k = 0; j < n; j++)
			{
				if (data[i][j])
				{
					if (!check && k != 0 && data[i][j] == retval.data[i][k - 1])
					{
						retval.data[i][k - 1] <<= 1;
						check = true;
					}

					else
					{
						retval.data[i][k++] = data[i][j];
						check = false;
					}
				}
			}
		}

		return retval;
	}

	Board right()
	{
		Board retval;
		unsigned int i, j, k;
		bool check;

		for (i = 0; i < n; i++)
		{
			check = false;
			for (j = n - 1, k = n - 1; j != -1; j--)
			{
				if (data[i][j])
				{
					if (!check && k != n - 1 && data[i][j] == retval.data[i][k + 1])
					{
						retval.data[i][k + 1] <<= 1;
						check = true;
					}

					else
					{
						retval.data[i][k--] = data[i][j];
						check = false;
					}
				}
			}
		}

		return retval;
	}
};

unsigned int dps(Board board, unsigned int depth)
{
	if (depth == 5) return board.max();

	unsigned int max = 0, temp;

	if ((temp = dps(board.up(), depth + 1)) > max) max = temp;
	if ((temp = dps(board.down(), depth + 1)) > max) max = temp;
	if ((temp = dps(board.left(), depth + 1)) > max) max = temp;
	if ((temp = dps(board.right(), depth + 1)) > max) max = temp;

	return max;
}

int main(void)
{
	Board board;
	unsigned int i, j;

	std::cin >> n;

	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			std::cin >> board.data[i][j];

	std::cout << dps(board, 0);

	return 0;
}