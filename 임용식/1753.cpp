#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAXV 20001
#define MAXE 300000
#define INF 0x7fff7fff

struct Path
{
	int vertex;
	int cost;

	friend bool operator>(const Path&, const Path&);
};
bool operator>(const Path& p1, const Path& p2)
{
	return p1.cost > p2.cost;
}

void solution(vector<vector<Path>>& graph, int start, vector<int>& dist)
{
	dist[start] = 0;
	priority_queue<Path, vector<Path>, greater<Path>> pq;
	pq.push({ start,dist[start] });

	while (!pq.empty())
	{
		auto cur = pq.top();
		pq.pop();

		for (int i = 0; i < graph[cur.vertex].size(); i++)
		{
			auto next = graph[cur.vertex][i];
			if (dist[next.vertex] > cur.cost + next.cost)
			{
				dist[next.vertex] = cur.cost + next.cost;
				Path temp = { next.vertex, dist[next.vertex] };
				pq.push(temp);
			}
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int v, e, start;
	cin >> v >> e >> start;
	vector<vector<Path>> graph(v + 1);
	for (int i = 0; i < e; i++)
	{
		int from, to, cost;
		cin >> from >> to >> cost;
		graph[from].push_back({ to, cost });
	}

	vector<int> dist(v + 1);
	for (int i = 1; i <= v; i++)
	{
		dist[i] = INF;
	}

	solution(graph, start, dist);

	for (int i = 1; i <= v; i++)
	{
		if (dist[i] == INF)
		{
			cout << "INF" << "\n";
		}
		else
		{
			cout << dist[i] << "\n";
		}
	}

	return 0;
}
