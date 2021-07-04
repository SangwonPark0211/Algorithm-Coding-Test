# https://www.acmicpc.net/problem/2252

n, m = list(map(int, input().split()))

# adjacent list
adj_list = [[] for _ in range(n+1)]
# indegree list
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = list(map(int, input().split()))
    adj_list[x].append(y)
    indegree[y] += 1

st = [] # save 0 indegree vertex
for i in range(1,n+1):
    if indegree[i] == 0:
        st.append(i)
answer = []
while st:
    v = st.pop()
    answer.append(v)
    for x in adj_list[v]:
        indegree[x] -= 1
        if indegree[x] == 0:
            st.append(x)
for x in answer:
    print(x, end=' ')




