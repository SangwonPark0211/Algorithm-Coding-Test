# https://www.acmicpc.net/problem/1107

target = int(input())
broken_n = int(input())
broken = set(list(input().split()))

ans = abs(target-100)
for i in range(1000001):
    str_i = str(i)
    flag = 0
    for s in str_i:
        if s in broken:
            flag = 1
            break
    if flag==0:
        ans = min(ans, len(str_i)+abs(i-target))

print(ans)