#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>

#define MAXN 500001

using namespace std;

int check[MAXN];
vector<int> v[MAXN];
int leafInfo;
void SetTree(int x, int parent, int height)
{
	check[x] = true;
	bool isLeaf = true;
	for (int i = 0; i < v[x].size(); i++)
	{
		int next = v[x][i];
		if (!check[next])
		{
			isLeaf = false;
			SetTree(next, x, height + 1);
		}
	}
	if (isLeaf)
	{
		leafInfo += height;
	}
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int from, to;
		cin >> from >> to;
		v[from].push_back(to);
		v[to].push_back(from);
	}

	SetTree(1, 0, 0);
	cout << (leafInfo % 2 ? "Yes" : "No");

	return 0;
}