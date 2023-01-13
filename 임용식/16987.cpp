#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int n, answer;

void count(vector<pair<int, int>>& v)
{
	int count = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (!v[i].first)
		{
			count++;
		}
	}
	answer = max(answer, count);
	return;
}

void solution(vector<pair<int, int>>& v, int index)
{
	if (index == v.size())
	{
		count(v);
		return;
	}

	if (!v[index].first)
	{
		solution(v, index + 1);
		return;
	}
	bool hasCrashed = false;
	for (int i = 0; i < v.size(); i++)
	{
		if (i == index || v[i].first == 0)
		{
			continue;
		}
		hasCrashed = true;
		int leftOrigin = v[index].first;
		int rightOrigin = v[i].first;
		v[i].first -= v[index].second;
		v[i].first = v[i].first <= 0 ? 0 : v[i].first;
		v[index].first -= v[i].second;
		v[index].first = v[index].first <= 0 ? 0 : v[index].first;

		solution(v, index + 1);
		v[index].first = leftOrigin;
		v[i].first = rightOrigin;
	}

	if (!hasCrashed)
	{
		if (index == v.size() - 1)
		{
			count(v);
			return;
		}
		else
		{
			solution(v, index + 1);
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	vector<pair<int, int>> v;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int hp, weight;
		cin >> hp >> weight;
		v.push_back(make_pair(hp, weight));
	}

	solution(v, 0);
	cout << answer;

	return 0;
}