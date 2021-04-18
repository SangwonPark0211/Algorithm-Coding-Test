# https://www.acmicpc.net/problem/1057

n, x, y = list(map(int, input().split()))
round = 1
while True:
    if abs(x-y)==1 and x//2!=y//2:
        break
    x, y = x//2 + x%2, y//2 + y%2
    round += 1
print(round)
