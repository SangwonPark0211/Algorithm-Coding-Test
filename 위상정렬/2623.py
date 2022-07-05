# https://www.acmicpc.net/problem/2623

N, M = map(int, input().split())
singers = []
for _ in range(M):
    temp = list(map(int, input().split()))
    singers.append(temp[1:])
for i in range(M):
    for j in range(len(singers[i])):
        singers[i][j] -= 1
adj_list = [[] for _ in range(N)]

for i in range(M):
    for j in range(len(singers[i])-1):
        adj_list[singers[i][j]].append(singers[i][j+1])

indegree = [0] * N
for i in range(len(adj_list)):
    for j in adj_list[i]:
        indegree[j] += 1

stack = []
ans = []
for i in range(len(indegree)):
    if indegree[i] == 0:
        stack.append(i)
while stack:
    x = stack.pop()
    ans.append(x)
    for i in range(len(adj_list[x])):
        indegree[adj_list[x][i]] -= 1
        if indegree[adj_list[x][i]] == 0:
            stack.append(adj_list[x][i])

if len(ans) != N:
    print(0)
else:
    for i in range(len(ans)):
        ans[i] += 1
    for num in ans:
        print(num)