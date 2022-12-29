#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <utility>

#define MAXN 8
#define TRACE 10

using namespace std;

int n, m;
int room[MAXN][MAXN];
int zeroCount = 0;
vector<pair<int, int>> cameras;

int watch(int row, int col, const int dr, const int dc, const int index, int count)
{
	if (row < 0 || row >= n || col < 0 || col >= m || room[row][col] == 6)
		return count;

	if (room[row][col] == 0)
	{
		room[row][col] = TRACE + index;
		count++;
	}

	return watch(row + dr, col + dc, dr, dc, index, count);
}

void deleteTrace(int row, int col, const int dr, const int dc, const int index)
{
	if (row < 0 || row >= n || col < 0 || col >= m || room[row][col] == 6)
		return;
	if (room[row][col] == TRACE + index)
	{
		room[row][col] = 0;
	}
	deleteTrace(row + dr, col + dc, dr, dc, index);
}

int solution(int index, int count)
{
	static int dr[] = { -1, 0, 1, 0 };
	static int dc[] = { 0, -1, 0, 1 };

	int answer = 0;
	if (index == cameras.size())
		return count;

	int curCameraRow = cameras[index].first;
	int curCameraCol = cameras[index].second;
	int curCamera = room[curCameraRow][curCameraCol];

	switch (curCamera)
	{
	case 1:
		{
			for (int i = 0; i < 4; i++)
			{
				int watchCount = watch(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index, 0);
				int result = solution(index + 1, count + watchCount);
				answer = answer > result ? answer : result;
				deleteTrace(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index);
			}
		}
		break;
	case 2:
		{
			for (int i = 0; i < 2; i++)
			{
				int watchCount = watch(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index, 0)
					+ watch(curCameraRow + dr[i + 2], curCameraCol + dc[i + 2], dr[i + 2], dc[i + 2], index, 0);
				int result = solution(index + 1, count + watchCount);
				answer = answer > result ? answer : result;
				deleteTrace(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index);
				deleteTrace(curCameraRow + dr[i + 2], curCameraCol + dc[i + 2], dr[i + 2], dc[i + 2], index);
			}
		}
		break;
	case 3:
		{
			for (int i = 0; i < 4; i++)
			{
				int watchCount = watch(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index, 0)
					+ watch(curCameraRow + dr[(i + 1) % 4], curCameraCol + dc[(i + 1) % 4], dr[(i + 1) % 4], dc[(i + 1) % 4], index, 0);
				int result = solution(index + 1, count + watchCount);
				answer = answer > result ? answer : result;
				deleteTrace(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index);
				deleteTrace(curCameraRow + dr[(i + 1) % 4], curCameraCol + dc[(i + 1) % 4], dr[(i + 1) % 4], dc[(i + 1) % 4], index);
			}
		}
		break;
	case 4:
		{
			for (int i = 0; i < 4; i++)
			{
				int watchCount = watch(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index, 0)
					+ watch(curCameraRow + dr[(i + 1) % 4], curCameraCol + dc[(i + 1) % 4], dr[(i + 1) % 4], dc[(i + 1) % 4], index, 0)
					+ watch(curCameraRow + dr[(i + 2) % 4], curCameraCol + dc[(i + 2) % 4], dr[(i + 2) % 4], dc[(i + 2) % 4], index, 0);
				int result = solution(index + 1, count + watchCount);
				answer = answer > result ? answer : result;
				deleteTrace(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index);
				deleteTrace(curCameraRow + dr[(i + 1) % 4], curCameraCol + dc[(i + 1) % 4], dr[(i + 1) % 4], dc[(i + 1) % 4], index);
				deleteTrace(curCameraRow + dr[(i + 2) % 4], curCameraCol + dc[(i + 2) % 4], dr[(i + 2) % 4], dc[(i + 2) % 4], index);
			}
		}
		break;
	case 5:
		{
			int watchCount = 0;
			for (int i = 0; i < 4; i++)
				watchCount += watch(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index, 0);

			answer = solution(index + 1, count + watchCount);

			for (int i = 0; i < 4; i++)
				deleteTrace(curCameraRow + dr[i], curCameraCol + dc[i], dr[i], dc[i], index);
		}
		break;
	}

	return answer;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n >> m;
	for (int r = 0; r < n; r++)
	{
		for (int c = 0; c < m; c++)
		{
			cin >> room[r][c];
			if (1 <= room[r][c] && 5 >= room[r][c])
				cameras.push_back(make_pair(r, c));
			else if (0 == room[r][c])
				zeroCount++;
		}
	}

	int result = solution(0, 0);
	cout << zeroCount - result;

	return 0;
}