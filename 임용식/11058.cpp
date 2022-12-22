#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstring>
#include <stdint.h>

using namespace std;

int64_t memo[101];

int64_t solution(int cur)
{
	if (cur <= 0)
	{
		return 0;
	}
	if (memo[cur])
	{
		return memo[cur];
	}
	memo[cur] = solution(cur - 1) + 1;
	for (int i = cur - 3; i >= 0; i--)
	{
		memo[cur] = max(memo[cur], solution(i) * ((cur - 3) - i + 2));
	}
	return memo[cur];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;

	cout << solution(n);

	return 0;
}