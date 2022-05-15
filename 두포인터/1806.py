# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
arr = list(map(int, input().split()))

i,j = 0,0
ans = float('inf')
temp = arr[0]
while True:
    if temp >= S:
        temp -= arr[i]
        ans = min(ans, j-i+1)
        i += 1
    else:
        j += 1
        if j == N:
            break
        temp += arr[j]
print(0) if ans==float('inf') else print(ans)
        

