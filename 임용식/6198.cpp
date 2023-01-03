#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stack>
#include <utility>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;
	stack<pair<int, int>> stk;
	int64_t answer = 0;

	for (int i = 1; i <= n; i++)
	{
		int height;
		cin >> height;
		while (!stk.empty() && stk.top().second <= height)
		{
			answer += i - stk.top().first - 1;
			stk.pop();
		}
		stk.push(make_pair(i, height));
	}

	while (!stk.empty())
	{
		answer += n - stk.top().first;
		stk.pop();
	}
	cout << answer;

	return 0;
}