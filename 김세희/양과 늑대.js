function solution(info, edges) {
  var answer = 0;
  const graph = Array.from(new Array(info.length), () => []);
  edges.map(([par, chd]) => {
    graph[par].push(chd);
  });

  const dfs = (node, sheep, wolf, togo) => {
    const nextTogo = togo.filter((d) => d !== node);
    if (info[node]) {
      wolf += 1;
    } else {
      sheep += 1;
    }
    if (wolf >= sheep) {
      return;
    }
    if (sheep > answer) {
      answer = sheep;
    }
    for (let next of nextTogo) {
      dfs(next, sheep, wolf, [...nextTogo, ...graph[next]]);
    }
  };

  dfs(0, 0, 0, graph[0]);

  return answer;
}
