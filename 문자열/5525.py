# https://www.acmicpc.net/problem/5525
import sys

N = int(sys.stdin.readline())
S_len = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

pattern = "IOI"
i = 1
pattern_cnt = 0
ans = 0
while i < S_len-1:
    if S[i-1:i+2] == pattern:
        pattern_cnt += 1
        i += 2
        if pattern_cnt == N:
            ans += 1
            pattern_cnt -= 1
    else:
        i += 1
        pattern_cnt = 0
print(ans)