# https://www.acmicpc.net/problem/9375

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    clothes = {}
    for i in range(n):
        wear, kind = sys.stdin.readline().split()
        if kind not in clothes:
            clothes[kind] = 0
        clothes[kind] += 1
    ans = 1
    for kind in clothes:
        ans *= clothes[kind] + 1
    print(ans-1)