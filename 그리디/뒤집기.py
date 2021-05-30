# https://www.acmicpc.net/problem/1439

s = input()
tmp = [0,0]
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        tmp[int(s[i-1])]+=1
tmp[int(s[-1])]+=1
print(min(tmp))