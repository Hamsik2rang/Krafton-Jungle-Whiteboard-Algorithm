#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <set>
#include <vector>

#define MAXT 1'000'000'000

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int64_t s, t;
	cin >> s >> t;

	if (s == t)
	{
		cout << 0;
		return 0;
	}

	queue<pair<int64_t, string>> q;
	set<int64_t> st;
	st.insert(s);
	q.push(make_pair(s, ""));
	while (!q.empty())
	{
		int64_t cur = q.front().first;
		string curString = q.front().second;
		q.pop();

		if (cur == t)
		{
			cout << curString;
			return 0;
		}

		if (cur * cur <= MAXT && st.find(cur * cur) == st.end())
		{
			q.push(make_pair(cur * cur, curString + "*"));
			st.insert(cur * cur);
		}
		if (cur + cur <= MAXT && st.find(cur + cur) == st.end())
		{
			q.push(make_pair(cur + cur, curString + "+"));
			st.insert(cur + cur);
		}
		if (cur != 0 && st.find(cur / cur) == st.end())
		{
			q.push(make_pair(cur / cur, curString + "/"));
			st.insert(cur / cur);
		}
	}
	cout << -1;

	return 0;
}
