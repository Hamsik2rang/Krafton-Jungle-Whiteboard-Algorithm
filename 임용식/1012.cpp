#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>
#include <utility>
#include <cstring>

using namespace std;

int m, n, k;
bool check[51][51]{ false };
bool graph[51][51]{ false };

void bfs(int row, int col)
{
	static int dr[]{ -1, 0, 1, 0 };
	static int dc[]{ 0, -1, 0, 1 };

	queue<pair<int, int>> q;
	check[row][col] = true;
	q.push(make_pair(row, col));

	while (!q.empty())
	{
		int cr = q.front().first;
		int cc = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nr = cr + dr[i];
			int nc = cc + dc[i];

			if (nr < 0 || nr >= n || nc < 0 || nc >= m || check[nr][nc] || !graph[nr][nc])
			{
				continue;
			}
			check[nr][nc] = true;
			q.push(make_pair(nr, nc));
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		memset(check, false, sizeof(check));
		memset(graph, false, sizeof(graph));


		cin >> m >> n >> k;

		for (int i = 0; i < k; i++)
		{
			int r, c;
			cin >> c >> r;
			graph[r][c] = true;
		}

		int answer = 0;
		for (int row = 0; row < n; row++)
		{
			for (int col = 0; col < m; col++)
			{
				if (graph[row][col] && !check[row][col])
				{
					bfs(row, col);
					answer++;
				}
			}
		}
		cout << answer << "\n";
	}

	return 0;
}