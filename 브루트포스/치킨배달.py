# https://www.acmicpc.net/problem/15686

def dfs(cur, arr, m, comb):
    if len(cur)==m:
        comb.append(cur)
        return
    for i in range(len(arr)):
        dfs(cur+[arr[i]], arr[i+1:], m, comb)
        

n, m = list(map(int, input().split()))
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

house, chicken = [], []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))
comb = []
arr = [i for i in range(len(chicken))]
dfs([], arr, m, comb)

ans = float('inf')
for i in range(len(comb)):
    temp_sum = 0
    for x,y in house:
        min_dist = float('inf')
        for j in range(m):
            l = abs(x-chicken[comb[i][j]][0]) + abs(y-chicken[comb[i][j]][1])
            min_dist = min(min_dist, l)
        temp_sum += min_dist
    ans = min(ans, temp_sum)
print(ans)


