def solution(info, edges):
    def dfs(sheep: int, wolf: int) -> None:
        nonlocal vis, ret
        
        if sheep > wolf:
            ret.append(sheep)
        else:
            return
        
        for u, v in edges:
            if vis[u] and not vis[v]:
                vis[v] = True
                if info[v] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                vis[v] = False
    
    vis = [False] * len(info)
    ret = list()
    
    vis[0] = True
    dfs(1, 0)
    
    answer = max(ret)
    return answer
