# https://www.acmicpc.net/problem/1937
import sys
sys.setrecursionlimit(10**9)

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx,dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N and forest[x][y]<forest[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
    return dp[x][y]

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        dp[i][j] = dfs(i,j)
print(max(map(max,dp)))
