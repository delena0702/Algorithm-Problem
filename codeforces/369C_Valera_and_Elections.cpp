#include <iostream>
#include <vector>

class Edge {
public:
	unsigned int node;
	bool weight;

	Edge(unsigned int node, bool weight) :node(node), weight(weight) {}
};

unsigned int _dfs(bool* output, std::vector<Edge>* tree, unsigned int node, unsigned int parent, bool weight)
{
	unsigned int check = 0;

	for (Edge& e : tree[node])
	{
		if (e.node == parent)
			continue;

		check += _dfs(output, tree, e.node, node, e.weight);
	}

	if (check)
		return check;
	if (!weight)
		return 0;
	output[node] = true;
	return 1;
}

unsigned int dfs(bool* output, std::vector<Edge>* tree)
{
	unsigned int check = 0;

	for (Edge& e : tree[0])
		check += _dfs(output, tree, e.node, 0, e.weight);

	return check;
}

int main(void)
{
	std::vector<Edge>* tree;
	bool* output;
	unsigned int n;

	std::cin >> n;

	tree = new std::vector<Edge>[n];
	output = new bool[n];

	for (unsigned int i = 0; i < n; i++)
		output[i] = false;

	for (unsigned int i = 0; i < n - 1; i++)
	{
		unsigned int x, y, t;
		std::cin >> x >> y >> t;

		tree[x - 1].push_back(Edge(y - 1, t == 2));
		tree[y - 1].push_back(Edge(x - 1, t == 2));
	}

	std::cout << dfs(output, tree) << std::endl;

	for (unsigned int i = 0; i < n; i++)
	{
		if (output[i])
			std::cout << i + 1 << " ";
	}

	delete[] tree;
	delete[] output;
}