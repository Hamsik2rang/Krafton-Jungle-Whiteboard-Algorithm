#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int r, c;
vector<string> graph;
vector<pair<int, int>> sheeps;

bool SetFence(int row, int col)
{
	static int dr[]{ -1, 0, 1, 0 };
	static int dc[]{ 0, -1, 0, 1 };

	for (int i = 0; i < 4; i++)
	{
		int nr = row + dr[i];
		int nc = col + dc[i];
		if (nr < 0 || nr >= r || nc < 0 || nc >= c || graph[nr][nc] == 'S')
		{
			continue;
		}

		if (graph[nr][nc] == 'W')
		{
			return false;
		}
		graph[nr][nc] = 'D';
	}

	return true;
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> r >> c;
	graph.assign(r, "");
	for (int i = 0; i < r; i++)
	{
		cin >> graph[i];
		for (int j = 0; j < c; j++)
		{
			if (graph[i][j] == 'S')
			{
				sheeps.push_back(make_pair(i, j));
			}
		}
	}

	for (int i = 0; i < sheeps.size(); i++)
	{
		bool result = SetFence(sheeps[i].first, sheeps[i].second);
		if (!result)
		{
			cout << 0;
			return 0;
		}
	}
	cout << 1 << "\n";
	for (const auto& s : graph)
	{
		cout << s << "\n";
	}


	return 0;
}