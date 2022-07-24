#include <iostream>
#include <list>

int main(void)
{
	unsigned int n, k1, k2;
	std::list<unsigned int> l1, l2;
	unsigned int ui;
	unsigned int i;

	std::cin >> n >> k1;
	for (i = 0; i < k1; i++)
	{
		std::cin >> ui;
		l1.push_back(ui);
	}

	std::cin >> k2;
	for (i = 0; i < k2; i++)
	{
		std::cin >> ui;
		l2.push_back(ui);
	}

	unsigned int round, num1, num2;

	for (round = 0; round < 10000 && k1 && k2; round++)
	{
		num1 = l1.front();
		l1.pop_front();
		num2 = l2.front();
		l2.pop_front();

		if (num1 > num2)
		{
			l1.push_back(num2);
			l1.push_back(num1);
			k1++;
			k2--;
		}

		else
		{
			l2.push_back(num1);
			l2.push_back(num2);
			k1--;
			k2++;
		}
	}

	if (!k2)
		std::cout << round << " 1";
	else if (!k1)
		std::cout << round << " 2";
	else
		std::cout << -1;

	return 0;
}