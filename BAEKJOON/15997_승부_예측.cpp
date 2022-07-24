#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> name(4);
double p[4][4][3] = { 0, };
double win[4] = { 0.0, };

const int winPointd[3][2] = {
	{ 3,0 },
	{ 1,1 },
	{ 0,3 }
};

void makeWin(int a, int b, double k, int winPoint[4]) {
	if (a == 3) {
		int rank[4] = { 0, 1, 2, 3 };
		int temp;

		for (int i = 0; i < 3; i++) {
			for (int j = i + 1; j < 4; j++) {
				if (winPoint[rank[i]] < winPoint[rank[j]]) {
					temp = rank[i];
					rank[i] = rank[j];
					rank[j] = temp;
				}
			}
		}

		if (winPoint[rank[1]] == winPoint[rank[2]]) {
			if (winPoint[rank[0]] == winPoint[rank[1]]) {
				if (winPoint[rank[1]] == winPoint[rank[3]]) {
					win[rank[0]] += k / 2;
					win[rank[1]] += k / 2;
					win[rank[2]] += k / 2;
					win[rank[3]] += k / 2;
				}

				else {
					win[rank[0]] += k * 2 / 3;
					win[rank[1]] += k * 2 / 3;
					win[rank[2]] += k * 2 / 3;
				}
			}

			else {
				win[rank[0]] += k;

				if (winPoint[rank[1]] == winPoint[rank[3]]) {
					win[rank[1]] += k / 3;
					win[rank[2]] += k / 3;
					win[rank[3]] += k / 3;
				}

				else {
					win[rank[1]] += k / 2;
					win[rank[2]] += k / 2;
				}
			}
		}

		else {
			win[rank[0]] += k;
			win[rank[1]] += k;
		}

		return;
	}

	double nk;

	for (int i = 0; i < 3; i++) {
		int temp[4] = { winPoint[0], winPoint[1], winPoint[2], winPoint[3] };
		temp[a] += winPointd[i][0];
		temp[b] += winPointd[i][1];

		nk = k*p[a][b][i];

		if (b == 3) makeWin(a + 1, a + 2, nk, temp);
		else makeWin(a, b + 1, nk, temp);
	}
}

int main(void) {
	cin.sync_with_stdio(false);

	for (int i = 0; i < 4; i++)
		cin >> name[i];

	string s;
	int ind[2];
	double d[3];

	for (int i = 0; i < 6; i++) {
		cin >> s;
		ind[0] = find(name.begin(), name.end(), s) - name.begin();
		cin >> s;
		ind[1] = find(name.begin(), name.end(), s) - name.begin();

		for (int j = 0; j < 3; j++)
			cin >> d[j];

		p[ind[0]][ind[1]][0] = d[0];
		p[ind[0]][ind[1]][1] = d[1];
		p[ind[0]][ind[1]][2] = d[2];

		p[ind[1]][ind[0]][0] = d[2];
		p[ind[1]][ind[0]][1] = d[1];
		p[ind[1]][ind[0]][2] = d[0];
	}

	int temp[4] = {0, };
	makeWin(0, 1, 1, temp);

	for (int i = 0; i < 4; i++) {
		cout << win[i] << endl;
	}

	return 0;
}