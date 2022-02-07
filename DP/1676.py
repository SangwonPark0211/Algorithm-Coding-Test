# https://www.acmicpc.net/problem/1676

dp = [1]*501
for i in range(2,501):
    dp[i] = dp[i-1] * i
num = int(input())
num_fac = list(str(dp[num]))
num_fac.reverse()
cnt = 0
for i in range(len(num_fac)):
    if num_fac[i] != '0':
        break
    cnt += 1
print(cnt)

'''
short coding
'''
# t = int(input())
# print(t//5 + t//25 + t//125)
