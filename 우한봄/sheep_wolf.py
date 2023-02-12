def solution(info, edges):

    visit=[False]*len(info)    
    answer=[]
    
    def dfs(sheep_cnt,wolf_cnt):
        if sheep_cnt<=wolf_cnt:
            return
        else:
            answer.append(sheep_cnt)

        for p,c in edges:
            if visit[p] and not visit[c]:
                visit[c]=True
                if info[c]==0:
                    dfs(sheep_cnt+1, wolf_cnt)
                else:
                    dfs(sheep_cnt, wolf_cnt+1)
                visit[c]=False
                    
    visit[0]=1
    dfs(1,0)
    return max(answer)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))