#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <numeric>

#define DIV  1'000'000'000

using namespace std;

// ���̰� k�̰� ������ ���ڰ� m�� ��� memo[k][m]�� �޸�
int64_t memo[101][10];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;
	memo[1][0] = 0;
	for (int i = 1; i < 10; i++)
	{
		memo[1][i] = 1;
	}

	for (int len = 2; len <= n; len++)
	{
		for (int num = 0; num < 10; num++)
		{
			if (num - 1 < 0)
			{
				memo[len][num] = memo[len - 1][num + 1] % DIV;
			}
			else if (num + 1 > 9)
			{
				memo[len][num] = memo[len - 1][num - 1] % DIV;
			}
			else
			{
				memo[len][num] = (memo[len - 1][num - 1] % DIV + memo[len - 1][num + 1] % DIV) % DIV;
			}
		}
	}
	int64_t answer = 0;
	for (int i = 0; i < 10; i++)
	{
		answer += memo[n][i] % DIV;
	}
	answer %= DIV;
	cout << answer;


	return 0;
}