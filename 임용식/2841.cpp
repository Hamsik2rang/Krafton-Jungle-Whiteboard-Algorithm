#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <stack>
#include <utility>

using namespace std;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, p;
	cin >> n >> p;
	stack<int> stk[7];
	int count = 0;
	for (int i = 0; i < n; i++)
	{
		int line, fret;
		cin >> line >> fret;

		while (!stk[line].empty() && stk[line].top() > fret)
		{
			stk[line].pop();
			count++;
		}

		if (!stk[line].empty() && stk[line].top() == fret)
		{
			continue;
		}
		stk[line].push(fret);
		count++;
	}

	cout << count;


	return 0;
}