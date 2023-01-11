#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

#define MAXN 2001

int seq[MAXN];
bool memo[MAXN][MAXN];
bool check[MAXN][MAXN];

bool isPalindrome(int start, int end)
{
	if (end <= start)
	{
		return true;
	}
	else if (1 == end - start)
	{
		return seq[end] == seq[start];
	}
	else if (check[start][end])
	{
		return memo[start][end];
	}
	memo[start][end] = (seq[end] == seq[start]) && isPalindrome(start + 1, end - 1);
	check[start][end] = true;
	return memo[start][end];
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cin >> seq[i];
	}
	int m;
	cin >> m;
	for (int i = 0; i < m; i++)
	{
		int start;
		int end;
		cin >> start >> end;
		cout << isPalindrome(start, end) << "\n";
	}

	return 0;
}