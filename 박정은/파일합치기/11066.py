t = int(input())
INF = int(10e9)

for _ in range(t):
	n = int(input())
	lst = [int(x) for x in input().split()]
	dpmem = [[0 for _ in range(n)] for _ in range(n)]
	
	for j in range(1, n):
		for i in range(j-1,-1,-1):
			small = INF
			for k in range(j-i):
				small = min(small, dpmem[i][i+k]+dpmem[i+k+1][j])
			dpmem[i][j] = small + sum(lst[i:j+1])
	print(dpmem[0][n-1])
