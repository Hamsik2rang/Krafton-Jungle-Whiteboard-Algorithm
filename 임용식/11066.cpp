#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>

using namespace std;

int memo[501][501];
int files[501];
int fileSum[501];

int solution(int left, int right)
{
	if (left == right)
	{
		return 0;
	}
	if (memo[left][right])
	{
		return memo[left][right];
	}

	int& cur = memo[left][right];
	cur = 1e9;
	for (int mid = left; mid < right; mid++)
	{
		cur = min(cur, solution(left, mid) + solution(mid + 1, right) + fileSum[right] - fileSum[left - 1]);
	}

	return cur;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int k;
		cin >> k;
		memset(files, 0, sizeof(files));
		memset(memo, 0, sizeof(memo));
		for (int i = 0; i < k; i++)
		{
			cin >> files[i];
			if (i == 0)
			{
				fileSum[i] = files[i];
			}
			else
			{
				fileSum[i] = fileSum[i - 1] + files[i];
			}
		}

		auto answer = solution(0, k - 1);
		cout << answer << "\n";
	}

	return 0;
}