# https://www.acmicpc.net/problem/2437

#n입력받기
n=int(input())
#무게 입력받기
weight=list(map(int,input().split()))
weight.sort()

target = 1
for w in weight:
    if target<w:
        break
    else:
        target += w
print(target)